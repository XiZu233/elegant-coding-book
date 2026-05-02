# Skill 风格测试报告

## 搜索结果摘要

本次搜索覆盖了 5 组关键词，检索了 GitHub、技术博客和 Claude Code Skill 市场等渠道。共发现约 15 个相关开源项目/资源，经过筛选后聚焦到 6 个高社区活跃度的候选：

- `JimLiu/baoyu-skills`（16.9k stars）— 文章插图 Skill，含教育预设
- `ZeroLu/awesome-nanobanana-pro`（9.9k stars）— Nano Banana Pro 提示词合集，含 Education & Knowledge 专类
- `wuyoscar/gpt_image_2_skill`（1.2k stars）— GPT Image 2 提示词库，含 Scientific & Educational 类别
- `op7418/Document-illustrator-skill`（514 stars）— 文档配图 Skill，含 vector-illustration 风格
- `axtonliu/smart-illustrator`（461 stars）— 三引擎智能插图工具
- `wanshuiyin/Auto-claude-code-research-in-sleep` — 学术论文插图 Skill

筛选逻辑：优先选择**有明确风格定义**、**社区验证**（stars > 500）、**教育场景适配**的项目。排除纯艺术创作、无结构 prompt、或状态为 Experimental 且作者声明不再维护的项目。

---

## 三款入选 Skill

### 1. Baoyu Article Illustrator（宝玉文章插图 Skill）

- **来源**：[https://github.com/JimLiu/baoyu-skills/tree/main/skills/baoyu-article-illustrator](https://github.com/JimLiu/baoyu-skills/tree/main/skills/baoyu-article-illustrator)
- **社区数据**：16.9k stars，2k forks
- **风格定义**：Type x Style x Palette 三维体系，支持 infographic / flowchart / framework / scene 等类型，风格含 notion / warm / minimal / blueprint / watercolor / elegant，教育场景有 `--preset edu-visual` 快捷预设
- **测试场景**：Agent Loop 循环图
- **测试结果**：成功
- **文件路径**：`src/assets/images/skill-tests/01-baoyu-article-illustrator.png`
- **与教材适配度评分**：9/10
  - 统一黑色轮廓线 + 复古柔和配色，视觉上"友好但专业"
  - 圆形布局清晰，三个节点（Explore/Act/Validate）信息层级分明
  - 文字渲染准确（"AGENTIC LOOP"、"EXPLORE"、"ACT"、"VALIDATE"）
  - 与教材"先动手再理解"的调性高度匹配

### 2. Document Illustrator — Vector Illustration 风格

- **来源**：[https://github.com/op7418/Document-illustrator-skill](https://github.com/op7418/Document-illustrator-skill)
- **社区数据**：514 stars，55 forks
- **风格定义**：扁平化矢量插画，统一粗细的黑色轮廓线，复古柔和的配色方案，官方标注适用场景包含"教育内容"
- **测试场景**：T 型能力模型
- **测试结果**：成功
- **文件路径**：`src/assets/images/skill-tests/02-document-illustrator-vector.png`
- **与教材适配度评分**：8/10
  - T 型结构表达清晰，横向（Breadth）和纵向（Depth）分区明确
  - 图标风格统一（机器人、对话框、人群、终端、括号、bug）
  - 中央"JUDGMENT + TASTE"发光效果增强了视觉焦点
  - 扣分项：Breadth 区域文字"AI TOOLS"、"COMMUNICATION"略小，在印刷品上可能不够清晰

### 3. GPT Image 2 — Scientific & Educational 风格

- **来源**：[https://github.com/wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill)
- **社区数据**：1.2k stars，119 forks
- **风格定义**：结构化 prompt 写作体系（背景/场景 -> 主体 -> 关键细节 -> 约束条件），含 Scientific & Educational / Infographics / Technical Illustration 等类别，支持质量分级（low/medium/high）
- **测试场景**：Docker 集装箱比喻
- **测试结果**：成功
- **文件路径**：`src/assets/images/skill-tests/03-gpt-image-2-scientific.png`
- **与教材适配度评分**：8.5/10
  - 三阶段叙事（Build & Pack -> Ship -> Pull & Run）逻辑清晰
  - 集装箱核心隐喻表达准确，内部层级（Application / Runtime / Dependencies / System Libraries）一目了然
  - 底部四个关键词（Portable / Consistent / Isolated / Lightweight）强化了信息密度
  - 风格偏"商业信息图"，比前两款稍正式，对零基础读者亲和力略低

---

## 与现有 9 种风格对比

| 维度 | 现有最佳（扁平插画） | Baoyu Article Illustrator | Document Illustrator Vector | GPT Image 2 Scientific |
|------|---------------------|---------------------------|----------------------------|------------------------|
| 信息清晰度 | 8 | 9 | 8 | 9 |
| 教育亲和力 | 9 | 9 | 8 | 7 |
| 生图可控性 | 7 | 8 | 7 | 8 |
| 风格一致性 | 8 | 9 | 8 | 7 |
| 文字渲染准确度 | 6 | 8 | 7 | 8 |
| 社区支持度 | 无 | 高（16.9k stars） | 中（514 stars） | 中（1.2k stars） |

---

## 最终推荐

**最值得吸收到教材配图体系中的是：Baoyu Article Illustrator 风格（统一黑色轮廓线 + 复古柔和配色 + 教育预设）**

理由：

1. **教育场景专精**：该 Skill 明确支持 `--preset edu-visual`，Type 体系中的 infographic / flowchart / framework 直接对应教材中的流程图、概念图、架构图需求
2. **视觉调性匹配**："友好但专业"的复古矢量风格，既不会让零基础读者感到冰冷，又保持了足够的信息密度
3. **文字渲染可靠**：三张测试图中，Baoyu 风格的文字准确度最高（所有标签清晰可读），这对教育内容至关重要
4. **社区规模最大**：16.9k stars 意味着 prompt 模板经过大量验证，后续迭代和维护有保障
5. **与现有扁平插画相比的优势**：在保持扁平插画信息清晰度的同时，增加了统一的轮廓线约束，使多张图之间的风格一致性更强；复古柔和配色比纯扁平色块更有温度，更适合纸质教材印刷

---

## 附录：生成脚本

生成脚本位于同目录下 `generate_test.py`，基于 ToAPIs（OpenAI 兼容格式）调用 `gpt-image-2` 模型。API Key 从项目根目录 `.env` 文件读取，未硬编码到脚本中（运行时手动填入，脚本用后即删）。
