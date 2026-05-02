# 01 搭建基础开发环境

欢迎来到编程世界。本章的目标很简单：让你在 **30 分钟内** 写下第一行代码并看到它运行起来。我们会一步一步来，不需要任何基础。

---

## 第一层：最小必要环境（30分钟）

> 这一层只需要装两样东西：一个写代码的编辑器，一个运行代码的 Python 解释器。其他什么都不装。

---

### 1. 安装 VS Code（代码编辑器）

VS Code 是微软推出的免费代码编辑器，也是目前最流行的开发工具之一。

**Step 1：下载**

1. 打开浏览器，访问 https://code.visualstudio.com/
2. 网站会自动识别你的系统，点击大大的下载按钮即可
   - Windows 用户：下载 **User Installer 64-bit**（不需要管理员权限）
   - macOS 用户：下载 `.zip` 或 `.dmg` 版本

[此处配图：VS Code 官网下载页面截图，红框标注下载按钮]

**Step 2：安装**

双击下载的安装包，一路点击"下一步"。只有两个地方需要注意：

- **勾选"添加到 PATH"**（或 "Add to PATH"）：这样你可以在任意地方用命令打开 VS Code
- **勾选"注册为受支持的文件编辑器"**：让 `.py` 文件默认用 VS Code 打开

[此处配图：VS Code 安装向导截图，红框标注"Add to PATH"选项]

**Step 3：安装中文语言包（可选）**

如果你更习惯中文界面：

1. 打开 VS Code
2. 按 `Ctrl+Shift+X`（macOS 是 `Cmd+Shift+X`）打开扩展面板
3. 搜索 `Chinese (Simplified)`
4. 点击安装，然后按提示重启 VS Code

[此处配图：扩展市场搜索中文包的截图]

**Step 4：验证**

打开 VS Code，点击左上角 `文件 → 打开文件夹`，随便选一个你电脑上的文件夹。如果能正常打开，说明 VS Code 安装成功。

> [配图占位：此处应有 VS Code 界面标注图，详见附录D]

---

### 2. 安装 Python（代码解释器）

Python 是目前最适合初学者入门的编程语言，也是 AI 时代最主流的开发语言。

**Step 1：下载**

1. 打开浏览器，访问 https://www.python.org/downloads/
2. 点击页面上最大的黄色按钮 **"Download Python 3.x.x"**

[此处配图：Python 官网下载页面截图，红框标注黄色下载按钮]

**Step 2：安装（Windows 关键步骤）**

双击下载的 `.exe` 文件开始安装。这里有一个**超级重要的勾选框**：

> **务必勾选 "Add Python to PATH"（添加到环境变量）**
>
> 如果没勾选，VS Code 将找不到 Python，后面所有步骤都会报错。

[此处配图：Python 安装向导截图，红框强力标注"Add Python to PATH"复选框]

勾选后，点击 **"Install Now"** 即可。

macOS 用户：打开下载的 `.pkg` 文件，按向导完成安装即可。

**Step 3：验证**

打开 VS Code，按 `` Ctrl+` ``（数字 1 左边的那个键）打开底部终端，输入：

```bash
python --version
```

如果看到类似 `Python 3.12.3` 的输出，恭喜你，Python 安装成功。

[此处配图：VS Code 终端中显示 python --version 输出结果的截图]

> 如果 Windows 提示 "python" 不是内部命令，说明安装时漏勾了 "Add to PATH"。请重新运行 Python 安装包，选择 "Modify"，然后勾选 "Add Python to PATH"。

---

### 3. 第一个 Hello World

现在，让我们写下人生的第一行代码。

**Step 1：创建一个文件夹**

在你的电脑上创建一个文件夹，命名为 `my-first-code`。

**Step 2：用 VS Code 打开它**

在 VS Code 中点击 `文件 → 打开文件夹`，选择刚才创建的 `my-first-code`。

**Step 3：创建 Python 文件**

1. 点击左侧资源管理器空白处，或者点击 `新建文件` 图标
2. 输入文件名：`hello.py`
3. 回车确认

[此处配图：VS Code 左侧资源管理器，红框标注新建文件按钮]

**Step 4：写下第一行代码**

在右侧编辑器中输入：

```python
print("Hello, World!")
```

**Step 5：运行它**

点击右上角的 **▶️ 三角形运行按钮**，或者右键编辑器选择 `在终端中运行 Python 文件`。

你会在底部终端看到：

```
Hello, World!
```

[此处配图：VS Code 中 hello.py 运行后的截图，红框标注终端输出]

**恭喜你！这就是你的第一行代码。** 从现在开始，你是一个程序员了。

---

**✅ 里程碑：最小必要环境已完成**

你已经拥有了写代码和运行代码的全部基础能力。接下来，我们再装两个工具，让你能更好地管理代码和使用 AI 辅助编程。

---

## 第二层：基础工具（再花30分钟）

---

### 4. 安装 Git（版本控制）

Git 是一个"代码时光机"。它帮你记录代码的每一次修改，写错了可以随时回退，也是和别人协作开发的必备工具。

**Step 1：下载**

访问 https://git-scm.com/downloads，点击下载对应系统的安装包。

**Step 2：安装（Windows）**

双击安装包，一路下一步。只有两个选项需要关注：

1. **默认编辑器**：选择 **VS Code**（而不是默认的 Vim）
2. **PATH 环境**：选择 **"Git from the command line and also from 3rd-party software"**

[此处配图：Git 安装向导截图，红框标注"默认编辑器选 VS Code"和"PATH 选项"]

其他选项全部保持默认即可。

> [配图占位：此处应有 Git 安装关键选项截图，详见附录D]

macOS 用户：打开下载的 `.dmg` 安装包，双击 `.pkg` 文件完成安装。

**Step 3：首次配置**

打开 VS Code 终端，输入以下两条命令（把引号里的内容换成你的名字和邮箱）：

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱@example.com"
```

