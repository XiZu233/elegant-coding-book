# 链接与引用有效性检查报告

> 检查时间：2026-05-02
> 检查范围：src/chapter-00.md 至 src/chapter-07.md、src/appendix-a.md 至 src/appendix-g.md、src/reference.md
> 检查工具：curl -I --max-time 10

---

## 外部URL检查结果

| URL | 位置 | HTTP状态 | 状态 |
|-----|------|---------|------|
| https://code.visualstudio.com/ | chapter-01.md:19 | 200 | 正常 |
| https://www.python.org/downloads/ | chapter-01.md:60 | 200 | 正常 |
| https://git-scm.com/downloads | chapter-01.md:155 | 301 | 正常（重定向） |
| https://claude.ai/install.ps1 | chapter-01.md:211, chapter-03.md:285 | 302 | 正常（重定向） |
| https://claude.ai/install.sh | chapter-01.md:216, chapter-03.md:280 | 302 | 正常（重定向） |
| https://www.kimi.com/code/console | chapter-01.md:223 | 200 | 正常 |
| https://code.visualstudio.com/docs | chapter-01.md:313 | 200 | 正常 |
| https://docs.python.org/zh-cn/3/tutorial/ | chapter-01.md:314 | 200 | 正常 |
| https://git-scm.com/doc | chapter-01.md:315 | 200 | 正常 |
| https://www.kimi.com/code/docs | chapter-01.md:316, reference.md:2 | 302 | 正常（重定向） |
| https://console.anthropic.com | chapter-01.md:338 | 302 | 正常（重定向） |
| https://code.claude.com/docs/zh-CN/ | chapter-04.md:7, reference.md:1, appendix-f.md:20 | 200 | 正常 |
| https://github.com/MrNine-666/claude-code-quickstart | reference.md:3, appendix-f.md:51 | 200 | 正常 |
| https://code.visualstudio.com/Docs | reference.md:5, appendix-f.md:66 | 200 | 正常 |
| https://docs.python.org/3/ | reference.md:6, appendix-f.md:81 | 200 | 正常 |
| https://paulgraham.com/ | reference.md:9, appendix-f.md:110 | 200 | 正常 |
| https://vibecoding.cn/guide | reference.md:11, appendix-f.md:96 | 200 | 正常 |
| https://github.com/PHY041/vibe-coding-cookbook | reference.md:13, appendix-f.md:96 | 200 | 正常 |
| https://github.com/XiZu233/elegant-coding-book | appendix-e.md:149 | 200 | 正常 |
| https://github.com/XiZu233/elegant-coding-book/blob/main/docs/CONTRIBUTING.md | appendix-e.md:199 | 200 | 正常 |
| https://github.com/XiZu233/elegant-coding-book/actions/workflows/test-examples.yml/badge.svg | appendix-e.md:203 | 200 | 正常 |
| https://github.com/XiZu233/elegant-coding-book/blob/main/LICENSE | appendix-e.md:207 | 200 | 正常 |
| https://github.com/astral-sh/ruff-pre-commit | appendix-e.md:757 | 200 | 正常 |
| https://github.com/pre-commit/pre-commit-hooks | appendix-e.md:764 | 200 | 正常 |
| https://api.moonshot.cn/v1 | chapter-03.md:370 | 404 | 失效（API基础路径，非浏览器访问地址） |
| https://geocoding-api.open-meteo.com/v1/search?name=Beijing&count=1 | appendix-a.md:286 | 200 | 正常 |
| https://api.open-meteo.com/v1/forecast?latitude=... | appendix-a.md:287 | 200 | 正常 |
| https://code.kimi.com/install.sh | chapter-03.md:362, appendix-f.md:40 | 未检查 | 安装脚本URL（与claude.ai/install.sh类似，预期可访问） |
| https://old-api.example.com | chapter-02.md:369 | 未检查 | 示例占位URL，非真实链接 |
| http://localhost:3000 | appendix-b.md:413 | 未检查 | 本地开发地址，非外部链接 |
| http://localhost:5000 | appendix-e.md:588 | 未检查 | 本地开发地址，非外部链接 |

---

## 失效链接

| URL | 位置 | 状态码 | 建议 |
|-----|------|--------|------|
| https://api.moonshot.cn/v1 | chapter-03.md:370 | 404 | 这是Moonshot API的基础路径，本身不是供浏览器访问的页面。建议改为说明性文字，如"API基础URL为 https://api.moonshot.cn/v1"，不作为可点击链接处理 |

---

## 内部引用问题

### 1. 章节引用格式检查

| 位置 | 引用内容 | 问题 | 建议 |
|------|---------|------|------|
| chapter-04.md:56 | "（文件路径详见第06章2.1节）" | 格式正确 | 无 |
| chapter-04.md:58 | "（包管理器详见第06章3.1节）" | 格式正确 | 无 |
| chapter-04.md:216 | "（Git工作区详见第06章相关章节）" | 格式正确，但"相关章节"较模糊 | 建议改为"详见第06章2.1节"（如Git工作区对应路径章节） |
| chapter-03.md:476 | "见第02章" | 格式正确 | 无 |
| chapter-07.md:62 | "（会话的工作内存，见第04章术语表）" | 格式正确 | 无 |
| chapter-07.md:120 | "（见第04章术语表）" | 格式正确 | 无 |
| chapter-07.md:253 | "（见第04章4.4节）" | 格式正确 | 无 |

