# 代码可运行性检查报告

> 检查范围：src/chapter-00.md ~ src/chapter-07.md、src/appendix-a.md ~ src/appendix-g.md、code/ 目录下所有 Python 代码
> 检查时间：2026-05-02
> 检查工具：python -m py_compile、pytest、人工审查

---

## 一、语法检查结果

### 1.1 code/ 目录下的项目代码

| 位置 | 代码摘要 | 状态 | 说明 |
|------|---------|------|------|
| code/chapter-02/examples/01_variables.py | 变量与基础类型演示 | 通过 | py_compile 通过，运行正常 |
| code/chapter-02/examples/02_functions.py | 函数定义与调用演示 | 通过 | py_compile 通过，运行正常 |
| code/chapter-02/examples/03_conditions.py | 条件判断演示 | 通过 | py_compile 通过，运行正常 |
| code/chapter-02/examples/04_loops.py | 循环演示 | 通过 | py_compile 通过，运行正常 |
| code/chapter-02/examples/05_lists.py | 列表操作演示 | 通过 | py_compile 通过，运行正常 |
| code/chapter-02/examples/06_dictionaries.py | 字典操作演示 | 通过 | py_compile 通过，运行正常 |
| code/chapter-05/project-01/organize_downloads.py | 自动整理下载文件夹 | 通过 | py_compile 通过，测试通过 |
| code/chapter-05/project-02/rename_photos.py | 批量重命名照片 | 通过 | py_compile 通过，测试通过 |
| code/tests/test_chapter02_examples.py | 第02章测试 | 通过 | py_compile 通过，6/6 测试通过 |
| code/tests/test_chapter05_projects.py | 第05章测试 | 通过 | py_compile 通过，5/5 测试通过 |

### 1.2 Markdown 文件中的 python 代码块

