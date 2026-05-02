# 附录 E：配套 GitHub 仓库设计

> 本附录为教程设计一个完整的配套 GitHub 仓库，包含示例代码、练习模板、自动化测试和文档。读者可以 Fork 或 Clone 这个仓库，边学边练。

---

## 仓库名称建议

| 方案 | 名称 | 说明 |
|------|------|------|
| 推荐 | `ai-era-elegant-coding` | 英文，简洁，国际化 |
| 备选 | `ai-coding-for-beginners` | 更直白，SEO 友好 |
| 备选 | `优雅编程-AI时代入门` | 中文，与教程书名呼应 |

**推荐选择**：`ai-era-elegant-coding`

---

## 目录结构

```
ai-era-elegant-coding/
├── .github/
│   └── workflows/
│       ├── test-examples.yml      # 自动测试示例代码
│       └── lint-check.yml         # 代码风格检查
├── chapter-01-setup/
│   ├── README.md                  # 本章说明
│   ├── check-installation.py      # 环境检查脚本
│   └── exercises/
│       └── env-checklist.md       # 环境搭建自检清单
├── chapter-02-python-basics/
│   ├── README.md
│   ├── examples/
│   │   ├── 01_variables.py
│   │   ├── 02_functions.py
│   │   ├── 03_conditions.py
│   │   ├── 04_loops.py
│   │   ├── 05_lists.py
│   │   └── 06_dictionaries.py
│   └── exercises/
│       └── exercise-template.md   # 02章练习模板
├── chapter-03-ai-tools/
│   ├── README.md
│   ├── examples/
│   │   ├── claude-code-intro.md   # Claude Code 入门示例对话
│   │   └── claude-md-template.md  # CLAUDE.md 模板
│   └── exercises/
│       └── first-ai-task.md       # 第一个 AI 协作任务
├── chapter-04-best-practices/
│   ├── README.md
│   ├── examples/
│   │   ├── good-prompt-example.md     # 好的 prompt 示例
│   │   └── bad-prompt-example.md      # 差的 prompt 示例（对比）
│   └── exercises/
│       └── prompt-refactoring.md      # Prompt 改写练习
├── chapter-05-projects/
│   ├── README.md
│   ├── project-01-organize-downloads/    # 实战案例一：自动整理下载文件夹
│   │   ├── organize_downloads.py         # 主脚本
│   │   └── README.md
│   ├── project-02-rename-photos/         # 实战案例二：批量重命名照片
│   │   ├── rename_photos.py              # 主脚本
│   │   └── README.md
│   └── exercises/
│       └── project-template.md    # 05章练习模板
├── chapter-06-agent-knowledge/
│   ├── README.md
│   ├── examples/
│   │   ├── http-request-example.py    # HTTP 请求示例
│   │   ├── json-handling.py           # JSON 处理示例
│   │   ├── path-examples.py           # 路径操作示例
│   │   └── dotenv-example.py          # 环境变量示例
│   └── exercises/
│       └── api-debug-challenge.md     # API 调试挑战
├── chapter-07-long-term/
│   ├── README.md
│   └── exercises/
│       └── personal-learning-plan.md  # 个人学习计划模板
├── shared/
│   ├── .gitignore-template          # 各项目通用的 .gitignore
│   ├── pre-commit-config.yaml       # 预提交钩子配置
│   └── common-prompts.md            # 常用 AI Prompt 模板合集
├── tests/
│   ├── __init__.py
│   ├── test_chapter02_examples.py   # 第02章示例代码测试
│   └── test_chapter06_examples.py   # 第06章示例代码测试
├── docs/
│   ├── CONTRIBUTING.md              # 贡献指南
│   ├── CODE_OF_CONDUCT.md           # 行为准则
│   └── learning-roadmap.png         # 学习路线图（配图）
├── LICENSE
├── README.md
└── requirements.txt                 # 仓库依赖（pytest、ruff 等）
```

---

## 每个目录/文件的用途说明

### 根级文件