**Step 4：验证**

```bash
git --version
```

看到版本号输出，说明 Git 安装成功。

---

**✅ 里程碑：基础工具已就绪**

你现在可以写代码、运行代码、用 Git 记录代码历史了。

---

## 第三层：AI 编程助手（与第03章衔接）

---

### 5. 安装 Kimi Code（AI 编程助手）

Kimi Code 是月之暗面推出的 AI 编程助手，可以直接在终端里帮你写代码、改代码、解答问题。国内网络直接可用，对新手非常友好。

**Step 1：下载安装**

打开终端，复制粘贴以下命令：

**Windows（PowerShell）：**
```powershell
irm https://claude.ai/install.ps1 | iex
```

**macOS / Linux：**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

等待约 5 分钟，安装程序会自动完成配置。

**Step 2：获取 API Key**

1. 打开浏览器，访问 https://www.kimi.com/code/console
2. 登录后点击「创建 API Key」
3. 复制以 `sk-kimi-` 开头的密钥（一串很长的字符）

[此处配图：Kimi Code 控制台创建 API Key 的页面截图]

> **注意**：请妥善保管你的 API Key，不要分享给他人，也不要上传到公开的地方。

**Step 3：配置环境变量**（环境变量详见第06章2.2节）

根据你的系统，将 API Key 配置到环境变量中：

**Windows（PowerShell）：**
```powershell
[Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "sk-kimi-你的密钥", "User")
```

**macOS（默认终端）：**
```bash
echo 'export ANTHROPIC_API_KEY="sk-kimi-你的密钥"' >> ~/.zshrc
source ~/.zshrc
```

**Linux：**
```bash
echo 'export ANTHROPIC_API_KEY="sk-kimi-你的密钥"' >> ~/.bashrc
source ~/.bashrc
```

**Step 4：启动并验证**

在终端中输入：

```bash
claude
```

你会进入 Kimi Code 的交互界面。试着跟它说句话：

```
你好，请帮我解释一下 print("Hello, World!") 这行代码是什么意思？
```

如果 Kimi 回复了你，说明一切配置成功。

[此处配图：终端中 Kimi Code 交互界面截图，展示对话示例]

---

**✅ 里程碑：AI 编程助手已就绪**

你现在拥有了一个 24 小时在线的编程导师。遇到不懂的代码、报错信息，都可以直接问它。

---

## 环境验证清单

> [配图占位：此处应有环境验证流程图，详见附录D]

全部安装完成后，在 VS Code 终端中依次输入以下命令，确认一切正常：

```bash
# 1. VS Code
code --version

# 2. Python
python --version

# 3. Git
git --version

# 4. Kimi Code
claude --version
```

如果每条命令都返回了版本号，你的开发环境就搭建完成了。

---

## 下一步

- **第 02 章**：Python 基础语法 —— 变量、数据类型、条件判断、循环
- **第 03 章**：用 AI 辅助编程 —— 让 Kimi Code 帮你写更复杂的程序

---

## 参考文档

| 工具 | 官方文档 |
|------|---------|
| VS Code | https://code.visualstudio.com/docs |
| Python | https://docs.python.org/zh-cn/3/tutorial/ |
| Git | https://git-scm.com/doc |
| Kimi Code | https://www.kimi.com/code/docs |

---

## 附录：常见问题

**Q：安装 Python 时忘记勾选 "Add to PATH" 怎么办？**

重新运行 Python 安装包，选择 "Modify"，然后勾选 "Add Python to PATH"，点击完成。

**Q：Windows 上输入 `python` 没有反应，但 `py` 有反应？**

这是 Windows 的别名机制。你可以在 VS Code 中按 `Ctrl+Shift+P`，输入 "Python: Select Interpreter"，选择你安装的 Python 版本即可。

**Q：Kimi Code 启动后提示 API Key 无效？**

1. 检查 Key 是否复制完整（以 `sk-kimi-` 开头）
2. 检查环境变量是否配置正确
3. 如果刚配置完环境变量，尝试关闭终端重新打开

**Q：我不想用 Kimi Code，想用 Claude Code 可以吗？**

可以。Claude Code 的安装方式与 Kimi Code 完全相同（使用同一个安装脚本），区别在于 API Key 需要从 https://console.anthropic.com 获取。但需要注意的是，Claude Code 需要稳定的国际网络环境。
