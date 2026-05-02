# 参考文档调研报告

## 概述

**调研范围**：本次调研覆盖了《参考文档.md》中列出的全部来源，包括 Claude Code / Kimi Code 官方文档、VS Code / Python 官方文档、CCQ GitHub 项目、Paul Graham 博客、vibe coding 相关资源，以及"人人都是产品经理"书籍相关内容。

**调研方法**：使用 WebFetch、WebSearch、mcp__exa__web_search_exa、mcp__deepwiki__ask_question 等工具获取网页和文档内容，结合教程现有章节进行比对分析。

**总体发现**：
1. 教程对 Claude Code / Kimi Code 官方文档的覆盖已经相当全面，但仍有少量可补充的最佳实践细节。
2. Paul Graham 的博客文章是教程"长期主义"和"编程素养"部分的优质素材来源，多篇经典文章的观点可以直接丰富内容。
3. "人人都是产品经理"的核心概念（用户思维、需求分析 Y 模型）与教程 07 章的产品思维部分高度契合，可作为理论补充。
4. vibe coding 相关资源对零基础读者过于侧重前端工程化，与教程定位不符。
5. CCQ 项目的自动化安装思路值得借鉴，但复杂度超出零基础范围。

---

## 各来源详细分析

### 1. Claude Code 官方文档（https://code.claude.com/docs/zh-CN/）

- **核心内容摘要**：Claude Code 是一个代理编码工具，可读取代码库、编辑文件、运行命令并与开发工具集成。官方文档涵盖快速开始、核心概念（Agentic Loop、Context Window、CLAUDE.md 等）、最佳实践、常见工作流、平台集成和 Agent SDK 等内容。

- **可吸收到教程的知识点**：
  - **知识点 1：Claude Code 的"首次使用"引导方式** —— 官方文档在安装后提示"首次使用时，系统会提示你登录。就这样！"，这种极简的 onboarding 思路可以借鉴。→ 建议融入章节：第 01 章（搭建基础开发环境），方式：在介绍安装步骤时，强调"安装即完成，无需复杂配置"的零负担理念。
  - **知识点 2：官方推荐的"后续步骤"路径** —— 文档明确列出：快速入门 → 存储说明和内存 → 常见工作流和最佳实践 → 设置 → 故障排除。这是一个自然的进阶路径。→ 建议融入章节：第 03 章（AI 编程工具入门），方式：作为"学完本章后下一步做什么"的推荐阅读顺序。
  - **知识点 3：Claude Code 的多界面统一性** —— "每个界面都连接到相同的底层 Claude Code 引擎，因此你的 CLAUDE.md 文件、设置和 MCP 服务器可在所有界面中工作。"→ 建议融入章节：第 03 章，方式：补充说明 CLI / VS Code / JetBrains 之间的配置互通性，降低读者对"选错工具"的焦虑。

- **与现有教程的对比**：教程第 04 章已经系统整理了 Claude Code 的核心概念和最佳实践，覆盖度很高。官方文档中更进阶的内容（如 Subagents、Agent Teams、MCP 深度配置）对零基础读者来说过于复杂，教程的取舍是合理的。

- **忽略原因**：高级 MCP 配置、CI/CD 集成、Slack/Chrome 扩展等企业级功能超出零基础范围；Agent SDK 开发属于进阶内容。

---

### 2. Kimi Code 官方文档（https://www.kimi.com/code/docs/）

- **核心内容摘要**：Kimi Code 是 Kimi 会员权益中专为开发者提供的智能编程服务，支持 CLI、VS Code 扩展和第三方工具接入。文档涵盖产品概览、CLI 快速开始、VS Code 集成、配置管理、定制化（MCP、Hooks、Skills）和平台对比等内容。

