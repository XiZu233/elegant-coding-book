# 配套代码仓库

> 本目录是《给零基础小白准备的 AI 时代优雅编程》教程的配套代码资源，包含示例代码、实战项目和自动化测试。

## 目录结构

```
code/
├── chapter-01-setup/              # 第01章：搭建基础开发环境
│   └── ...
├── chapter-02-python-basics/      # 第02章：编程语法和代码审美
│   └── examples/                  # 6 个基础语法示例
│       ├── 01_variables.py        # 变量声明和类型
│       ├── 02_functions.py        # 函数定义和调用
│       ├── 03_conditions.py       # 条件判断
│       ├── 04_loops.py            # 循环
│       ├── 05_lists.py            # 列表操作
│       └── 06_dictionaries.py     # 字典操作
├── chapter-03-ai-tools/           # 第03章：AI 编程工具入门
│   └── ...
├── chapter-04-best-practices/     # 第04章：概念介绍与最佳实践
│   └── ...
├── chapter-05-projects/           # 第05章：实战案例
│   ├── project-01-organize-downloads/   # 案例一：自动整理下载文件夹
│   │   ├── organize_downloads.py
│   │   └── README.md
│   └── project-02-rename-photos/        # 案例二：批量重命名照片
│       ├── rename_photos.py
│       └── README.md
├── chapter-06-agent-knowledge/    # 第06章：Agent 时代知识基础
│   └── ...
├── chapter-07-long-term/          # 第07章：优雅编程的长期主义
│   └── ...
├── shared/                        # 共享资源
│   ├── .gitignore-template        # Python 项目通用 .gitignore
│   └── common-prompts.md          # 常用 AI Prompt 模板合集
└── tests/                         # 自动化测试
    ├── test_chapter02_examples.py # 第02章示例代码测试
    └── test_chapter05_projects.py # 第05章实战项目测试
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行示例代码

每个示例都是独立的，可以直接运行：

```bash
cd chapter-02-python-basics/examples
python 01_variables.py
python 02_functions.py
# ...
```

### 3. 运行测试

```bash
pytest tests/ -v
```

## 使用说明

### 学习者

1. 按章节顺序学习，每个 `examples/` 目录下的代码都可以直接运行
2. 第05章的实战项目包含完整的 README.md，按步骤操作即可
3. 遇到问题时，使用 `shared/common-prompts.md` 中的模板向 AI 求助

### 代码规范

- 所有示例代码**只使用 Python 标准库**，无需安装第三方包
- 遵循 PEP 8 命名规范（snake_case）
- 关键步骤附有中文注释
- 代码风格适合零基础初学者阅读
