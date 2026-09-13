# 写博客和发布

电脑已经有 Python 和 Git。日常写作只需要工作目录 `E:\blogs` 中的两个脚本，不需要 Ruby。脚本从自身位置定位仓库，不依赖终端当前所在目录。

## 1. 新建 Markdown 文章

在 `E:\blogs` 的 PowerShell 中运行：

```powershell
.\new-post.cmd "我的文章标题"
```

也可以双击 `new-post.cmd`，按提示输入标题。

新文件位于 `liboqiao1234.github.io\_posts\当天日期-文章标题.md`。用 VS Code、Typora 或其他 Markdown 编辑器打开，保留开头由 `---` 包围的文章信息，在后面写正文。标题、日期和标签已经填好；`excerpt` 可以写一句摘要。脚本会输出文件的完整路径，同名文件不会被覆盖。

可选：自定义链接名称和标签。

```powershell
.\new-post.cmd "关于大模型记忆的笔记" --slug llm-memory --tags "LLM,论文阅读"
```

文章发布后的地址类似 `/blog/2026/09/llm-memory/`，并自动出现在 Blog 页面。文件名里的月份决定链接，不要在发布后随意重命名。

Markdown 支持标题、列表、引用、表格、代码块和图片。例如：

````markdown
## 我的笔记

这里是正文。

```python
print("hello")
```

![示意图](/images/posts/2026-09-13-llm-memory/figure.png)
````

将图片放在仓库内对应的 `images/posts/日期-文章名/` 目录。新文章文件中的注释会给出可直接使用的图片路径。

## 2. 保存并发布

写完并保存文件后，在 `E:\blogs` 运行：

```powershell
.\publish.cmd
```

也可以双击 `publish.cmd`。无参数启动时，脚本结束后按 Enter 关闭窗口。

它会检查文章的基本格式和正文，提交**整个网站仓库内尚未提交的修改**（包括新文章、图片、主页和删除操作），同步远程 `main` 的更新，然后上传。成功后会显示网站和构建状态链接。GitHub 完成构建后，网站才会更新；上传成功不代表构建已经完成。

可选：填写提交说明，或只做本地检查。

```powershell
.\publish.cmd "添加大模型记忆笔记"
.\publish.cmd --check
```

`--check` 不提交、不上传、不联网。尚未填写正文的新文章会阻止发布。脚本只从 `main` 发布；遇到远程冲突会取消自动合并，保留你的本地提交，不会强制覆盖远程。

上传因网络中断失败时，修复网络后再运行同一个发布脚本即可，已有本地提交不会丢失。脚本沿用 Git 登录，并优先使用 Git/环境变量的代理设置，否则尝试读取 Windows 系统代理。必要时可在当前 PowerShell 临时指定：

```powershell
$env:BLOG_PROXY = "http://127.0.0.1:7890"
.\publish.cmd
```

脚本不会修改全局 Git 设置或关闭 HTTPS 证书验证。若 GitHub 登录失效，按 Git 的浏览器提示重新授权即可。

仓库里的 `scripts/new-post.cmd` 和 `scripts/publish.cmd` 也可直接使用；以后重新 clone 仓库时，这两个入口会一起保留。
