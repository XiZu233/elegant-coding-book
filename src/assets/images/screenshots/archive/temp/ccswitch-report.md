# CC-Switch + Plan/Normal Mode 截图提取报告

## CC-Switch 截图

- **提取 URL**：1 个
- **成功下载**：1 个
- **下载目录**：`src/assets/images/screenshots/temp/ccswitch/`

| 文件名 | 来源 | 大小 | 推荐用途 |
|--------|------|------|----------|
| `ccswitch-main-interface.png` | https://cc.x-qu.com/assets/image-1-R32R1qyR.png | ~205 KB | **推荐用于 03-4**：CC-Switch 主界面截图，展示 Provider 管理界面，可直接用于教材 03 章「AI编程工具入门」的 CC-Switch 工具介绍部分 |

**说明**：CC-Switch 教程原文中仅包含 1 张图片（image-1-R32R1qyR.png），即主界面截图。该截图展示了 CC-Switch 的核心功能界面，适合作为教材配图。

---

## Plan/Normal Mode 截图

- **搜索结果**：找到（非官方，来自 DataCamp 教程）
- **推荐来源**：https://www.datacamp.com/tutorial/claude-code-plan-mode
- **下载目录**：`src/assets/images/screenshots/temp/planmode/`

| 文件名 | 来源 | 大小 | 内容描述 | 推荐用途 |
|--------|------|------|----------|----------|
| `datacamp-image6-permission-mode.png` | DataCamp | ~1.5 MB | 权限模式循环图（Normal / Auto-Accept / Plan Mode 的切换关系） | **最推荐用于 05-3**：直观展示三种模式的切换关系 |
| `datacamp-image4-planmode-indicator.jpg` | DataCamp | ~22 KB | 终端输入框显示 Plan Mode 指示器（`⏸ plan mode on`） | **推荐用于 05-3**：展示终端中 Plan Mode 的实际状态 |
| `datacamp-image2-refactoring-plan.jpg` | DataCamp | ~210 KB | Claude Code 生成的重构计划截图 | 辅助说明 Plan Mode 的输出格式 |
| `datacamp-image3-completion.jpg` | DataCamp | ~163 KB | Plan 完成后的选项界面（含 Ctrl+G 编辑快捷键提示） | 辅助说明 Plan Mode 完成后的交互 |
| `datacamp-image5-explore-subagent.jpg` | DataCamp | ~120 KB | Plan Mode 下通过 Explore subagent 读取项目文件 | 进阶内容配图 |
| `datacamp-image10-askuserquestion.jpg` | DataCamp | ~135 KB | Plan Mode 中 AskUserQuestion 显示架构选项 | 进阶内容配图 |
| `datacamp-image1-workflow.png` | DataCamp | ~1.5 MB | Explore → Plan → Execute 循环工作流图 | 概念说明图，非终端截图 |

**注意**：未在 Anthropic 官方文档（docs.anthropic.com / code.claude.com）或 GitHub 仓库中找到 Plan/Normal Mode 的终端截图。DataCamp 教程是目前找到的最权威第三方来源，截图质量较高且内容准确。

---

## 待解决问题

1. **Plan/Normal Mode 缺少官方截图**：Anthropic 官方文档中未找到 Plan Mode 的终端界面截图。当前使用的 DataCamp 截图虽内容准确，但非官方来源。
2. **缺少 Normal Mode 单独截图**：现有素材中 Plan Mode 内容较多，但缺少一张清晰的「Normal Mode 与 Plan Mode 对比」的终端截图。
3. **建议补充方案**：
   - 方案 A：在教材中直接使用 DataCamp 的 `image6-permission-mode.png`（模式循环图）+ `image4-planmode-indicator.jpg`（终端状态指示器）组合说明
   - 方案 B：用户自行运行 `claude` 进入终端，按 `Shift+Tab` 切换模式后截图，可获得最贴合教材的素材
   - 方案 C：使用终端模拟工具（如 carbon.now.sh 或 terminalscreenshot.com）基于文本内容生成示意图

---

## 素材清单汇总

| 教材位置 | 推荐图片 | 状态 |
|----------|----------|------|
| 03-4 CC-Switch 界面 | `temp/ccswitch/ccswitch-main-interface.png` | 已获取 |
| 05-3 Plan/Normal Mode 切换 | `temp/planmode/datacamp-image6-permission-mode.png` + `datacamp-image4-planmode-indicator.jpg` | 已获取（第三方来源） |