- **可吸收到教程的知识点**：
  - **知识点 1：Kimi Code 的安装命令** —— Windows: `Invoke-RestMethod https://code.kimi.com/install.ps1 | Invoke-Expression`，macOS/Linux: `curl -LsSf https://code.kimi.com/install.sh | bash`。安装后运行 `kimi` 即可启动。→ 建议融入章节：第 01 章或第 03 章，方式：作为 Kimi Code 的安装指引，与 Claude Code 并列呈现。
  - **知识点 2：OAuth 自动认证机制** —— "使用 Kimi Code CLI 或 VS Code 扩展的用户，可通过 OAuth 授权自动接入，无需手动管理 API Key。"这降低了入门门槛。→ 建议融入章节：第 03 章，方式：强调"无需手动配置 API Key"的便利性。
  - **知识点 3：Kimi Code 的额度机制说明** —— "每 7 天自动刷新""每 5 小时的滚动频率窗口""所有登录设备和 API Key 共享同一套配额"。→ 建议融入章节：第 03 章，方式：作为"使用注意事项"补充，帮助读者理解额度限制。
  - **知识点 4：模型 ID 的固定设计** —— "`kimi-for-coding` 是固定的模型 ID，后端会根据最新发布的模型自动更新其对应的 display name，你无需变更客户端配置即可享受模型升级。"→ 建议融入章节：第 03 章，方式：作为补充说明，解释为什么不需要手动切换模型版本。

- **与现有教程的对比**：教程目前以 Claude Code 为主，对 Kimi Code 的着墨较少。Kimi Code 的安装和认证流程更简单，适合作为替代方案介绍。

- **忽略原因**：第三方工具接入配置（JetBrains、Zed、Zsh）、Wire 协议、自定义插件等属于进阶内容；平台对比表格中的 Kimi 开放平台信息对零基础读者无直接价值。

---

### 3. CCQ（Claude Code Quickstart）GitHub 项目（https://github.com/MrNine-666/claude-code-quickstart）

- **核心内容摘要**：CCQ 是一个 Windows PowerShell 自动化安装器，用于一键搭建 Claude Code 开发环境。它通过双阶段架构（PowerShell 5.1 引导 + PowerShell 7 安装）自动化处理 Node.js、Git、Claude Code、第三方供应商配置、MCP Server、CCG 工作流等 13 个步骤的安装和配置。

- **可吸收到教程的知识点**：
  - **知识点 1："云端直接执行"的极简安装理念** —— CCQ 推荐用户直接复制粘贴 PowerShell 命令即可开始安装，无需下载文件或理解背后的依赖关系。→ 建议融入章节：第 01 章，方式：作为"最简安装路径"的参考思路，但需简化（CCQ 本身包含太多进阶组件）。
  - **知识点 2：配置持久化策略** —— CCQ 将配置分层管理（`~/.claude/settings.json`、`~/.claude/CLAUDE.md`、`~/.claude/providers/`），这种"配置即代码"的思路值得借鉴。→ 建议融入章节：第 04 章，方式：在介绍 CLAUDE.md 时，补充"配置文件分层"的概念。
  - **知识点 3：实时检测与增量更新** —— "每次运行都会检测当前组件状态，已安装的组件会自动跳过，避免重复安装。"→ 建议融入章节：第 01 章，方式：作为安装脚本的"幂等性"概念简单提及。

- **与现有教程的对比**：CCQ 的自动化程度很高，但覆盖的组件过多（包括 CCG Workflow、OpenSpec CLI、Codex CLI、Gemini CLI 等），对零基础读者会造成认知负担。教程目前的"分步手动安装"方式虽然步骤更多，但每一步都可理解、可控制，更适合初学者。

- **忽略原因**：CCQ 是一个面向中高级用户的"全家桶"安装器，包含大量零基础读者不需要的工具（MCP Server 配置、CCG 工作流、多模型切换等）。教程不应引导读者使用超出其理解范围的自动化工具。

---

### 4. VS Code 官方文档（https://code.visualstudio.com/Docs）

- **核心内容摘要**：VS Code 官方文档提供完整的入门路径，包括 Getting Started Tutorial、User Interface 指南、Extensions 安装、Tips and Tricks、Intro Videos 等。推荐路径：Basic Editing → IntelliSense → Code Navigation → Refactoring。

- **可吸收到教程的知识点**：
  - **知识点 1：官方推荐的"初学者优先"路径** —— 文档明确建议"beginners should prioritize core editor fundamentals before Copilot features"。→ 建议融入章节：第 01 章，方式：在介绍 VS Code 时，强调"先掌握编辑器基础，再使用 AI 功能"的学习顺序。
  - **知识点 2：VS Code 的 Tips and Tricks 页面** —— 包含大量提升效率的快捷键和操作技巧。→ 建议融入章节：第 01 章，方式：作为延伸阅读推荐，附官方链接。
  - **知识点 3：Intro Videos（介绍视频）** —— 官方提供视频形式的入门教程，适合视觉学习者。→ 建议融入章节：第 01 章，方式：作为"不同学习风格"的补充资源推荐。