### 2. 附录引用检查

| 位置 | 引用内容 | 问题 | 建议 |
|------|---------|------|------|
| 全书多处 | "详见附录D" | 格式统一 | 无问题。所有配图占位引用均指向 appendix-d.md，该文件存在 |
| appendix-c.md:9 | "详见附录D" | 指向正确 | appendix-d.md 存在 |
| appendix-b.md:9 | "详见附录D" | 指向正确 | appendix-d.md 存在 |

### 3. 潜在问题

| 位置 | 引用内容 | 问题 | 建议 |
|------|---------|------|------|
| chapter-05.md:281 | "详见附录D"（配图占位：项目目录树形图（Next.js 仪表盘）） | 案例二标题为"批量重命名照片"，但配图描述为"Next.js 仪表盘"，与附录A内容混淆 | 修正配图占位描述为"批量重命名照片项目结构" |
| chapter-01.md:210-211 | 安装Kimi Code的标题下使用Claude Code安装脚本 | 命令URL为claude.ai而非kimi.com | 经确认，这是教材中的已知设计问题（详见format-structure.md检查报告）。第01章使用Claude Code安装脚本介绍Kimi Code，第03章才给出Kimi Code专属安装命令 |
| chapter-03.md:351-363 | Kimi Code安装命令与第01章不一致 | 第01章使用claude.ai脚本，第03章使用npm和code.kimi.com脚本 | 建议统一两处安装方式，避免读者困惑 |

---

## 参考文档引用检查

### reference.md 中列出的外部资源

| 资源 | URL | 状态 | 在教材中是否被引用 |
|------|-----|------|-------------------|
| Claude Code Docs | https://code.claude.com/docs/zh-CN/ | 200 | 是（chapter-04.md, appendix-f.md） |
| Kimi Code 文档 | https://www.kimi.com/code/docs/ | 302 | 是（chapter-01.md, chapter-03.md） |
| CCQ GitHub | https://github.com/MrNine-666/claude-code-quickstart | 200 | 是（appendix-f.md） |
| VS Code 文档 | https://code.visualstudio.com/Docs | 200 | 是（chapter-01.md, appendix-f.md） |
| Python 文档 | https://docs.python.org/3/ | 200 | 是（chapter-01.md, appendix-f.md） |
| 人人都是产品经理 | （无URL，书籍） | - | 是（chapter-07.md, appendix-f.md） |
| 黑客与画家 | （无URL，书籍） | - | 是（chapter-07.md, appendix-f.md） |
| Paul Graham博客 | https://paulgraham.com/ | 200 | 是（chapter-07.md, appendix-f.md） |
| vibeconding指南 | https://vibecoding.cn/guide | 200 | 是（appendix-f.md） |
| vibe coding cookbook | https://github.com/PHY041/vibe-coding-cookbook | 200 | 是（appendix-f.md） |

### 未在 reference.md 中列出的外部引用

| URL | 位置 | 说明 |
|-----|------|------|
| https://console.anthropic.com | chapter-01.md:338 | Claude Code API Key获取页面，未在reference.md中列出 |
| https://github.com/XiZu233/elegant-coding-book | appendix-e.md:149 | 配套GitHub仓库，属于附录E内容，非外部参考资源 |
| https://geocoding-api.open-meteo.com/ | appendix-a.md:286 | Open-Meteo免费API，仅在附录A实战案例中使用 |
| https://api.open-meteo.com/ | appendix-a.md:287 | Open-Meteo免费API，仅在附录A实战案例中使用 |
| https://github.com/astral-sh/ruff-pre-commit | appendix-e.md:757 | 预提交钩子配置中的仓库地址 |
| https://github.com/pre-commit/pre-commit-hooks | appendix-e.md:764 | 预提交钩子配置中的仓库地址 |

> 建议：将 https://console.anthropic.com 添加到 reference.md 中，作为Claude Code相关资源的一部分。

---

## 统计

- 外部URL总数：27（排除本地地址和示例占位URL）
- 可访问：26
- 失效：1（https://api.moonshot.cn/v1，为API基础路径，非浏览器页面）
- 重定向：5（均正常，301/302为服务器正常重定向）
- 内部引用问题：3（1个配图描述错误 + 2个安装命令不一致）
- 参考文档缺失项：1（console.anthropic.com 未在 reference.md 中列出）

---

## 总结

1. **外部链接整体健康**：教材中引用的外部URL绝大部分可正常访问，仅1个API基础路径返回404（属于正常现象，该URL不是供浏览器访问的页面）。

2. **内部引用基本规范**：章节间引用格式统一，"详见第XX章X.X节"格式使用一致。所有对附录D的引用均指向存在的文件。

3. **已知问题**：
   - chapter-05.md:281 配图占位描述与章节内容不符（Next.js仪表盘 vs 批量重命名照片）
   - chapter-01.md 和 chapter-03.md 中 Kimi Code 的安装方式不一致
   - reference.md 未包含 console.anthropic.com

4. **无需修复的链接**：
   - 所有返回301/302的链接均为正常服务器重定向，不影响访问
   - localhost地址为本地开发环境地址，无需检查
   - example.com为示例占位域名，非真实链接
