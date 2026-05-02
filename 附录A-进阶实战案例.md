根据 Claude Code 官方文档的最佳实践，我为你设计了两份**从零开始的实战案例**。这两个案例分别覆盖 **Python 后端/CLI 工具** 和 **现代前端 Web 应用**，完整展示 Claude Code + VS Code 的实战工作流。

---

# 实战案例一：Python 天气查询 CLI 工具

## 项目概述
从零搭建一个功能完整的命令行天气工具，支持多城市查询、本地缓存、配置文件管理，并包含完整的测试套件。

## 技术栈
- Python 3.11+
- `httpx`（异步 HTTP）
- `pydantic`（配置验证）
- `typer`（CLI 框架）
- `pytest` + `pytest-asyncio`（测试）
- `ruff`（代码质量）

---

### Step 1：环境准备与项目初始化

```bash
# 创建项目目录
mkdir weather-cli && cd weather-cli

# 使用 uv 初始化（推荐）或 venv
uv init --python 3.11
# 或：python -m venv .venv && source .venv/bin/activate

# 启动 VS Code 并打开 Claude Code
code .
# 在 VS Code 中：Cmd+Shift+P → "Claude Code: Open in New Tab"
```

**对 Claude 说：**
```text
我要从零创建一个 Python CLI 天气查询工具。先进入 Plan Mode，帮我分析项目结构并制定实现计划。
要求：
1. 使用 typer 构建 CLI
2. 使用 httpx 异步调用 Open-Meteo 免费 API（无需 API Key）
3. 支持配置文件管理（~/.weather-cli/config.json）
4. 支持本地缓存（TTL 5分钟）
5. 包含完整的 pytest 测试
6. 使用 ruff 进行代码检查
```

---

### Step 2：Plan Mode 规划（按 Shift+Tab 两次进入 Plan Mode）

Claude 会分析并输出类似计划：

```markdown
## 项目结构
weather-cli/
├── src/
│   └── weather_cli/
│       ├── __init__.py
│       ├── main.py          # CLI 入口
│       ├── api.py           # Open-Meteo API 客户端
│       ├── config.py        # 配置管理
│       ├── cache.py         # 本地缓存
│       └── models.py        # Pydantic 数据模型
├── tests/
│   ├── test_api.py
│   ├── test_cache.py
│   └── test_config.py
├── pyproject.toml
└── README.md

## 实现步骤
1. 配置 pyproject.toml 依赖
2. 实现数据模型（CurrentWeather, CityConfig）
3. 实现配置管理（读取/写入 ~/.weather-cli/config.json）
4. 实现缓存层（JSON 文件缓存 + TTL）
5. 实现 API 客户端（Open-Meteo 地理编码 + 天气接口）
6. 实现 CLI 命令（search, current, config）
7. 编写测试（mock API + 临时目录测试配置）
8. 配置 ruff 并运行检查
```

**操作：** 按 `Ctrl+G` 在编辑器中审阅计划，确认后切换回 Normal Mode（Shift+Tab）。

---

### Step 3：让 Claude 执行实现

```text
按照你的计划开始实现。先创建 pyproject.toml 和项目结构，然后逐个实现模块。
每完成一个模块，运行对应的测试验证。
```

Claude 会自动：
1. 创建 `pyproject.toml` 并安装依赖
2. 创建目录结构
3. 实现 `models.py`：
```python
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CurrentWeather(BaseModel):
    temperature: float
    humidity: int
    wind_speed: float
    weather_code: int
    timestamp: datetime

class CityConfig(BaseModel):
    name: str
    latitude: float
    longitude: float
    alias: Optional[str] = None
```
4. 实现 `config.py`（带文件锁和验证）
5. 实现 `cache.py`（TTL 检查）
6. 实现 `api.py`（Open-Meteo 接口）
7. 实现 `main.py`（Typer CLI）

**验证指令：**
```text
运行 pytest 确保所有测试通过，然后运行 ruff check . 确保代码风格正确。
```

---

### Step 4：功能验证与迭代