- **与现有教程的对比**：教程第 01 章已经覆盖了 VS Code 的安装和基础配置。VS Code 官方文档的体系更庞大，但大部分内容（如远程开发、容器化、调试器深度配置）超出零基础范围。

- **忽略原因**：Copilot Quickstart、高级调试、多根工作区、语言特定配置等属于进阶内容；Web 版 VS Code 对本地开发场景价值有限。

---

### 5. Python 3.14.4 官方文档（https://docs.python.org/3/）

- **核心内容摘要**：Python 官方文档首页明确将 Tutorial 列为"首选起点"（"Start here: a tour of Python's syntax and features"），并配套提供 Beginner's Guide、Glossary、FAQs 和 Installing Python Modules 等资源。

- **可吸收到教程的知识点**：
  - **知识点 1：官方明确推荐的入门路径** —— Tutorial → Beginner's Guide → Glossary → FAQs。→ 建议融入章节：第 02 章或附录，方式：作为"学完本书后进一步学习 Python"的官方推荐路径。
  - **知识点 2：Glossary（术语表）的价值** —— 官方文档强调术语表是"专门解释 Python 技术术语"的查词工具。→ 建议融入章节：第 02 章，方式：鼓励读者遇到不懂的术语时查阅官方 Glossary。
  - **知识点 3：Python 3.14 作为稳定版推荐** —— 文档明确标注当前稳定版为推荐学习版本。→ 建议融入章节：第 01 章，方式：在安装 Python 时，建议读者选择最新稳定版而非旧版本。

- **与现有教程的对比**：教程第 02 章采用"最小必要语法"的教学策略，与官方 Tutorial 的系统性介绍形成互补。教程侧重"看懂代码"，官方 Tutorial 侧重"完整语法"。

- **忽略原因**：Library Reference、Python HOWTOs、Language Reference 等属于进阶查阅资料；C API 和扩展开发完全超出范围。

---

### 6. Vibe Coding 相关资源（vibecoding.cn/guide、github.com/PHY041/vibe-coding-cookbook）

- **核心内容摘要**：vibecoding.cn 提供了一套从编程概览到部署上线的 14 模块学习路径，主要围绕 Cursor 展开；vibe-coding-cookbook 是一套 Claude Code 的 Skills + Rules，强调"先想清楚（PRD），再动手"的流程化开发方法。

- **可吸收到教程的知识点**：
  - **知识点 1："慢即是快"的心法** —— vibe-coding-cookbook 提出："错误姿势：想到啥写啥 → 写完一堆 bug → 重构三遍；正确姿势：先想清楚 → 再动手 → 一遍过。"→ 建议融入章节：第 04 章或第 07 章，方式：作为"与 AI 协作时的人类责任"的补充观点。
  - **知识点 2：PRD 速记五问** —— "问题：用户痛点是什么？用户：谁会用？指标：怎么衡量成功？范围：做什么 / 不做什么？优先级：Must / Should / Could / Won't？"→ 建议融入章节：第 07 章（产品思维部分），方式：作为"定义问题"的实用工具介绍。

- **与现有教程的对比**：vibecoding.cn 的学习路径包含大量前端内容（HTML/CSS/JavaScript、React、Vue），与教程"Python + CLI 工具"的定位差异很大。vibe-coding-cookbook 的"大项目门禁"（强制 PRD + 架构 + ADR）对零基础读者过于沉重。

- **忽略原因**：vibecoding.cn 的 14 模块路径中，超过一半内容（前端开发、框架与工具、后端开发、数据库与 API、部署与上线）与教程的零基础 Python 定位不符；vibe-coding-cookbook 的 Skills/Rules 体系需要读者已熟练使用 Claude Code，不适合入门阶段。

---

### 7. Paul Graham 博客（https://paulgraham.com/）

- **核心内容摘要**：Paul Graham 是 Y Combinator 联合创始人，《黑客与画家》作者。他的博客文章涵盖编程哲学、创造者思维、工作方式、独立思考和长期主义等主题。本次调研重点阅读了《Hackers and Painters》《Maker's Schedule, Manager's Schedule》《Taste for Makers》《How to Do What You Love》《How to Think for Yourself》《Crazy New Ideas》《The Need to Read》等经典文章。

