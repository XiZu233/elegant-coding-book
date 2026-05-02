# AI时代的优雅编程

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://[你的用户名].github.io/elegant-coding-book/)

## 项目简介

本项目是一本面向零基础读者的编程入门教程，核心教学理念是**"先动手，再理解"**。读者将学会如何与AI协作完成编程任务——从描述需求、生成代码，到运行验证、迭代优化，全程不需要死记语法，也能写出优雅、可维护的Python代码。

## 在线阅读

访问 GitHub Pages 在线阅读完整教程：

https://[你的用户名].github.io/elegant-coding-book/

> 请将 `[你的用户名]` 替换为你的 GitHub 用户名。

## 目录

| 章节 | 内容 | 代码 |
|------|------|------|
| 00 | 编程在AI时代的重新定义 | - |
| 01 | 搭建基础开发环境 | `code/chapter-01-setup/` |
| 02 | 编程语法和代码审美 | `code/chapter-02-python-basics/` |
| 03 | AI编程工具入门 | `code/chapter-03-ai-tools/` |
| 04 | 概念介绍与最佳实践 | `code/chapter-04-best-practices/` |
| 05 | 实战案例 | `code/chapter-05-projects/` |
| 06 | Agent时代需要补充的知识基础 | `code/chapter-06-agent-knowledge/` |
| 07 | 优雅编程的长期主义 | `code/chapter-07-long-term/` |

## 本地开发

本项目使用 [mdBook](https://github.com/rust-lang/mdBook) 构建。

```bash
# 安装 mdBook
cargo install mdbook

# 本地预览
mdbook serve

# 打开浏览器访问 http://localhost:3000
```

## 配套代码使用

每章均配有可运行的示例代码，位于 `code/` 目录下。

```bash
cd code
python -m pytest tests/ -v
```

## 项目结构

```
.
├── src/              # mdBook 源文件
├── code/             # 配套示例代码
├── book.toml         # mdBook 配置文件
└── .github/          # GitHub Actions 工作流
```

## License

[MIT](LICENSE)