```text
现在测试实际功能：
1. 查询北京天气：python -m weather_cli current "Beijing"
2. 添加城市别名：python -m weather_cli config add --alias bj --lat 39.9 --lon 116.4
3. 再次查询验证缓存：python -m weather_cli current bj
4. 检查缓存文件是否正确生成

如果遇到问题，修复并重新运行测试。
```

---

### Step 5：收尾（CLAUDE.md + Git）

```text
帮我生成 README.md，包含安装说明、使用示例和 API 来源。
然后初始化 git 仓库，创建 .gitignore，并做第一次提交。
```

**创建 `CLAUDE.md` 供后续维护：**
```markdown
# Weather CLI 项目约定
- 使用 typer 构建所有 CLI 命令
- API 调用必须使用 httpx.AsyncClient
- 缓存 TTL 默认为 300 秒，可在配置中修改
- 测试使用 pytest-asyncio，mock 外部 API
- 提交前运行：pytest && ruff check .
```

---

# 实战案例二：Next.js 个人仪表盘（Full-Stack）

## 项目概述
从零搭建一个现代化的个人仪表盘 Web 应用，包含天气卡片、待办事项、笔记速记功能，使用 App Router 和 Server Actions。

## 技术栈
- Next.js 15 (App Router)
- TypeScript
- Tailwind CSS + shadcn/ui
- SQLite + Prisma（本地数据库）
- next-auth（GitHub 登录）

---

### Step 1：项目初始化

```bash
# 创建 Next.js 项目（选择 TypeScript, Tailwind, App Router）
npx create-next-app@latest dashboard --typescript --tailwind --app --no-src-dir
cd dashboard

# 初始化 shadcn/ui
npx shadcn@latest init

# 安装额外依赖
npm install @prisma/client next-auth bcryptjs
npm install -D prisma @types/bcryptjs

# VS Code 打开
code .
```

**对 Claude 说：**
```text
我要从零搭建一个 Next.js 个人仪表盘应用。进入 Plan Mode，帮我制定完整的实现计划。
功能需求：
1. 首页仪表盘布局（侧边栏 + 主内容区）
2. 天气卡片组件（调用 Open-Meteo API，Server Component）
3. 待办事项（Prisma + SQLite，Server Actions）
4. 笔记速记（CRUD，本地存储优先）
5. 暗色模式支持（next-themes）
6. 响应式设计

技术约束：
- 使用 App Router
- 使用 Server Actions 处理数据变更
- 使用 shadcn/ui 组件
- 数据库用 SQLite + Prisma
```

---

### Step 2：Plan Mode 架构规划

Claude 会输出详细计划，包括：

```markdown
## 数据库 Schema (Prisma)
- Todo: id, title, completed, createdAt, updatedAt
- Note: id, title, content, createdAt, updatedAt

## 组件结构
app/
├── layout.tsx          # 根布局（ThemeProvider）
├── page.tsx            # 仪表盘首页
├── globals.css
├── api/                # Next Auth 路由
├── actions/            # Server Actions
│   ├── todo.ts
│   └── note.ts
components/
├── ui/                 # shadcn 组件
├── weather-card.tsx    # 天气卡片（Server）
├── todo-list.tsx       # 待办列表（Client）
├── note-editor.tsx     # 笔记编辑器（Client）
└── sidebar.tsx         # 侧边栏
lib/
├── prisma.ts           # Prisma 客户端单例
└── utils.ts
```

**操作：** 审阅计划，确认数据流和组件边界，然后切换 Normal Mode。

---

### Step 3：数据库与核心架构

```text
先配置 Prisma 和数据库：
1. 创建 prisma/schema.prisma
2. 初始化迁移
3. 创建 lib/prisma.ts 单例
4. 创建 Server Actions（todo.ts, note.ts）

然后安装需要的 shadcn 组件：card, button, input, checkbox, textarea, badge
```

Claude 会执行：
```bash
npx shadcn add card button input checkbox textarea badge
npx prisma init
npx prisma migrate dev --name init
```

---

### Step 4：实现页面与组件