- **可吸收到教程的知识点**：
  - **知识点 1："黑客与画家"的创造者视角** —— "What hackers and painters have in common is that they're both makers... what hackers and painters are trying to do is make good things.""A programming language is for thinking of programs, not for expressing programs you've already thought of. It should be a pencil, not a pen."→ 建议融入章节：第 07 章（编程素养部分），方式：直接引用或改编，作为"编程作为创造性活动"的论述支撑。
  - **知识点 2："草图式编程"的方法论** —— "You should figure out programs as you're writing them, just as writers and painters and architects do.""The way to create something beautiful is often to make subtle tweaks to something that already exists, or to combine existing ideas in a slightly new way."→ 建议融入章节：第 03 章或第 04 章，方式：作为"迭代式开发"理念的理论来源，解释为什么"先跑起来，再慢慢改"是合理的。
  - **知识点 3："同理心"是区分好黑客与伟大黑客的关键** —— "Empathy is probably the single most important difference between a good hacker and a great one.""Programs should be written for people to read, and only incidentally for machines to execute."→ 建议融入章节：第 07 章（UX 部分），方式：直接引用 Abelson 和 Sussman 的名言，强化"代码是写给人看的"这一观点。
  - **知识点 4："做你热爱的事"的深度论述** —— "To do something well you have to like it.""The test of whether people love what they do is whether they'd do it even if they weren't paid for it.""Always produce."→ 建议融入章节：第 07 章（长期主义部分），方式：作为"如何保持在快速变化中的竞争力"的补充，强调内在驱动力的重要性。
  - **知识点 5："创造者的时间表"（Maker's Schedule）** —— "There are two types of schedule... The manager's schedule is for bosses... But there's another way of using time that's common among people who make things, like programmers and writers. They generally prefer to use time in units of half a day at least."→ 建议融入章节：第 07 章，方式：作为"优雅编程者的日常仪式"的补充，帮助读者理解为什么编程需要大块 uninterrupted time。
  - **知识点 6："品味"是可以培养的** —— "Good design is simple... Good design is timeless... Good design solves the right problem... Good design is redesign."→ 建议融入章节：第 02 章（代码审美部分）或第 07 章，方式：作为"代码审美"的理论框架，将"好设计"的原则映射到"好代码"。
  - **知识点 7："独立思考"的三要素** —— "Independent-mindedness has three components: fastidiousness about truth, resistance to being told what to think, and curiosity.""Your motto should not be 'do what you love' so much as 'do what you're curious about.'"→ 建议融入章节：第 07 章，方式：作为"持续学习"部分的补充，强调好奇心驱动的学习比功利性学习更持久。
  - **知识点 8："阅读的必要性"** —— "Reading about x doesn't just teach you about x; it also teaches you how to write.""There is a kind of thinking that can only be done by writing."→ 建议融入章节：第 07 章（知识管理部分），方式：作为"为什么写作是学习的最佳方式"的理论支撑。

- **与现有教程的对比**：教程第 07 章已经引用了《黑客与画家》的部分观点，但引用深度和广度可以进一步扩展。Paul Graham 的文章风格生动、比喻丰富，非常适合零基础读者理解抽象的编程哲学。

- **忽略原因**：关于创业（Y Combinator、融资、startup 模式）的文章与教程主题无关；部分技术评论（如对静态类型的批评）可能引发不必要的争议，不适合入门教程。

---

### 8. 人人都是产品经理（书籍及相关文章）

- **核心内容摘要**：《人人都是产品经理》由苏杰著，核心内容包括产品思维的定义、需求采集与分析方法论（用户访谈、调查问卷、可用性测试、数据分析）、需求分析 Y 模型（用户需求 → 用户目的 → 人性本质 → 产品功能）、KANO 模型、以及产品从 0 到 1 的完整流程。相关文章补充了"用户是需求的集合""用户的诉求不等于需求""共情设计"等观点。

