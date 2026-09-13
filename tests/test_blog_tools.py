"""Exercise writing and publishing against disposable local Git remotes."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("blog_tools", Path(__file__).resolve().parents[1] / "scripts/blog.py")
blog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(blog)


def git(root, *args):
    result = subprocess.run(["git", "-c", f"safe.directory={root.as_posix()}", *args], cwd=root, capture_output=True, encoding="utf-8", errors="replace")
    if result.returncode:
        raise AssertionError(result.stderr)
    return result.stdout.strip()


class BlogToolsTests(unittest.TestCase):
    def setUp(self):
        temporary_root = Path(tempfile.gettempdir()).resolve()
        self.temporary = tempfile.TemporaryDirectory(prefix="academic-blog-tools-", dir=temporary_root)
        self.area = Path(self.temporary.name).resolve()
        # Verify the disposable directory before registering recursive cleanup.
        assert self.area.is_relative_to(temporary_root) and self.area != temporary_root
        self.addCleanup(self.temporary.cleanup)
        self.repo = self.area / "site"
        self.repo.mkdir()
        git(self.repo, "init", "--initial-branch=main")
        self.set_identity(self.repo)
        (self.repo / "README.md").write_text("Initial website\n", encoding="utf-8")
        git(self.repo, "add", ".")
        git(self.repo, "commit", "-m", "Initial website")
        self.remote = self.area / "remote.git"
        self.remote.mkdir()
        git(self.remote, "init", "--bare", "--initial-branch=main")
        git(self.repo, "remote", "add", "origin", str(self.remote))
        git(self.repo, "push", "-u", "origin", "main")

    @staticmethod
    def set_identity(repo):
        git(repo, "config", "user.name", "Blog Tool Test")
        git(repo, "config", "user.email", "test@example.invalid")
        git(repo, "config", "commit.gpgsign", "false")
        git(repo, "config", "core.autocrlf", "false")

    def writer(self):
        other = self.area / "other-writer"
        git(self.area, "clone", "--branch", "main", str(self.remote), str(other))
        self.set_identity(other)
        return other

    def ready_post(self):
        post = blog.new_post(self.repo, '中文标题："LLM" 与 Markdown', slug="llm-notes", tags="LLM，论文阅读")
        with post.open("a", encoding="utf-8") as output:
            output.write("研究笔记正文。\n\n```python\nprint('hello')\n```\n")
        return post

    def test_unicode_metadata_and_no_overwrite_or_path_escape(self):
        title = '中文 "引号" 与换行\n标题'
        post = blog.new_post(self.repo, title, slug="safe-name", tags="LLM，笔记")
        original = post.read_bytes()
        title_line = post.read_text(encoding="utf-8").splitlines()[1]
        self.assertEqual(json.loads(title_line.removeprefix("title: ")), title)
        with self.assertRaises(blog.BlogError):
            blog.new_post(self.repo, "另一个标题", slug="safe-name")
        self.assertEqual(post.read_bytes(), original)
        with self.assertRaises(blog.BlogError):
            blog.new_post(self.repo, "外部路径", slug="../outside")

    def test_blank_post_blocks_publish_and_check_is_read_only(self):
        post = blog.new_post(self.repo, "未完成文章")
        initial = git(self.repo, "rev-parse", "HEAD")
        with self.assertRaises(blog.BlogError):
            blog.publish(self.repo)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), initial)
        with post.open("a", encoding="utf-8") as output:
            output.write("现在有正文。\n")
        # A check should work even when the remote is unavailable.
        git(self.repo, "remote", "set-url", "origin", str(self.area / "missing.git"))
        blog.publish(self.repo, check_only=True)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), initial)
        self.assertEqual(git(self.repo, "diff", "--cached", "--name-only"), "")

    def test_upload_and_retry_after_network_failure(self):
        post = self.ready_post()
        git(self.repo, "remote", "set-url", "origin", str(self.area / "missing.git"))
        with self.assertRaises(blog.BlogError):
            blog.publish(self.repo, "New Markdown post")
        committed = git(self.repo, "rev-parse", "HEAD")
        self.assertEqual(git(self.repo, "status", "--porcelain"), "")
        git(self.repo, "remote", "set-url", "origin", str(self.remote))
        blog.publish(self.repo)
        self.assertEqual(git(self.remote, "rev-parse", "main"), committed)
        self.assertIn("研究笔记正文", git(self.remote, "show", f"main:{post.relative_to(self.repo).as_posix()}"))
        blog.publish(self.repo)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), committed)

    def test_remote_changes_are_preserved(self):
        other = self.writer()
        (other / "remote-note.md").write_text("Remote update\n", encoding="utf-8")
        git(other, "add", ".")
        git(other, "commit", "-m", "Remote change")
        git(other, "push", "origin", "main")
        post = self.ready_post()
        blog.publish(self.repo)
        self.assertEqual((self.repo / "remote-note.md").read_text(), "Remote update\n")
        self.assertIn(post.name, git(self.remote, "ls-tree", "-r", "--name-only", "main"))

    def test_conflict_restores_local_commit_without_overwriting_remote(self):
        other = self.writer()
        (other / "README.md").write_text("Remote version\n", encoding="utf-8")
        git(other, "add", ".")
        git(other, "commit", "-m", "Remote change")
        git(other, "push", "origin", "main")
        remote_head = git(self.remote, "rev-parse", "main")
        (self.repo / "README.md").write_text("Local version\n", encoding="utf-8")
        git(self.repo, "add", ".")
        git(self.repo, "commit", "-m", "Local change")
        local_head = git(self.repo, "rev-parse", "HEAD")
        with self.assertRaises(blog.BlogError):
            blog.publish(self.repo)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), local_head)
        self.assertEqual(git(self.remote, "rev-parse", "main"), remote_head)
        self.assertEqual((self.repo / "README.md").read_text(), "Local version\n")
        self.assertFalse((self.repo / ".git/rebase-merge").exists())


if __name__ == "__main__":
    unittest.main()
