# 教材截图素材索引

本目录收录从教程剪藏文档中提取、处理后用于教材的 6 张真实软件截图。

---

## 素材清单

| 教材位置 | 文件名 | 来源 | 水印状态 | 处理说明 |
|----------|--------|------|----------|----------|
| 01-1 VS Code 界面标注图 | `../01-1-vscode-editor.png` | 菜鸟教程 | 无 | 暗色主题，含红色箭头/方框中文标注 |
| 01-4 Git PATH 配置 | `../01-4-git-path-config.png` | 知乎 | **已裁剪去除** | 裁剪右下角水印，保留核心选项内容 |
| 01-4 Git 行尾转换 | `../01-4-git-line-ending.png` | 知乎 | **已裁剪去除** | 裁剪右下角水印，三个选项均清晰可读 |
| 02-5 Python Traceback 错误信息 | `../02-5-python-traceback.png` | **程序生成** | 无 | 使用 PIL 生成，含中文标注框 |
| 03-2 Claude Code 启动界面 | `../03-2-claude-welcome.png` | 菜鸟教程 | 无 | 显示"Welcome back"界面，非首次登录引导 |
| 03-4 CC-Switch 主界面 | `../03-4-ccswitch-interface.png` | cc.x-qu.com | 无 | 主界面截图，展示 Provider 管理 |
| 05-3 Plan/Normal Mode 循环图 | `../05-3-plan-mode-diagram.png` | DataCamp | 无 | 展示三种权限模式的切换关系 |
| 05-3 Plan Mode 终端指示器 | `../05-3-plan-mode-indicator.jpg` | DataCamp | 无 | 终端中 `⏸ plan mode on` 状态 |

---

## 待人工处理项

| 问题 | 位置 | 建议 |
|------|------|------|
| VS Code 为暗色主题 | 01-1 | 教材要求浅色主题（印刷清晰），建议自行截图浅色主题界面替换 |
| Claude Code 非首次启动 | 03-2 | 当前为"Welcome back"，如需首次登录引导界面，建议自行截图 |
| 全屏截图水印未去除 | temp/git/git-step-01.png | 底部中央大面积水印，未使用 |
| 浏览器跳转截图水印 | temp/git/git-step-17.png | 底部中央大面积水印，未使用 |

---

## 原始素材目录

- `archive/temp/vscode/` — VS Code + Claude Code 截图（来自菜鸟教程）
- `archive/temp/git/` — Git for Windows 安装步骤截图（来自知乎，含裁剪版）
- `archive/temp/ccswitch/` — CC-Switch 界面截图（来自 cc.x-qu.com）
- `archive/temp/planmode/` — Plan/Normal Mode 截图（来自 DataCamp）
- `archive/temp/vscode-report.md` / `archive/temp/git-report.md` / `archive/temp/ccswitch-report.md` — 各分类提取报告