| 文件/目录 | 用途 |
|-----------|------|
| `README.md` | 仓库主页，包含项目介绍、快速开始、目录导航 |
| `LICENSE` | 开源许可证（推荐 MIT，允许自由使用和学习） |
| `requirements.txt` | 运行测试和示例所需的 Python 依赖 |
| `.github/workflows/` | GitHub Actions 自动化配置 |

### 章节目录（chapter-XX-xxx）

每个章节目录遵循统一结构：

| 子目录/文件 | 用途 |
|-------------|------|
| `README.md` | 本章学习目标、前置要求、文件说明 |
| `examples/` | 与教程对应的可运行示例代码 |
| `exercises/` | 读者练习模板和挑战任务 |

### 共享资源（shared/）

| 文件 | 用途 |
|------|------|
| `.gitignore-template` | Python / Node.js 项目的通用 .gitignore 模板 |
| `pre-commit-config.yaml` | 代码提交前自动运行格式检查和测试 |
| `common-prompts.md` | 跨章节复用的 AI Prompt 模板（如调试模板、PR 模板） |

### 测试（tests/）

| 文件 | 用途 |
|------|------|
| `test_chapter02_examples.py` | 自动验证第02章所有示例代码能否正常运行 |
| `test_chapter06_examples.py` | 自动验证第06章所有示例代码能否正常运行 |

---

## README.md 内容大纲

```markdown
# AI 时代优雅编程 — 配套代码仓库

> 本仓库是《给零基础小白准备的 AI 时代优雅编程》教程的配套资源，包含示例代码、练习模板和自动化测试。

## 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/XiZu233/elegant-coding-book.git
cd elegant-coding-book
```

### 2. 创建虚拟环境

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 运行测试

```bash
pytest tests/ -v
```

## 目录导航

| 章节 | 内容 | 示例代码 | 练习 |
|------|------|----------|------|
| 01 搭建基础开发环境 | 环境检查脚本 | `chapter-01-setup/` | 环境自检清单 |
| 02 编程语法和代码审美 | Python 基础示例 | `chapter-02-python-basics/examples/` | 语法练习模板 |
| 03 AI编程工具入门 | AI 协作示例 | `chapter-03-ai-tools/examples/` | 第一个 AI 任务 |
| 04 概念介绍与最佳实践 | Prompt 示例 | `chapter-04-best-practices/examples/` | Prompt 改写 |
| 05 实战案例 | 两个完整项目 | `chapter-05-projects/` | 项目练习模板 |
| 06 AI编程时代知识基础 | 网络/路径/环境示例 | `chapter-06-agent-knowledge/examples/` | API 调试挑战 |
| 07 优雅编程的长期主义 | 学习计划模板 | `chapter-07-long-term/` | 个人学习规划 |

## 如何使用本仓库

### 学习者

1. 按章节顺序学习，每个 `examples/` 目录下的代码都可以直接运行
2. 完成 `exercises/` 中的练习，对照参考答案
3. 遇到问题时，使用 `shared/common-prompts.md` 中的模板向 AI 求助

### 贡献者