| 位置 | 代码摘要 | 状态 | 说明 |
|------|---------|------|------|
| src/chapter-01.md:119 | `print("Hello, World!")` | 通过 | 单行语句，语法正确 |
| src/chapter-02.md:19 | 变量声明（name/age/height/is_student） | 通过 | 完整可运行片段 |
| src/chapter-02.md:56 | 字符串操作 | 通过 | 完整可运行片段 |
| src/chapter-02.md:71 | 数字运算 | 通过 | 完整可运行片段 |
| src/chapter-02.md:88 | 列表操作 | 通过 | 完整可运行片段 |
| src/chapter-02.md:105 | 字典操作 | 通过 | 完整可运行片段 |
| src/chapter-02.md:131 | `def greet(name)` 函数 | 通过 | 完整可运行片段 |
| src/chapter-02.md:147 | `def calculate_area(width, height)` | 通过 | 完整可运行片段 |
| src/chapter-02.md:173 | 条件判断 if/elif/else | 通过 | 完整可运行片段 |
| src/chapter-02.md:190 | `os.path.exists()` 判断 | 通过 | 完整可运行片段 |
| src/chapter-02.md:214 | 逻辑运算符 and/or/not | 通过 | 完整可运行片段 |
| src/chapter-02.md:233 | for 循环遍历列表 | 通过 | 完整可运行片段 |
| src/chapter-02.md:247 | range() 生成数字序列 | 通过 | 完整可运行片段 |
| src/chapter-02.md:260 | while 循环 | 通过 | 完整可运行片段 |
| src/chapter-02.md:272 | 猜数字游戏 | 通过 | 完整可运行片段 |
| src/chapter-02.md:306 | `def check_age(age)` 缩进示例 | 通过 | 完整可运行片段 |
| src/chapter-02.md:332 | 命名规范示例 | 通过 | 完整可运行片段 |
| src/chapter-02.md:360 | `calculate_price()` 函数 | 通过 | 完整可运行片段 |
| src/chapter-02.md:383 | main() 函数 + 文件读写 | 通过 | 完整可运行片段 |
| src/chapter-02.md:416 | reader.py / main.py 模块化示例 | 片段（无法独立编译） | 跨文件引用，需合并才能运行 |
| src/chapter-02.md:459 | `calculate(a, b)` print 调试 | 通过 | 完整可运行片段 |
| src/chapter-03.md:103 | `print("Hello, World!")` | 通过 | 单行语句，语法正确 |
| src/chapter-03.md:136 | 计算器函数（add/subtract/multiply/divide） | 通过 | 完整可运行片段 |
| src/chapter-03.md:232 | `def power(a, b)` | 通过 | 片段，依赖前文函数 |
| src/chapter-04.md:98 | Pydantic 模型（CurrentWeather/CityConfig） | 片段（无法独立编译） | 依赖 pydantic 第三方库 |
| src/chapter-05.md:51 | organize_downloads() 第一版 | 通过 | 完整可运行 |
| src/chapter-05.md:166 | organize_downloads() 第二版（dry_run） | 通过 | 完整可运行 |
| src/chapter-05.md:310 | rename_photos() 完整版 | 通过 | 完整可运行 |
| src/chapter-05.md:460 | rename_photos() 带前缀版 | 通过 | 片段，展示关键修改部分 |
| src/chapter-06.md:112 | `os.environ` 访问示例 | 片段（无法独立编译） | 单行引用，无完整上下文 |
| src/chapter-07.md:373 | 测试驱动开发文本示例 | 非代码 | text 代码块，非 Python |
| src/appendix-a.md:98 | Pydantic 模型示例 | 片段（无法独立编译） | 依赖 pydantic 第三方库 |
| src/appendix-a.md:177 | `uv init --python 3.11` 等 | 非 Python | bash 代码块 |
| src/appendix-a.md:259 | `npx shadcn add ...` 等 | 非 Python | bash 代码块 |
| src/appendix-a.md:297 | WeatherCard Open-Meteo API 调用 | 片段（无法独立编译） | 文本描述，非可运行代码 |
| src/appendix-b.md:31 | IndentationError 示例 | 片段（无法独立编译） | 故意展示错误，非可运行 |
| src/appendix-b.md:76 | ModuleNotFoundError 示例 | 片段（无法独立编译） | 故意展示错误，非可运行 |
| src/appendix-b.md:119 | FileNotFoundError 示例 | 片段（无法独立编译） | 故意展示错误，非可运行 |
| src/appendix-b.md:153 | SyntaxError 示例 | 片段（无法独立编译） | 故意展示错误，非可运行 |
| src/appendix-b.md:212 | PermissionError 示例 | 片段（无法独立编译） | 故意展示错误，非可运行 |
| src/appendix-b.md:248 | NameError 示例 | 片段（无法独立编译） | 故意展示错误，非可运行 |
| src/appendix-b.md:286 | TypeError 示例 | 片段（无法独立编译） | 故意展示错误，非可运行 |
| src/appendix-e.md:36 | 项目目录树（文本） | 非代码 | text 代码块 |
| src/appendix-e.md:191 | requirements.txt 示例 | 非 Python | text 代码块 |
| src/appendix-e.md:201 | package.json 示例 | 非 Python | json 代码块 |
| src/appendix-e.md:268 | `calculate_future_age()` 练习 | 通过 | 完整可运行片段 |
| src/appendix-e.md:295 | `get_grade(score)` 练习 | 通过 | 完整可运行片段 |
| src/appendix-e.md:319 | 待办事项列表练习 | 通过 | 完整可运行片段 |
| src/appendix-e.md:354 | 猜数字游戏练习 | 通过 | 完整可运行片段 |
| src/appendix-e.md:439 | expense-tracker 项目结构 | 非代码 | text 代码块 |
| src/appendix-e.md:480 | 记账工具 prompt | 非代码 | text 代码块 |
| src/appendix-e.md:543 | bookmark-manager 项目结构 | 非代码 | text 代码块 |
| src/appendix-e.md:566 | 书签管理器 prompt | 非代码 | text 代码块 |
| src/appendix-e.md:641 | GitHub Actions workflow | 非 Python | yaml 代码块 |
| src/appendix-e.md:686 | lint-check.yml | 非 Python | yaml 代码块 |
| src/appendix-e.md:721 | project-build.yml | 非 Python | yaml 代码块 |
| src/appendix-e.md:756 | pre-commit-config.yaml | 非 Python | yaml 代码块 |
| src/appendix-e.md:779 | CONTRIBUTING.md 模板 | 非代码 | markdown 代码块 |
| src/appendix-f.md:190 | Python 依赖版本示例 | 非 Python | text 代码块 |
| src/appendix-f.md:201 | Node.js package.json 示例 | 非 Python | json 代码块 |
| src/appendix-g.md | 一致性检查报告 | 无代码块 | 纯文本报告 |

