"""Create Markdown posts and publish this website using Python and Git only."""
from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
SHANGHAI = timezone(timedelta(hours=8))
SITE_URL = "https://liboqiao1234.github.io"
ACTIONS_URL = "https://github.com/liboqiao1234/liboqiao1234.github.io/actions"


class BlogError(Exception):
    pass


def new_post(root: Path, title: str, slug: str | None = None, tags: str = "") -> Path:
    title = title.strip()
    if not title:
        raise BlogError("文章标题不能为空。")
    name = unicodedata.normalize("NFKC", slug if slug is not None else title).lower()
    if slug is not None and (not name or any(not (c.isalnum() or c == "-") for c in name)):
        raise BlogError("--slug 只能包含文字、数字和连字符，例如 llm-memory。")
    name = re.sub(r"-+", "-", "".join(c if c.isalnum() else "-" for c in name)).strip("-")
    if not name:
        raise BlogError("标题需要包含文字或数字；也可以用 --slug 指定文件名。")
    # Leave room for the date prefix and extension on Windows filesystems.
    if len(name.encode("utf-8")) > 180:
        raise BlogError("标题较长，请用 --slug 指定较短的文件名。")
    now = datetime.now(SHANGHAI)
    stem = f"{now:%Y-%m-%d}-{name}"
    posts = root / "_posts"
    posts.mkdir(exist_ok=True)
    destination = posts / f"{stem}.md"
    tag_list = [tag.strip() for tag in re.split(r"[,，]", tags) if tag.strip()]
    content = (
        "---\n"
        f"title: {json.dumps(title, ensure_ascii=False)}\n"
        f"date: {now:%Y-%m-%d %H:%M:%S} +0800\n"
        f"tags: {json.dumps(tag_list, ensure_ascii=False)}\n"
        'excerpt: ""\n'
        "---\n\n"
        "<!-- 在这里开始写 Markdown 正文。上面的 excerpt 可填写一句摘要。\n"
        f"图片可放在 images/posts/{stem}/，然后插入：\n"
        f"![图片说明](/images/posts/{stem}/example.png)\n"
        "写完保存，再运行 publish.cmd 发布。 -->\n\n"
    )
    try:
        with destination.open("x", encoding="utf-8", newline="\n") as output:
            output.write(content)
    except FileExistsError:
        raise BlogError(f"文章已经存在，未覆盖：{destination}\n请直接编辑它，或换一个 --slug。") from None
    return destination


def validate_posts(root: Path) -> None:
    for post in sorted((root / "_posts").rglob("*")):
        if not post.is_file() or post.suffix.lower() not in (".md", ".markdown"):
            continue
        date_match = re.match(r"^(\d{4}-\d{2}-\d{2})-.+\.(?:md|markdown)$", post.name)
        if not date_match:
            raise BlogError(f"文章文件名应为 YYYY-MM-DD-title.md：{post.name}")
        try:
            datetime.strptime(date_match.group(1), "%Y-%m-%d")
        except ValueError:
            raise BlogError(f"文章文件名中的日期无效：{post.name}") from None
        text = post.read_text(encoding="utf-8-sig")
        front = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)(.*)\Z", text, re.DOTALL)
        if not front or not re.search(r"(?m)^title:[ \t]*\S", front.group(1)):
            raise BlogError(f"文章缺少包含 title 的 YAML 头部，请保留开头的两行 ---：{post.name}")
        body = re.sub(r"<!--.*?-->", "", front.group(2), flags=re.DOTALL).strip()
        if not body:
            raise BlogError(f"文章正文还没写，暂不发布：{post.name}")


def system_proxy() -> str | None:
    """Honor explicit overrides and Git/environment settings before Windows settings."""
    if os.environ.get("BLOG_PROXY"):
        return os.environ["BLOG_PROXY"]
    if any(os.environ.get(name) for name in ("HTTPS_PROXY", "https_proxy", "ALL_PROXY", "all_proxy")):
        return None
    if os.name != "nt":
        return None
    try:
        import winreg
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Internet Settings") as key:
            if not winreg.QueryValueEx(key, "ProxyEnable")[0]:
                return None
            value = winreg.QueryValueEx(key, "ProxyServer")[0]
        if "=" in value:
            choices = dict(item.strip().split("=", 1) for item in value.split(";") if "=" in item)
            value = choices.get("https") or choices.get("http")
        if value:
            return value if "://" in value else "http://" + value
    except (OSError, ValueError):
        pass
    return None