- **可吸收到教程的知识点**：
  - **知识点 1："需求分析 Y 模型"** —— 用户需求 → 用户目的 →（人性本质 / 马斯洛需求）→ 产品功能。→ 建议融入章节：第 07 章（产品思维部分），方式：作为"如何定义问题"的可视化工具，帮助读者理解"用户说要一匹更快的马，其实想要的是更快到达目的地"。
  - **知识点 2："用户的诉求不等于需求"** —— "用户无法准确表达自己的诉求... 我们还要从海量的用户和用户需求里抽象分析、梳理整合出真正需要满足的需求。"→ 建议融入章节：第 07 章，方式：作为"产品思维"的核心原则，与教程中"用户买的不是钻头，是墙上的洞"形成呼应。
  - **知识点 3："用户是需求的集合"** —— 用户不是单一维度的标签，而是在不同场景下具有不同需求的复杂个体。→ 建议融入章节：第 07 章，方式：作为"认知用户"的补充，提醒读者不要简单地将"用户"抽象化。
  - **知识点 4："角色-场景-流程"需求判断法** —— 用角色（用户）、场景和流程来判断需求的真伪和满足程度。→ 建议融入章节：第 07 章，方式：作为"评估需求"的实用框架，帮助读者在定义问题时考虑"谁在什么情况下做什么"。
  - **知识点 5："共情"作为设计思维的核心** —— "共情就是站在用户的角度和位置上，客观的理解用户的内心感受。""有情感的产品植根于人，而非技术。"→ 建议融入章节：第 07 章（UX 部分），方式：作为"用户体验"的情感维度补充，强调技术实现之外的人文关怀。
  - **知识点 6：KANO 模型用于需求分类** —— 将需求分为基本型、期望型、兴奋型、无差异型和反向型，帮助确定开发优先级。→ 建议融入章节：第 07 章，方式：作为"需求优先级排序"的工具介绍，但需简化（零基础读者不需要掌握完整模型）。

- **与现有教程的对比**：教程第 07 章已经包含了产品思维、UX 和系统思维三个板块，但产品思维部分偏重于"是什么"和"为什么"，缺少"怎么做"的具体方法论。"人人都是产品经理"的需求分析方法可以填补这一空白。

- **忽略原因**：BRD/PRD 文档规范、项目管理流程、运营推广策略等属于专业产品经理的工作内容，对零基础编程读者来说过于细分；OKR、数据指标体系等内容会增加不必要的复杂度。

---

## 可立即吸收的 Top 10 知识点

### 1. Paul Graham "黑客与画家"的创造者视角
- **知识点概述**：黑客与画家的共同点是他们都是创造者（makers），编程语言应该是思考的铅笔而非表达的钢笔。
- **建议融入的章节和具体位置**：第 07 章"代码之外：AI 时代编程者的核心素养"，在"产品思维"小节之后新增"创造者视角"子节。
- **融入方式**：改编引用，将 Paul Graham 的论述与 AI 时代的"人类负责创造、AI 负责实现"分工结合。

### 2. Paul Graham "同理心"是区分好黑客与伟大黑客的关键
- **知识点概述**："Programs should be written for people to read, and only incidentally for machines to execute."
- **建议融入的章节和具体位置**：第 07 章"1.2 用户体验（UX）"小节。
- **融入方式**：直接引用 Abelson 和 Sussman 的这句名言（教程已引用，可强化其出处和上下文）。

### 3. "需求分析 Y 模型"（人人都是产品经理）
- **知识点概述**：用户需求 → 用户目的 → 人性本质 → 产品功能，帮助读者理解"用户说要 A，其实需要 B"。
- **建议融入的章节和具体位置**：第 07 章"1.1 产品思维"小节，在"用户买的不是钻头"之后。
- **融入方式**：改编为简化版 Y 模型图示，配合一个具体例子（如"用户说想要一个自动整理桌面的程序"）。

### 4. "用户的诉求不等于需求"（人人都是产品经理）
- **知识点概述**：用户无法准确表达自己的需求，产品经理的价值在于从海量诉求中抽象出真正的需求。
- **建议融入的章节和具体位置**：第 07 章"1.1 产品思维"小节。
- **融入方式**：作为"问题定义能力"的补充论述，与 Claude Code 的"Start with intent, not instructions"形成呼应。

### 5. Paul Graham "草图式编程"方法论
- **知识点概述**：编程应该像画画一样，在创作过程中逐步完善，而不是在纸上完全设计好再动手。
- **建议融入的章节和具体位置**：第 03 章"第一次对话"或第 04 章"先探索，再规划，最后编码"。
- **融入方式**：作为"迭代式开发"的理论支撑，解释为什么教程鼓励"先跑起来，再慢慢改"。

### 6. Kimi Code 的 OAuth 自动认证和额度机制
- **知识点概述**：Kimi Code 支持 OAuth 自动登录，无需手动管理 API Key；额度每 7 天刷新，有 5 小时滚动频率窗口。
- **建议融入的章节和具体位置**：第 03 章"AI 编程工具入门"，在介绍 Kimi Code 时补充。
- **融入方式**：直接补充到现有内容中，作为使用 Kimi Code 的实用信息。