---

## 二、命名规范问题

| 位置 | 变量/函数名 | 问题 | 建议 |
|------|------------|------|------|
| src/chapter-02.md:339 | `x = 3` | 使用了无意义单字母 | 作为"不好的命名"示例出现，属于教学目的，合规 |
| src/chapter-02.md:338 | `userName` | 使用了驼峰命名 | 作为"不好的命名"示例出现，教学目的，合规 |
| src/chapter-02.md:337 | `UserName` | 使用了大驼峰 | 作为"不好的命名"示例出现，教学目的，合规 |
| src/appendix-e.md:439 | `expense-tracker/` | 目录名含连字符 | 项目目录命名，非 Python 变量，合规 |
| code/chapter-02/examples/01_variables.py | 全部变量 | 全部使用 snake_case | 符合规范 |
| code/chapter-02/examples/02_functions.py | 全部函数 | 全部使用 snake_case | 符合规范 |
| code/chapter-05/project-01/organize_downloads.py | 全部变量/函数 | 全部使用 snake_case | 符合规范 |
| code/chapter-05/project-02/rename_photos.py | 全部变量/函数 | 全部使用 snake_case | 符合规范 |

**结论**：全书未发现实际命名违规。第02章中故意展示了不好的命名示例（`x`、`userName`、`UserName`），这是教学需要，不属于问题。

---

## 三、路径示例问题

