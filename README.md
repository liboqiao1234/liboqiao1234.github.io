# Boqiao Li — academic homepage and blog

基于 [Academic Pages](https://github.com/academicpages/academicpages.github.io)。

## 网站结构

- `/`：学术首页；编辑 `_pages/about.md`。
- `/blog/`：文章目录；旧文章由 `_data/legacy_posts.json` 索引，支持搜索。
- `/blog/legacy/`：原博客首页。
- 旧文章、分类、标签、归档和图片保留原地址。
- 新文章：在 `_posts/` 添加 `YYYY-MM-DD-title.md`，写入 `title`、`date` 和正文；新文章自动出现在 Blog 页面。

## 个人资料

在 `_config.yml` 更新姓名、头像、学校、邮箱等信息。姓名来自本地 Git 作者信息（李泊桥）及原站 LinkedIn 链接（boqiao-li）；邮箱、头像沿用旧站，学校和研究方向来自 GitHub 简介。当前身份和学术链接可继续补充。

首页论文和项目由 `_data/publications.yml`、`_data/projects.yml` 管理；列表为空时不显示。添加条目后会自动出现。没有保留模板的虚构论文、教学、简历或新闻。

## 本地预览

安装 Ruby 3.3 和 Bundler 后（Windows 请使用包含 Devkit 的 RubyInstaller，并完成 MSYS2 开发工具安装）：

```sh
bundle install
bundle exec jekyll serve
```

访问 http://localhost:4000 。预览产物 `_site/` 不提交。

## 发布到 GitHub Pages

仓库 Settings → Pages → Source 选择 **GitHub Actions**。`academic-redesign` 分支只构建验证；推送到 `main` 后自动部署。

迁移以 `https://liboqiao1234.github.io` 为主地址。旧 `CNAME` 内容含 `https://`，不是合法的 CNAME 文件格式，已保存到备份，暂不沿用；如需恢复自定义域名，应先确认域名控制权，再按纯域名填写。

## 备份与许可证

旧站备份分支：`backup/pre-academic-2026-09-13`。完整网页 ZIP 和 Git 历史 bundle 位于工作目录外的 `E:\blogs\backups`。

原站许可证保留于 `LICENSE`；Academic Pages 模板许可证为 `LICENSE-academicpages`。迁移详情见 `docs/MIGRATION.md`。