### 7. Paul Graham "创造者的时间表"（Maker's Schedule）
- **知识点概述**：创造者需要至少半天的大块时间才能进入深度工作状态，会议对创造者来说是灾难。
- **建议融入的章节和具体位置**：第 07 章"4. 优雅编程者的日常仪式"。
- **融入方式**：作为"如何安排编程时间"的建议，帮助读者理解为什么"每天编程 2 小时"比"断断续续 4 小时"更有效。

### 8. "角色-场景-流程"需求判断法（人人都是产品经理）
- **知识点概述**：用角色（谁）、场景（在什么情况下）、流程（做什么）三个维度判断需求是否真实。
- **建议融入的章节和具体位置**：第 07 章"1.1 产品思维"小节。
- **融入方式**：简化为一个检查清单，作为"定义问题"时的自问工具。

### 9. Paul Graham "品味是可以培养的"
- **知识点概述**：好设计是简单的、永恒的、解决正确问题的、不断重设计的。品味不是天生的，而是通过实践和反思培养的。
- **建议融入的章节和具体位置**：第 02 章"编程语法和代码审美"或第 07 章。
- **融入方式**：将"好设计原则"映射到"好代码原则"，作为代码审美部分的升华。

### 10. Python 官方文档推荐的入门路径
- **知识点概述**：Tutorial → Beginner's Guide → Glossary → FAQs 是官方明确标注的推荐学习顺序。
- **建议融入的章节和具体位置**：第 02 章结尾或附录，作为"学完本章后去哪里继续学习"的推荐。
- **融入方式**：作为延伸阅读推荐，附官方链接和简要说明。

---

## 不建议吸收的内容及原因

| 内容 | 来源 | 不建议吸收的原因 |
|------|------|-----------------|
| CCQ 的完整自动化安装流程 | CCQ GitHub | 包含过多进阶组件（MCP Server、CCG Workflow、多模型切换），对零基础读者造成认知负担，且隐藏了重要的学习过程 |
| vibe coding 的 14 模块前端路径 | vibecoding.cn | 超过一半内容与教程的 Python + CLI 定位不符，前端框架学习对零基础读者是额外的技术栈负担 |
| vibe-coding-cookbook 的 Skills/Rules 体系 | GitHub | 需要读者已熟练使用 Claude Code，且"大项目门禁"（强制 PRD + 架构 + ADR）对初学者过于沉重 |
| Claude Code 的 MCP 深度配置 | Claude Code 官方文档 | MCP 是进阶扩展机制，零基础读者应先掌握基础对话和文件操作 |
| Claude Code 的 CI/CD 集成 | Claude Code 官方文档 | GitHub Actions / GitLab CI 属于 DevOps 范畴，超出零基础编程教程范围 |
| Paul Graham 的创业相关文章 | paulgraham.com | 关于 Y Combinator、融资、startup 模式的讨论与编程教程主题无关 |
| 人人都是产品经理中的 BRD/PRD 规范 | 书籍 | 商业需求文档和产品需求文档的撰写规范属于专业产品经理技能，对编程初学者过于细分 |
| 人人都是产品经理中的运营推广策略 | 书籍 | 产品运营、市场推广内容与编程核心能力无关 |
| VS Code 的远程开发/容器化配置 | VS Code 官方文档 | Remote Development、Dev Containers 等属于进阶开发环境配置 |
| Python 的 C API 和扩展开发 | Python 官方文档 | 完全超出零基础范围，属于高级 Python 主题 |

---

## 附录：调研工具使用记录

| 来源 | 工具 | 访问状态 |
|------|------|----------|
| Claude Code 官方文档 | mcp__playwright__browser_navigate + snapshot | 成功 |
| Kimi Code 官方文档 | mcp__playwright__browser_navigate + snapshot | 成功 |
| CCQ GitHub | mcp__deepwiki__read_wiki_structure / ask_question | 成功 |
| VS Code 官方文档 | WebFetch | 成功 |
| Python 官方文档 | WebFetch | 成功 |
| vibe coding 指南 | mcp__exa__web_fetch_exa | 成功（内容有限） |
| vibe-coding-cookbook | mcp__exa__web_fetch_exa | 成功 |
| Paul Graham 博客 | mcp__exa__web_fetch_exa | 成功 |
| 人人都是产品经理 | mcp__exa__web_search_exa | 成功 |