| 位置 | 路径示例 | 问题 | 建议 |
|------|---------|------|------|
| src/chapter-01.md:101 | `my-first-code` | 文件夹名，无路径分隔符问题 | 合规 |
| src/chapter-01.md:210 | `irm https://claude.ai/install.ps1 \| iex` | Windows PowerShell 安装命令 | 合规，已区分 Windows/macOS |
| src/chapter-01.md:216 | `curl -fsSL https://claude.ai/install.sh \| bash` | macOS/Linux 安装命令 | 合规，已区分 |
| src/chapter-01.md:236 | `[Environment]::SetEnvironmentVariable(...)` | Windows PowerShell 环境变量配置 | 合规，已区分 |
| src/chapter-01.md:242 | `echo 'export ...' >> ~/.zshrc` | macOS 环境变量配置 | 合规，已区分 |
| src/chapter-01.md:248 | `echo 'export ...' >> ~/.bashrc` | Linux 环境变量配置 | 合规，已区分 |
| src/chapter-03.md:60 | `cd ~/projects` | macOS/Linux 路径示例 | 合规 |
| src/chapter-04.md:52 | `修改 src/auth.js` | 相对路径示例，未区分系统 | 作为通用示例，不涉及具体系统路径，合规 |
| src/chapter-05.md:34 | `C:\Users\我的用户名\Downloads` | Windows 路径示例 | 合规，已标注 Windows |
| src/chapter-05.md:118 | `Path.home() / "Downloads"` | 使用 pathlib，跨平台 | 合规 |
| src/chapter-05.md:398 | `Path(r"C:\Users\你的用户名\Pictures\相机照片")` | Windows 路径示例 | 合规，已标注 Windows |
| src/chapter-05.md:414 | `cd "C:\Users\你的用户名\Desktop\测试照片"` | Windows 路径示例 | 合规，已标注 Windows |
| src/chapter-06.md:84 | `C:\` 盘符、`/` 根目录 | 专业版路径解释，已区分 Windows/Unix | 合规 |
| src/chapter-06.md:98 | `pwd`、`ls` | Unix 命令，Windows 对应 `cd`、`dir` | 合规，人话版已提及 |
| src/appendix-b.md:143 | `python -c "import os; print(os.getcwd())"` | 跨平台 Python 命令 | 合规 |
| src/appendix-b.md:410 | `netstat -ano \| findstr :3000` | Windows 命令 | 合规，已区分 |
| src/appendix-b.md:411 | `lsof -i :3000` | macOS/Linux 命令 | 合规，已区分 |
| src/appendix-e.md:149 | `git clone ... && cd ...` | 通用命令 | 合规 |
| src/appendix-e.md:159 | `.venv\Scripts\activate` | Windows 虚拟环境激活 | 合规，已区分 |
| src/appendix-e.md:162 | `source .venv/bin/activate` | macOS/Linux 虚拟环境激活 | 合规，已区分 |

**结论**：全书路径示例区分 Windows 和 macOS/Linux 的情况良好。第05章实战案例使用 `pathlib.Path` 处理路径，自动适配不同系统，符合最佳实践。

---

## 四、标准库合规性问题

### 4.1 第05章实战案例（必须仅使用标准库）

| 位置 | import 语句 | 问题 | 建议 |
|------|------------|------|------|
| src/chapter-05.md:51 | `import os`, `import shutil`, `from pathlib import Path` | 均为标准库 | 合规 |
| src/chapter-05.md:166 | `import os`, `import shutil`, `from pathlib import Path` | 均为标准库 | 合规 |
| src/chapter-05.md:310 | `import os`, `import time`, `from pathlib import Path`, `from collections import defaultdict` | 均为标准库 | 合规 |
| code/chapter-05/project-01/organize_downloads.py | `import shutil`, `from pathlib import Path` | 均为标准库 | 合规 |
| code/chapter-05/project-02/rename_photos.py | `import os`, `import time`, `from pathlib import Path`, `from collections import defaultdict` | 均为标准库 | 合规 |

### 4.2 其他章节中的非标准库引用

| 位置 | import 语句 | 问题 | 建议 |
|------|------------|------|------|
| src/chapter-04.md:98 | `from pydantic import BaseModel` | 引用 pydantic（第三方库） | 出现在04章"概念介绍与最佳实践"中，属于进阶示例，非05章内容，合规 |
| src/appendix-a.md:98 | `from pydantic import BaseModel` | 引用 pydantic（第三方库） | 出现在附录A"进阶实战案例"中，属于进阶内容，非05章内容，合规 |
| src/appendix-a.md:177 | `uv init --python 3.11` | 引用 uv（第三方工具） | 附录A进阶案例，非05章内容，合规 |
| src/appendix-a.md:185 | `npm install @prisma/client next-auth bcryptjs` | 引用 npm 包 | 附录A进阶案例（Next.js项目），非05章内容，合规 |

**结论**：第05章实战案例严格遵守"仅使用 Python 标准库"的要求。其他章节中出现的第三方库引用均属于进阶示例或附录内容，不违反规范。

---

## 五、Bash 命令检查

| 位置 | 命令 | 问题 | 建议 |
|------|------|------|------|
| src/chapter-01.md:84 | `python --version` | 正确 | 合规 |
| src/chapter-01.md:177 | `git config --global user.name ...` | 正确 | 合规 |
| src/chapter-01.md:184 | `git --version` | 正确 | 合规 |
| src/chapter-01.md:257 | `claude` | 正确 | 合规 |
| src/chapter-01.md:285 | `code --version` | 正确 | 合规 |
| src/chapter-03.md:280 | `curl -fsSL https://claude.ai/install.sh \| bash` | 正确 | 合规 |
| src/chapter-03.md:285 | `irm https://claude.ai/install.ps1 \| iex` | 正确 | 合规 |
| src/chapter-03.md:290 | `claude --version` | 正确 | 合规 |
| src/chapter-03.md:309 | `claude --dangerously-skip-permissions` | 正确 | 合规 |
| src/chapter-03.md:358 | `npm install -g @moonshot-ai/kimi-code` | 正确 | 合规 |
| src/chapter-03.md:369 | `export KIMI_API_KEY=...` | 正确 | 合规 |
| src/chapter-04.md:220 | `claude -p "Explain what this project does"` | 正确 | 合规 |
| src/chapter-04.md:227 | `for file in $(cat files.txt); do ... done` | 正确 | Shell 循环语法正确 |
| src/chapter-06.md:254 | `docker build -t myapp:1.0 .` | 正确 | 合规 |
| src/chapter-06.md:255 | `docker run -d -p 3000:3000 myapp:1.0` | 正确 | 合规 |
| src/appendix-e.md:24 | `mkdir weather-cli && cd weather-cli` | 正确 | 合规 |
| src/appendix-e.md:27 | `uv init --python 3.11` | 正确 | 合规 |
| src/appendix-e.md:28 | `python -m venv .venv && source .venv/bin/activate` | 正确 | 合规 |
| src/appendix-e.md:178 | `npx create-next-app@latest dashboard ...` | 正确 | 合规 |
| src/appendix-e.md:259 | `npx shadcn add card button input ...` | 正确 | 合规 |