class Git:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.command = ["git", "-c", f"safe.directory={self.root.as_posix()}", "-c", "http.sslVerify=true", "-c", "http.version=HTTP/1.1"]
        configured = self.run("config", "--get", "http.proxy", check=False)
        proxy = os.environ.get("BLOG_PROXY") or (system_proxy() if configured.returncode != 0 else None)
        if proxy:
            self.command += ["-c", f"http.proxy={proxy}"]

    def run(self, *args: str, check: bool = True) -> subprocess.CompletedProcess:
        result = subprocess.run(self.command + list(args), cwd=self.root, capture_output=True, encoding="utf-8", errors="replace")
        if check and result.returncode:
            raise BlogError(f"Git 操作失败（{' '.join(args[:2])}）：\n{result.stderr.strip()}\n本地文件和提交仍保留，可修复问题后重新运行 publish.cmd。")
        return result


def publish(root: Path, message: str | None = None, check_only: bool = False) -> None:
    git = Git(root)
    if git.run("branch", "--show-current").stdout.strip() != "main":
        raise BlogError("当前不是 main 分支。请先确认要发布的版本并切换到 main。")
    for marker in ("MERGE_HEAD", "rebase-merge", "rebase-apply", "CHERRY_PICK_HEAD", "REVERT_HEAD"):
        path = Path(git.run("rev-parse", "--git-path", marker).stdout.strip())
        if not path.is_absolute():
            path = root / path
        if path.exists():
            raise BlogError("Git 中还有未完成的合并操作，请先处理完成再发布。")
    validate_posts(root)
    git.run("remote", "get-url", "origin")
    status = git.run("-c", "core.quotepath=false", "status", "--short").stdout.strip()
    print("待提交的修改：\n" + (status or "（没有未提交的修改；仍会检查是否有待上传的提交。）"), flush=True)
    if check_only:
        print("检查通过。--check 只检查文章格式和本地状态，没有提交或联网。", flush=True)
        return
    if status:
        git.run("add", "--all")
        staged = git.run("diff", "--cached", "--quiet", check=False)
        if staged.returncode == 1:
            commit_message = message or f"Update blog ({datetime.now(SHANGHAI):%Y-%m-%d %H:%M})"
            git.run("commit", "-m", commit_message)
        elif staged.returncode:
            raise BlogError("无法检查暂存区；未进行上传。")
    print("正在同步远程更新……", flush=True)
    git.run("fetch", "origin", "main")
    ancestor = git.run("merge-base", "--is-ancestor", "origin/main", "HEAD", check=False)
    if ancestor.returncode == 1:
        rebase = git.run("rebase", "origin/main", check=False)
        if rebase.returncode:
            git.run("rebase", "--abort")
            raise BlogError("本地修改与远程更新冲突，已取消本次合并并恢复本地提交。\n请先解决冲突，再运行 publish.cmd。")
    elif ancestor.returncode:
        raise BlogError("无法比较本地与远程历史；未进行上传。")
    validate_posts(root)
    print("正在上传 main……", flush=True)
    git.run("push", "origin", "main")
    print(f"上传完成。GitHub 会自动构建并发布；构建失败时旧版本仍在线。\n网站：{SITE_URL}\n构建状态：{ACTIONS_URL}", flush=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="新建 Markdown 博客，或提交并上传网站更新。")
    commands = parser.add_subparsers(dest="command", required=True)
    create = commands.add_parser("new", help="新建 Markdown 文章")
    create.add_argument("title", nargs="?", help="文章标题；不填时会提示输入")
    create.add_argument("--slug", help="可选的链接名称，例如 llm-memory")
    create.add_argument("--tags", default="", help="可选标签，用逗号分隔")
    release = commands.add_parser("publish", help="提交并上传整个网站的修改")
    release.add_argument("message", nargs="?", help="可选的提交说明")
    release.add_argument("--check", action="store_true", help="只检查本地，不提交或联网")
    args = parser.parse_args()
    try:
        if args.command == "new":
            title = args.title if args.title is not None else input("文章标题：")
            post = new_post(ROOT, title, args.slug, args.tags)
            print(f"已新建 Markdown 文章：\n{post}\n\n用你喜欢的 Markdown 编辑器打开，写完保存后运行 publish.cmd。")
        else:
            publish(ROOT, args.message, args.check)
        return 0
    except (BlogError, OSError, UnicodeError) as exc:
        print(f"\n未完成：{exc}", file=sys.stderr)
        return 1
    except (KeyboardInterrupt, EOFError):
        print("\n已取消。", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