参见 [CONTRIBUTING.md](https://github.com/XiZu233/elegant-coding-book/blob/main/docs/CONTRIBUTING.md)。

## 自动化测试状态

![Tests](https://github.com/XiZu233/elegant-coding-book/actions/workflows/test-examples.yml/badge.svg)

## 许可证

MIT License - 详见 [LICENSE](https://github.com/XiZu233/elegant-coding-book/blob/main/LICENSE)
```

---

## 练习模板设计

### 模板 1：第02章 — 编程语法练习模板

**文件路径**：`chapter-02-python-basics/exercises/exercise-template.md`

```markdown
# 第02章练习：Python 语法基础

## 练习目标

完成以下 5 个小程序，巩固变量、函数、条件、循环和列表的基础知识。

---

## 练习 1：变量与类型（5分钟）

### 任务

创建一个程序，接收用户输入的姓名和年龄，输出一段自我介绍。

### 预期输出

```
请输入你的姓名：张三
请输入你的年龄：25
你好，张三！你今年 25 岁，5年后你将 30 岁。
```

### 提示

- 使用 `input()` 接收用户输入
- 注意 `input()` 返回的是字符串，年龄需要做类型转换
- 使用 f-string 格式化输出

### 验证方式

运行程序，输入不同的姓名和年龄，确认输出格式正确。

---

## 练习 2：函数封装（10分钟）

### 任务

把练习 1 的功能封装成一个函数 `introduce(name, age)`，并添加一个函数 `calculate_future_age(age, years)` 计算未来年龄。

### 要求

- `introduce` 函数接收两个参数，打印自我介绍
- `calculate_future_age` 函数接收当前年龄和年数，返回未来年龄
- 在主程序中调用这两个函数

### 验证方式

```python
# 应该输出：30
print(calculate_future_age(25, 5))

# 应该输出自我介绍
introduce("李四", 30)
```

---

## 练习 3：条件判断（10分钟）

### 任务

编写一个程序，根据分数输出等级：

- 90-100：优秀
- 80-89：良好
- 70-79：中等
- 60-69：及格
- 0-59：不及格
- 其他：输入无效

### 要求

- 使用 `if-elif-else` 结构
- 对无效输入（如负数、超过100）进行处理
- 封装成函数 `get_grade(score)`

### 验证方式

用以下测试用例验证：

| 输入 | 预期输出 |
|------|----------|
| 95 | 优秀 |
| 85 | 良好 |
| 75 | 中等 |
| 65 | 及格 |
| 55 | 不及格 |
| -5 | 输入无效 |
| 105 | 输入无效 |

---

## 练习 4：循环与列表（15分钟）

### 任务

编写一个程序，管理一个简单的待办事项列表：

1. 创建一个空列表 `todos`
2. 实现 `add_todo(task)` 函数，添加任务
3. 实现 `show_todos()` 函数，显示所有任务（带序号）
4. 实现 `complete_todo(index)` 函数，将指定任务标记为完成（在任务前加 [x]）

### 预期交互

```
>>> add_todo("学习Python")
已添加：学习Python

>>> add_todo("做练习题")
已添加：做练习题

>>> show_todos()
1. [ ] 学习Python
2. [ ] 做练习题

>>> complete_todo(1)
已完成任务：学习Python

>>> show_todos()
1. [x] 学习Python
2. [ ] 做练习题
```

### 验证方式

按照预期交互顺序执行，确认每一步输出正确。

---

## 练习 5：综合挑战（20分钟）

### 任务

编写一个"猜数字"游戏：

1. 程序随机生成一个 1-100 之间的数字
2. 用户每次输入一个猜测
3. 程序提示"太大了"或"太小了"
4. 记录猜测次数，猜中时输出"恭喜你，用了 X 次猜中！"
5. 提供"再玩一次"的选项

### 要求

- 使用 `random.randint()` 生成随机数
- 使用 `while` 循环直到猜中
- 处理无效输入（如输入非数字）
- 封装成可复用的函数

### 验证方式

1. 运行游戏，故意猜错几次，确认提示正确
2. 输入非数字（如"abc"），确认程序不崩溃
3. 选择"再玩一次"，确认游戏重新开始

---

## 提交检查清单

完成所有练习后，确认：

- [ ] 所有代码文件保存在 `chapter-02-python-basics/exercises/` 目录下
- [ ] 每个练习都有独立的 `.py` 文件
- [ ] 代码能运行，没有报错
- [ ] 代码有适当的注释说明
- [ ] 使用 `ruff check .` 检查代码风格，无警告

## 求助模板

遇到问题时，复制以下内容给 AI：

```text
我在完成第02章练习 [练习编号] 时遇到了问题。

任务要求：[简述任务]
我的代码：
```python
[粘贴代码]
```

遇到的问题：[报错信息或不符合预期的输出]

请帮我：
1. 指出问题所在
2. 给出修复建议
3. 解释为什么这样修改
```
```

---

### 模板 2：第05章 — 实战项目练习模板

**文件路径**：`chapter-05-projects/exercises/project-template.md`

```markdown
# 第05章练习：实战项目模板

## 项目选择

从以下两个项目中选择一个完成：

- [ ] **项目 A**：Python CLI 工具（推荐零基础）
- [ ] **项目 B**：Web 应用（推荐有前端基础）

---

## 项目 A：Python CLI 工具 — 个人记账本

### 项目概述

创建一个命令行记账工具，支持记录收入/支出、查看账单、按类别统计。

### 技术栈

- Python 3.11+
- `typer`（CLI 框架）
- 标准库 `json`（数据存储）

### 功能需求

#### 阶段 1：基础功能（必须完成）

- [ ] `add` 命令：添加一笔记录（金额、类别、备注、日期）
- [ ] `list` 命令：列出所有记录
- [ ] 数据持久化：保存为 JSON 文件

#### 阶段 2：增强功能（推荐完成）

- [ ] `summary` 命令：按月份/类别统计
- [ ] `delete` 命令：删除指定记录
- [ ] 数据验证：金额必须是数字，类别必须是预设选项

#### 阶段 3：进阶功能（可选）

- [ ] 导出 CSV 功能
- [ ] 简单的月度预算提醒

### 项目结构

```
expense-tracker/
├── src/
│   └── expense_tracker/
│       ├── __init__.py
│       ├── main.py          # CLI 入口
│       ├── storage.py       # 数据读写
│       └── models.py        # 数据模型
├── data/
│   └── records.json         # 数据文件（不提交到 git）
├── tests/
│   └── test_storage.py      # 存储层测试
├── pyproject.toml
├── .gitignore
└── README.md
```

### 对 AI 的描述 prompt

```text
我要从零创建一个 Python CLI 个人记账工具。需求如下：

功能：
1. 使用 typer 构建 CLI
2. 支持 add（添加记录）、list（查看记录）、summary（统计）命令
3. 数据用 JSON 文件存储在 data/records.json
4. 每条记录包含：金额（正数收入/负数支出）、类别、备注、日期

技术约束：
- 使用 Python 3.11+
- 使用 typer 和 pydantic
- 包含 pytest 测试
- 使用 ruff 代码检查

请先进入 Plan Mode 分析项目结构，然后分阶段实现。
```

### 验证方式

1. 运行 `pytest`，所有测试通过
2. 运行 `ruff check .`，无代码风格警告
3. 手动测试：
   - 添加 3 条记录（2 支出 + 1 收入）
   - 列出记录，确认显示正确
   - 查看统计，确认总额计算正确
4. 关闭程序后重新打开，确认数据仍然保留

---

## 项目 B：Web 应用 — 个人书签管理器

### 项目概述

创建一个简单的 Web 应用，用于管理收藏的网站链接，支持添加、分类、搜索。

### 技术栈

- Python + Flask（后端）
- HTML + CSS（前端，可用 AI 生成）
- SQLite（数据库）

### 功能需求

#### 阶段 1：基础功能（必须完成）

- [ ] 添加书签（URL、标题、分类、备注）
- [ ] 查看所有书签列表
- [ ] 按分类筛选书签

#### 阶段 2：增强功能（推荐完成）

- [ ] 搜索功能（按标题或备注搜索）
- [ ] 删除书签
- [ ] 简单的界面美化

#### 阶段 3：进阶功能（可选）

- [ ] 导入/导出书签（HTML 格式，兼容浏览器导入）
- [ ] 标签系统（一个书签可有多个标签）

### 项目结构

```
bookmark-manager/
├── app/
│   ├── __init__.py
│   ├── routes.py            # 路由
│   ├── models.py            # 数据库模型
│   └── templates/           # HTML 模板
│       ├── base.html
│       ├── index.html
│       └── add.html
├── static/
│   └── style.css            # 样式
├── instance/
│   └── bookmarks.db         # SQLite 数据库（不提交到 git）
├── tests/
│   └── test_routes.py
├── requirements.txt
├── .gitignore
└── README.md
```

### 对 AI 的描述 prompt

```text
我要创建一个个人书签管理 Web 应用。需求如下：

功能：
1. 使用 Flask 框架
2. 支持添加、查看、搜索、删除书签
3. 书签字段：URL、标题、分类、备注
4. 使用 SQLite 存储数据
5. 简单的 HTML 前端，支持按分类筛选

技术约束：
- Python 3.11+
- Flask + SQLAlchemy
- 包含 pytest 测试
- 提供 requirements.txt

请先进入 Plan Mode 分析项目结构，然后分阶段实现。
```

### 验证方式

1. 运行 `pytest`，所有测试通过
2. 启动应用：`flask run`
3. 浏览器访问 `http://localhost:5000`
4. 手动测试：
   - 添加 3 个书签（不同分类）
   - 确认列表页显示正确
   - 测试分类筛选功能
   - 测试搜索功能
   - 删除一个书签，确认列表更新

---

## 通用提交要求

无论选择哪个项目，完成后必须：

- [ ] 项目能在新机器上通过 README 中的步骤一键运行
- [ ] 包含 `.gitignore`，不提交虚拟环境和数据文件
- [ ] 包含 `README.md`，说明安装步骤和使用方法
- [ ] 包含至少 3 个测试用例
- [ ] 代码通过 `ruff check .` 或 `eslint` 检查
- [ ] 提交到 Git，至少 3 个有意义的 commit

## 求助模板

```text
我在完成第05章实战项目 [项目A/项目B] 时遇到了问题。

当前阶段：[如：Plan Mode 规划 / 实现阶段 / 测试阶段]
遇到的问题：[具体描述]

相关代码/报错：
```
[粘贴代码或报错]
```

项目结构：
```
[粘贴当前目录树]
```

请帮我：
1. 分析问题原因
2. 给出具体修复步骤
3. 告诉我如何验证修复成功
```
```

---

## GitHub Actions 建议

### Workflow 1：测试示例代码（test-examples.yml）

```yaml
name: Test Examples

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test-python:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.11', '3.12']

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      run: pytest tests/ -v

    - name: Test Chapter 02 examples
      run: |
        cd chapter-02-python-basics/examples
        for f in *.py; do echo "Testing $f"; python "$f"; done

    - name: Test Chapter 06 examples
      run: |
        cd chapter-06-agent-knowledge/examples
        for f in *.py; do echo "Testing $f"; python "$f"; done
```

### Workflow 2：代码风格检查（lint-check.yml）

```yaml
name: Lint Check

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  lint:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.12'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install ruff

    - name: Run ruff check
      run: ruff check .

    - name: Run ruff format check
      run: ruff format --check .
```

### Workflow 3：项目构建验证（project-build.yml）

```yaml
name: Project Build Check

on:
  push:
    paths:
      - 'chapter-05-projects/**'
  pull_request:
    paths:
      - 'chapter-05-projects/**'

jobs:
  build-weather-cli:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-python@v5
      with:
        python-version: '3.12'
    - name: Install weather-cli
      run: |
        cd chapter-05-projects/project-01-weather-cli
        pip install -e .
    - name: Test CLI
      run: |
        cd chapter-05-projects/project-01-weather-cli
        python -m weather_cli --help
```

---

## 预提交钩子配置（pre-commit）

`.pre-commit-config.yaml`：

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
```

---

## 贡献指南要点（CONTRIBUTING.md）

```markdown
# 贡献指南

## 如何贡献

1. Fork 本仓库
2. 创建你的功能分支：`git checkout -b feature/xxx`
3. 提交更改：`git commit -m '添加 xxx 示例'`
4. 推送到分支：`git push origin feature/xxx`
5. 创建 Pull Request

## 代码规范

- Python 代码遵循 PEP 8，使用 ruff 检查
- 示例代码必须包含注释，解释关键步骤
- 每个示例文件顶部包含简短说明
- 新增示例需同步添加测试

## 报告问题

使用 GitHub Issues，包含：
- 问题描述
- 复现步骤
- 预期行为 vs 实际行为
- 环境信息（OS、Python 版本）
```

---

> 本仓库设计的核心理念是"可运行、可验证、可扩展"。每个示例代码都经过自动化测试确保能跑通，每个练习模板都提供清晰的验证方式，让读者在动手实践中建立信心。