**结论**：全书 bash 命令无明显错误，Windows 和 macOS/Linux 命令区分清晰。

---

## 六、其他发现

### 6.1 代码块语言标注问题

| 位置 | 问题 | 建议 |
|------|------|------|
| src/chapter-07.md:373 | 测试驱动开发示例使用 `text` 代码块而非 `python` | 内容为自然语言描述，使用 `text` 合理 |
| src/appendix-e.md:36 | 项目目录树使用 `text` 代码块 | 目录树非代码，使用 `text` 合理 |
| src/appendix-e.md:191 | requirements.txt 使用 `text` 代码块 | 文本内容，使用 `text` 合理 |

### 6.2 潜在改进建议

| 位置 | 问题 | 建议 |
|------|------|------|
| src/chapter-05.md:51 | 第一版代码中 `import os` 已导入但未使用 | 代码中实际使用了 `pathlib` 和 `shutil`，`os` 为冗余导入。建议删除 |
| src/chapter-05.md:166 | 第二版代码中 `import os` 已导入但未使用 | 同上，`os` 为冗余导入。建议删除 |
| code/chapter-05/project-01/organize_downloads.py | 无冗余导入 | 实际代码中已正确移除 `import os`，与书中示例不一致 |

**说明**：书中第05章两个代码示例都包含 `import os`，但实际代码文件 `organize_downloads.py` 中已正确移除了该冗余导入。这是一个书稿与代码文件不一致的问题，建议同步更新书稿。

---

## 七、统计

| 指标 | 数量 |
|------|------|
| 代码块总数 | 约 65 个（含 Python、bash、text、json、yaml 等） |
| Python 代码块数 | 约 35 个 |
| 语法错误 | **0** |
| 命名问题 | **0**（教学示例中的故意展示不计入） |
| 路径问题 | **0** |
| 标准库违规 | **0** |
| 冗余导入 | **2**（chapter-05.md 中 `import os` 未使用） |
| 书稿与代码不一致 | **1**（organize_downloads.py 已移除 `import os`，书稿未同步） |
| 测试通过率 | **100%**（11/11 测试通过） |

---

## 八、总结

### 整体评价：优秀

1. **语法正确性**：所有 Python 代码文件均通过 `py_compile` 检查，无语法错误。
2. **命名规范**：所有实际代码均使用 snake_case，无拼音命名或无意义单字母。
3. **路径处理**：第05章实战案例使用 `pathlib.Path` 处理路径，自动适配 Windows/macOS，符合跨平台最佳实践。
4. **标准库合规**：第05章严格遵守"仅使用 Python 标准库"的要求。
5. **测试覆盖**：code/tests/ 目录下的测试全部通过（11/11）。

### 需要修复的问题（共 2 个，均为轻微）

1. **src/chapter-05.md:51** —— 第一版 `organize_downloads()` 代码中 `import os` 为冗余导入，建议删除。
2. **src/chapter-05.md:166** —— 第二版 `organize_downloads()` 代码中 `import os` 为冗余导入，建议删除。

> 注意：code/chapter-05/project-01-organize-downloads/organize_downloads.py 实际代码中已正确移除了 `import os`，书稿需要同步更新。