```text
按以下顺序实现：
1. 根布局（添加 ThemeProvider 和 Sidebar）
2. WeatherCard 组件（Server Component，fetch Open-Meteo）
3. TodoList 组件（Client，useOptimistic + Server Actions）
4. NoteEditor 组件（Client，自动保存到 localStorage）
5. 主页面（组合所有组件）

要求：
- WeatherCard 使用 suspense 和 loading 骨架
- TodoList 支持添加、完成、删除，有乐观更新
- NoteEditor 支持 Markdown 预览（简单实现）
- 所有交互组件使用 shadcn/ui
```

**关键提示（利用 Claude Code 优势）：**
```text
实现 WeatherCard 时，使用 Open-Meteo API：
- 地理编码：https://geocoding-api.open-meteo.com/v1/search?name=Beijing&count=1
- 天气：https://api.open-meteo.com/v1/forecast?latitude=...&longitude=...&current=temperature_2m,relative_humidity_2m,weather_code

weather_code 映射到图标和描述（晴天、多云、雨天等）。
```

---

### Step 5：视觉验证与迭代

**利用 Claude Code + Chrome 扩展（如有）或截图反馈：**

```text
现在运行开发服务器：npm run dev
然后帮我检查以下问题：
1. 侧边栏在移动端是否可折叠？
2. 暗色模式切换是否正常工作？
3. 待办事项添加后是否有乐观更新动画？
4. 天气卡片加载状态是否美观？

[截图粘贴到对话中]
根据当前 UI，调整配色和间距，让整体更协调。
```

Claude 可以：
- 读取截图并对比设计
- 修改 Tailwind 类名
- 调整组件布局

---

### Step 6：构建与部署准备

```text
1. 配置 next.config.js 用于静态导出（或保持 SSR）
2. 运行 npm run build 检查是否有错误
3. 修复所有 TypeScript 和 ESLint 错误
4. 创建 .env.example 文件
5. 更新 README.md 包含本地开发步骤

如果构建成功，帮我准备部署到 Vercel 的配置。
```

---

### Step 7：项目配置归档

**创建 `.claude/CLAUDE.md`：**
```markdown
# Dashboard 项目约定
- 使用 Server Components 作为默认，仅在需要交互时用 "use client"
- 数据变更必须使用 Server Actions，不使用 API Routes
- 表单使用 useActionState 处理提交状态
- 颜色使用 Tailwind 的 slate/zinc 色系，保持中性
- shadcn 组件安装命令：npx shadcn add <component>
- 数据库变更流程：修改 schema → npx prisma migrate dev → npx prisma generate
```

---

# 两个案例的对比总结

| 维度 | Python CLI 工具 | Next.js 仪表盘 |
|------|----------------|----------------|
| **项目类型** | 后端/CLI | 全栈 Web |
| **Claude Code 模式** | Plan → 实现 → 测试 | Plan → 架构 → UI 迭代 |
| **验证方式** | pytest + ruff + 实际运行 | npm run build + 视觉检查 |
| **上下文管理** | 单文件逐步验证 | 多组件并行开发 |
| **扩展点** | Skills（部署工作流） | Subagents（UI 审查） |
| **最佳实践体现** | 先测试后实现 | Server/Client 边界划分 |

---

# 通用提示词模板（可直接复用）

**启动 Plan Mode：**
```text
进入 Plan Mode。我要从零创建 [项目类型]，需求是 [简述]。
技术栈：[列表]
约束：[特殊要求]
请分析并给出详细的项目结构和实现计划。
```

**实现阶段：**
```text
按照计划开始实现。先 [第一步]，完成后运行 [验证命令] 确认无误再继续下一步。
```

**调试阶段：**
```text
[粘贴错误日志]
这个错误出现在 [文件/操作] 时。修复它并验证：
1. [验证条件1]
2. [验证条件2]
```

**收尾阶段：**
```text
生成 README.md 和 CLAUDE.md，初始化 git 并提交。
确保项目可以在新机器上通过 [安装命令] 一键运行。
```

这两个案例涵盖了 AI 编程中最典型的两种场景：**命令行工具开发**（重逻辑、重测试）和 **现代 Web 开发**（重架构、重 UI）。你可以根据自己的兴趣选择其中一个开始实践。
