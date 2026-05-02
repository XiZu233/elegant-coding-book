#!/usr/bin/env python3
"""批量生成教材配图 - 异步任务轮询版
API 返回 task ID，需要轮询查询任务状态
"""

import os
import sys
import time
import json
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# ========== 配置 ==========
API_KEY = "sk-lQsah9Z9K0KtbaoEP3ORRWQKf27xNQYFkvoK5ZQuiOwtNJv4"
BASE_URL = "https://toapis.com/v1"
OUTPUT_DIR = Path("e:/00llm-wiki/01Projects/给零基础小白准备的AI时代优雅编程/src/assets/images")

POLL_INTERVAL = 10      # 轮询间隔（秒）
MAX_WAIT = 600          # 最大等待时间（秒）

# 28 张配图任务列表
TASKS = [
    # 第1批 (7张)
    {"id": "01", "file": "G1-learning-roadmap.png", "prompt": "Hand-drawn doodle illustration, bold marker lines with organic rough edges, imperfect wobbly outlines, dry brush texture, warm color fills with slight color bleeding outside lines, light cream paper texture background, sketchbook aesthetic. A horizontal timeline from left to right with 7 nodes connected by a wavy path like a travel journal route. Each node has a hand-drawn icon: lightbulb for '00 编程在AI时代的重新定义' (1-2h), gear for '01 搭建基础开发环境' (2-3h), code brackets for '02 编程语法和代码审美' (4-6h), robot for '03 AI编程工具入门' (2-3h), book for '04 概念介绍与最佳实践' (3-4h), hammer for '05 实战案例' (6-10h), network globe for '06 Agent时代需要补充的知识基础' (3-4h), compass for '07 优雅编程的长期主义' (1-2h). At the bottom: '预计总学习时间：2-4 周'. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
    {"id": "02", "file": "00-traditional-vs-ai.png", "prompt": "Flat vector illustration with unified black outline strokes, retro-soft color palette (muted teal, warm amber, dusty rose, soft sage), white background, clean educational textbook aesthetic, infographic style. Left side: '传统编程' — a person sitting at a desk facing a screen full of dense code, looking stressed and confused, with labels '记忆语法', '手动调试', '逐行编写'. Right side: 'AI 编程' — a person speaking to a friendly AI robot, the robot generating clean code on a screen, the person looks relaxed and confident, with labels '描述需求', 'AI 实现', '人类验收'. In the middle: a large curved arrow pointing from left to right labeled '范式转变'. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
    {"id": "03", "file": "00-ability-pyramid.png", "prompt": "Flat vector illustration with unified black outline strokes, retro-soft color palette (muted teal, warm amber, dusty rose, soft sage), white background, clean educational textbook aesthetic, infographic style. A three-layer pyramid. Bottom layer (widest): '基础能力' with icons and labels '逻辑思维', '问题分解', '表达能力'. Middle layer: '工具能力' with icons and labels 'AI 工具使用', 'Git', '调试'. Top layer (smallest): '高阶能力' with icons and labels '产品思维', '系统思维', '判断力'. To the right of the pyramid, a speech bubble says '数学/英语 = 加分项，不是门槛'. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
    {"id": "04", "file": "01-ai-tool-forms.png", "prompt": "Flat vector illustration with unified black outline strokes, retro-soft color palette (muted teal, warm amber, dusty rose, soft sage), white background, clean educational textbook aesthetic, infographic style. Three-column comparison layout. Column 1: '网页版' — a browser window frame with a chat interface inside, three feature bullets below: '随时可用', '无需安装', '功能受限'. Column 2: '桌面应用' — a desktop application window with a code editor and chat sidebar, three feature bullets: '深度集成', '本地文件', '付费订阅'. Column 3: 'CLI 命令行' — a terminal window with command prompt, three feature bullets: '极致效率', '键盘操作', '本书推荐'. At the bottom center, a large arrow points to the CLI column with label '本书主要使用 CLI 形态'. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
    {"id": "05", "file": "01-terminal-commands.png", "prompt": "Flat vector illustration with unified black outline strokes, retro-soft color palette (muted teal, warm amber, dusty rose, soft sage), white background, clean educational textbook aesthetic, infographic style. A simplified terminal window with rounded corners and a title bar showing a command prompt. Inside the terminal, four command examples stacked vertically, each in a different colored block: blue block shows command 'pwd' with output '/home/user/project', green block shows 'ls' with file list, amber block shows 'cd src' with path change indicator, rose block shows 'mkdir new_folder' with folder creation icon. Each command is color-coded: commands in blue, output in dark gray, prompt in green. Labels on the right side: '命令', '输出', '提示符'. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
    {"id": "06", "file": "01-env-checklist.png", "prompt": "Flat vector illustration with unified black outline strokes, retro-soft color palette (muted teal, warm amber, dusty rose, soft sage), white background, clean educational textbook aesthetic, infographic style. A horizontal 4-step checklist flow. Step 1: '检查 Python' with a command snippet 'python --version' and a green checkmark. Step 2: '检查 Git' with 'git --version' and green checkmark. Step 3: '检查 VS Code' with code icon and green checkmark. Step 4: '检查 AI 工具' with robot icon and green checkmark. Steps connected by arrows. After step 4, a final banner says '环境就绪，开始编程！'. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
    {"id": "07", "file": "02-python-four-elements.png", "prompt": "Flat vector illustration with unified black outline strokes, retro-soft color palette (muted teal, warm amber, dusty rose, soft sage), white background, clean educational textbook aesthetic, infographic style. A mind map with central node 'Python 四要素' in a large circle. Four branches radiating outward: Branch 1 (teal): '变量' with sub-label '存储数据' and a tiny code snippet 'name = Alice'. Branch 2 (amber): '函数' with '封装操作' and 'def greet():'. Branch 3 (rose): '条件' with '做出判断' and 'if score > 60:'. Branch 4 (sage): '循环' with '重复执行' and 'for i in range(5):'. Each branch has a small icon matching its concept. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},

    # 第2批 (7张)
    {"id": "08", "file": "02-indent-compare.png", "prompt": "Flat vector illustration with unified black outline strokes, retro-soft color palette (muted teal, warm amber, dusty rose, soft sage), white background, clean educational textbook aesthetic, infographic style. Top half: '错误示例' — a code block with mixed tabs and spaces shown as jagged indentation, red wavy underline beneath problematic lines, a red X mark on the right. Bottom half: '正确示例' — a code block with uniform 4-space indentation shown as smooth steps, green checkmark on the right. On the far right, a vertical text box says 'Python 用缩进表示层级，不是大括号'. The code snippets use simple Python examples with Chinese comments. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
    {"id": "09", "file": "02-function-lego.png", "prompt": "Hand-drawn doodle illustration, bold marker lines with organic rough edges, imperfect wobbly outlines, dry brush texture, warm color fills with slight color bleeding outside lines, light cream paper texture background, sketchbook aesthetic. Left side: a large messy scribble block labeled '混乱的代码'. Middle: a big arrow labeled '拆分成函数'. Right side: 4 small hand-drawn LEGO-like blocks stacked into a neat tower, each block labeled with a function name: '获取输入', '计算结果', '格式化输出', '输出报告'. Bottom caption: '函数就像积木，可以拼装组合'. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
    {"id": "10", "file": "02-debug-flow.png", "prompt": "Flat vector illustration with unified black outline strokes, retro-soft color palette (muted teal, warm amber, dusty rose, soft sage), white background, clean educational textbook aesthetic, infographic style. A circular flow diagram with 4 nodes connected by arrows forming a loop. Node 1: '假设' with label '代码应该输出 X' and a lightbulb icon. Node 2: '验证' with label '运行并观察' and a play button icon. Node 3 (diamond shape): '结果符合预期？' with two outgoing paths. Path '是' leads to Node 4: '继续' with green checkmark. Path '否' leads to '修正假设' with wrench icon then arrow back to Node 1. The outer loop arrow is labeled '调试思维'. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
    {"id": "11", "file": "03-ai-timeline.png", "prompt": "Flat vector illustration with unified black outline strokes, retro-soft color palette (muted teal, warm amber, dusty rose, soft sage), white background, clean educational textbook aesthetic, infographic style. A horizontal timeline with three eras. Era 1 (2021-2023): 'IDE 插件时代' with a code editor icon showing autocomplete suggestions, label '代码补全', representative tool 'GitHub Copilot'. Era 2 (2023-2024): '聊天窗口时代' with a chat bubble interface icon, label '对话生成', representative tool 'Cursor Chat'. Era 3 (2024-present): 'Agent 编程时代' with a robot agent icon executing tasks, label '自主执行', representative tool 'Claude Code'. Each era has a colored node on the timeline and a small thumbnail-style frame. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
    {"id": "12", "file": "03-claude-md-role.png", "prompt": "Flat vector illustration with unified black outline strokes, retro-soft color palette (muted teal, warm amber, dusty rose, soft sage), white background, clean educational textbook aesthetic, infographic style. Left side: a simplified project directory tree with folders and files. The file 'CLAUDE.md' at the root is highlighted with a glowing amber aura and a star badge. An arrow points from CLAUDE.md to the right side: a friendly AI robot character. Above the arrow: '每次会话自动加载'. Below the robot, 3-4 example rule cards floating: '使用 Python 3.11+', '变量命名用 snake_case', '优先使用标准库', '提交前运行测试'. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
    {"id": "13", "file": "04-agent-loop.png", "prompt": "Flat vector illustration with unified black outline strokes, retro-soft color palette (muted teal, warm amber, dusty rose, soft sage), white background, clean educational textbook aesthetic, infographic style. A circular flow with three rounded rectangles connected by thick curved arrows forming a loop. Rectangle 1 (teal): '收集上下文' with magnifying glass icon, sub-labels '读取文件', '分析代码', '理解需求'. Rectangle 2 (amber): '采取行动' with hammer/tool icon, sub-labels '编辑代码', '运行命令', '创建文件'. Rectangle 3 (sage): '验证结果' with checkmark icon, sub-labels '检查输出', '确认正确', '收集反馈'. Curved arrow from 3 back to 1. Outside the loop, a caption: '根据任务自动调整迭代次数'. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
    {"id": "14", "file": "04-extension-layers.png", "prompt": "Isometric 3D illustration, 30-degree axonometric projection, no perspective distortion, solid 3D blocks with subtle flat shading, clean geometric construction, miniature model aesthetic, light gray ground plane, soft gradient sky. Three stacked layers shown as 3D platforms. Bottom layer (largest base): a teal platform labeled 'Agent Loop' with circular arrow symbols. Middle layer: four equal-sized blocks on top of the base, labeled 'CLAUDE.md（持久记忆）', 'Skills（知识库）', 'MCP（外部工具）', 'Subagents（隔离执行）'. Top layer (smallest): a single golden block labeled 'Hooks（确定性自动化）'. Arrows show call relationships between layers. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},

    # 第3批 (7张)
    {"id": "15", "file": "04-context-window.png", "prompt": "Flat vector illustration with unified black outline strokes, retro-soft color palette (muted teal, warm amber, dusty rose, soft sage), white background, clean educational textbook aesthetic, infographic style. A large rectangular container labeled 'Context Window' at the top. Inside, colorful blocks filling the container representing: '对话历史' (blue blocks), '文件内容' (green blocks), '命令输出' (amber blocks), 'CLAUDE.md' (rose block). On the right side of the container, a warning triangle with '满' label indicating near capacity. Below the container, four tool icons in a row: trash can labeled '/clear', compression arrows labeled '/compact', speech bubble labeled '/btw', and a clone figure labeled 'Subagents'. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
    {"id": "16", "file": "04-decision-tree.png", "prompt": "Flat vector illustration with unified black outline strokes, retro-soft color palette (muted teal, warm amber, dusty rose, soft sage), white background, clean educational textbook aesthetic, infographic style. A top-down decision tree. Root node at top: '需要什么？'. Seven branches flowing downward to leaf nodes, each with a small icon: Branch 1: '持久约定 → CLAUDE.md' with document icon. Branch 2: '可重用知识 → Skills' with book icon. Branch 3: '外部服务 → MCP' with plug icon. Branch 4: '隔离任务 → Subagents' with clone icon. Branch 5: '多会话协作 → Agent Teams' with group icon. Branch 6: '事件自动化 → Hooks' with hook/anchor icon. Branch 7: '打包分发 → Plugins' with package box icon. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
    {"id": "17", "file": "04-permission-model.png", "prompt": "Flat vector illustration with unified black outline strokes, retro-soft color palette (muted teal, warm amber, dusty rose, soft sage), white background, clean educational textbook aesthetic, infographic style. A horizontal slider bar with 6 permission modes arranged left to right showing increasing security. Mode 1 (red): 'Bypass' with label '全开' and '危险'. Mode 2 (orange): 'Auto' with label '自动审查' and '谨慎'. Mode 3 (yellow): 'Accept Edits' with label '自动编辑' and '日常开发'. Mode 4 (green): 'Default' with label '默认询问' and '推荐'. Mode 5 (blue): 'Plan' with label '只读' and '审查代码'. Mode 6 (purple): 'DontAsk' with label '自动拒绝' and '最高安全'. Each mode is a colored block on the slider with a small icon. An arrow at the bottom points right labeled '安全级别递增'. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
    {"id": "18", "file": "05-project-tree-cli.png", "prompt": "Flat vector illustration with unified black outline strokes, retro-soft color palette (muted teal, warm amber, dusty rose, soft sage), white background, clean educational textbook aesthetic, infographic style. A stylized directory tree diagram for a Python CLI project. Root: 'weather-cli/'. Branches: 'src/weather_cli/' (green, labeled '源代码') with files '__init__.py', 'main.py ← CLI 入口', 'api.py ← API 客户端', 'config.py ← 配置管理', 'cache.py ← 本地缓存', 'models.py ← 数据模型'. 'tests/' (yellow, labeled '测试文件') with 'test_api.py', 'test_cache.py', 'test_config.py'. 'pyproject.toml' (blue, labeled '项目配置'). 'README.md' (gray, labeled '项目说明'). Color-coded folder icons matching the labels. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
    {"id": "19", "file": "05-project-tree-nextjs.png", "prompt": "Flat vector illustration with unified black outline strokes, retro-soft color palette (muted teal, warm amber, dusty rose, soft sage), white background, clean educational textbook aesthetic, infographic style. A stylized directory tree diagram for a Next.js project. Root: 'my-dashboard/'. Branches: 'app/' (blue, labeled 'App Router 页面') with route folders and 'page.tsx', 'layout.tsx'. 'components/' (green, labeled '组件') with 'Chart.tsx', 'Sidebar.tsx'. 'lib/' (orange, labeled 'Server Actions') with 'actions.ts'. 'db/' (purple, labeled '数据库') with 'schema.ts'. 'public/' (gray) with static assets. 'package.json' and 'next.config.js' at root. Color-coded folder icons. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
    {"id": "20", "file": "06-http-cycle.png", "prompt": "Flat vector illustration with unified black outline strokes, retro-soft color palette (muted teal, warm amber, dusty rose, soft sage), white background, clean educational textbook aesthetic, infographic style. Left side: a laptop labeled '客户端（你的程序）'. Right side: a server tower labeled '服务器'. Between them, two horizontal arrows. Top arrow pointing right labeled '请求' with smaller labels 'GET', 'POST', 'PUT', 'DELETE' along the arrow. A small package box icon on the arrow labeled 'JSON'. Bottom arrow pointing left labeled '响应' with status codes '200 OK', '404 Not Found' along the arrow, also with a package box icon labeled 'JSON'. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
    {"id": "21", "file": "06-path-system.png", "prompt": "Flat vector illustration with unified black outline strokes, retro-soft color palette (muted teal, warm amber, dusty rose, soft sage), white background, clean educational textbook aesthetic, infographic style. A simplified file system tree. Root '/' at top, branching down: 'home/' → 'user/' → 'project/' → 'data.txt'. A red arrow traces the full path from root to file, labeled '绝对路径 = /home/user/project/data.txt'. A blue arrow starts from 'project/' folder pointing to 'data.txt', labeled '相对路径（从 project 出发）= ./data.txt'. On the right side, a speech bubble says 'Agent 报错找不到文件，80% 是站错地方了'. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},

    # 第4批 (7张)
    {"id": "22", "file": "06-virtual-env.png", "prompt": "Flat vector illustration with unified black outline strokes, retro-soft color palette (muted teal, warm amber, dusty rose, soft sage), white background, clean educational textbook aesthetic, infographic style. Top half: '全局安装' — a single large room filled with a messy pile of Python packages all mixed together, looking chaotic. Bottom half: '虚拟环境' — three separate clean rooms side by side. Room A (teal) contains 'requests==2.28' and its dependencies neatly arranged. Room B (amber) contains 'requests==2.31' and different dependencies. Room C (rose) contains 'flask' and its own set. Walls between rooms are thick and solid, emphasizing isolation. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
    {"id": "23", "file": "06-docker-container.png", "prompt": "Hand-drawn doodle illustration, bold marker lines with organic rough edges, imperfect wobbly outlines, dry brush texture, warm color fills with slight color bleeding outside lines, light cream paper texture background, sketchbook aesthetic. Three panels left to right. Panel 1: a hand-drawn laptop labeled '你的电脑' with an app and some dependency icons inside. Panel 2: a large shipping container labeled 'Docker 打包' with the same app + runtime + dependencies + configuration all neatly packed inside. Panel 3: another laptop labeled '任何服务器' with the container being opened and the app running identically. Bottom caption: '一次打包，到处运行'. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
    {"id": "24", "file": "07-t-shaped-skills.png", "prompt": "Hand-drawn doodle illustration, bold marker lines with organic rough edges, imperfect wobbly outlines, dry brush texture, warm color fills with slight color bleeding outside lines, light cream paper texture background, sketchbook aesthetic. A large hand-drawn letter 'T' in the center. The vertical bar (depth) is labeled '一个技术栈扎到底' with examples listed: '前端工程化', 'Python 后端', '数据工程'. The horizontal bar (breadth) is labeled '广泛涉猎' with examples: 'AI 工具', '产品设计', '开源社区'. At the intersection point, a star burst labeled '判断力 + 品味'. The overall feel is like a personal growth journal page. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
    {"id": "25", "file": "07-open-source-ladder.png", "prompt": "Flat vector illustration with unified black outline strokes, retro-soft color palette (muted teal, warm amber, dusty rose, soft sage), white background, clean educational textbook aesthetic, infographic style. Four ascending steps from left to right, forming a staircase. Step 1 (lowest): '读者' with book icon, label '阅读文档和源码', '学习最佳实践'. Step 2: '提问者' with question mark icon, label '提 Issue 描述问题', '参与讨论'. Step 3: '贡献者' with code icon, label '提交 PR 修复 bug', '完善文档'. Step 4 (highest): '维护者' with crown icon, label '审核 PR', '规划方向'. Each step is a different shade, getting brighter toward the top. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
    {"id": "26", "file": "07-security-redline.png", "prompt": "Flat vector illustration with unified black outline strokes, retro-soft color palette (muted teal, warm amber, dusty rose, soft sage), white background, clean educational textbook aesthetic, infographic style. A large red prohibition sign (circle with diagonal slash) as the central element. Inside and around the sign, four danger behaviors listed with warning icons: 1 '把 API Key 粘贴给 AI' with key icon, 2 '让 AI 处理用户隐私数据' with lock icon, 3 '让 AI 自动执行 rm -rf' with terminal warning icon, 4 '让 AI 自动安装未知依赖' with package warning icon. At the bottom, a bold banner: 'AI 是你的同事，不是你的朋友'. Color scheme is dominated by red, black, and white to convey seriousness. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
    {"id": "27", "file": "A-error-cheatsheet.png", "prompt": "Flat vector illustration with unified black outline strokes, retro-soft color palette (muted teal, warm amber, dusty rose, soft sage), white background, clean educational textbook aesthetic, infographic style. A card-based layout with 10 error type cards arranged in a grid. Each card contains: error name at top (e.g., 'SyntaxError', 'NameError', 'TypeError'), a small icon representing the error scenario, and a colored urgency tag at bottom: red for '紧急', yellow for '注意', green for '提示'. The cards have rounded corners and subtle shadows. Title at top: '常见错误速查表'. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
    {"id": "28", "file": "A-checklist-usage.png", "prompt": "Hand-drawn doodle illustration, bold marker lines with organic rough edges, imperfect wobbly outlines, dry brush texture, warm color fills with slight color bleeding outside lines, light cream paper texture background, sketchbook aesthetic. A person sitting at a desk checking items on a handwritten checklist. The checklist has 7 items with checkboxes, some checked with bold marker strokes. Next to the person, a hand-drawn progress bar showing '7/7 章完成'. At the bottom: '自检清单不是考试，是路标'. The overall mood is relaxed and encouraging, like a study diary page. All text labels must be in Chinese (Simplified). Minimal text, clean layout."},
]


def submit_task(task):
    """提交生成任务，返回 task_id"""
    url = f"{BASE_URL}/images/generations"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "gpt-image-2",
        "prompt": task["prompt"],
        "size": "1536x1024",
        "n": 1
    }
    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        if "id" in data:
            return {"success": True, "task": task, "task_id": data["id"], "raw": data}
        return {"success": False, "task": task, "error": f"No task id in response: {data}"}
    except Exception as e:
        return {"success": False, "task": task, "error": str(e)}


def poll_task(task_id):
    """轮询任务状态，返回结果"""
    url = f"{BASE_URL}/images/generations/{task_id}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    try:
        resp = requests.get(url, headers=headers, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def wait_for_task(result, max_wait=MAX_WAIT, interval=POLL_INTERVAL):
    """轮询等待任务完成"""
    task = result["task"]
    task_id = result["task_id"]
    waited = 0
    while waited < max_wait:
        status_data = poll_task(task_id)
        if "error" in status_data:
            return {**result, "final_error": status_data["error"]}
        status = status_data.get("status", "unknown")
        progress = status_data.get("progress", 0)
        print(f"    [{task['id']}] {task['file']}: status={status}, progress={progress}%")
        if status == "completed":
            # 获取图片 URL - 检查 result.data[0].url 格式
            if "result" in status_data and isinstance(status_data["result"], dict):
                result_inner = status_data["result"]
                if "data" in result_inner and len(result_inner["data"]) > 0:
                    img = result_inner["data"][0]
                    if "url" in img:
                        return {**result, "completed": True, "image_url": img["url"]}
                    if "b64_json" in img:
                        return {**result, "completed": True, "b64": img["b64_json"]}
                if "url" in result_inner:
                    return {**result, "completed": True, "image_url": result_inner["url"]}
            # 尝试其他格式
            if "data" in status_data and len(status_data["data"]) > 0:
                img = status_data["data"][0]
                if "url" in img:
                    return {**result, "completed": True, "image_url": img["url"]}
                if "b64_json" in img:
                    return {**result, "completed": True, "b64": img["b64_json"]}
            return {**result, "completed": True, "raw_result": status_data}
        if status in ("failed", "error", "cancelled"):
            return {**result, "completed": False, "final_error": f"Task ended with status: {status}"}
        time.sleep(interval)
        waited += interval
    return {**result, "completed": False, "final_error": f"Timeout after {max_wait}s"}


def download_image(url, filepath):
    """下载图片到本地"""
    try:
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
        with open(filepath, "wb") as f:
            f.write(resp.content)
        return {"success": True, "size": len(resp.content)}
    except Exception as e:
        return {"success": False, "error": str(e)}


def save_b64(b64_data, filepath):
    """保存 base64 图片"""
    import base64
    try:
        img_bytes = base64.b64decode(b64_data)
        with open(filepath, "wb") as f:
            f.write(img_bytes)
        return {"success": True, "size": len(img_bytes)}
    except Exception as e:
        return {"success": False, "error": str(e)}


def run_batch(batch_tasks, batch_num):
    """执行一批任务：提交 -> 轮询 -> 下载"""
    print(f"\n========== 第 {batch_num} 批 ({len(batch_tasks)} 张) ==========")

    # Step 1: 并发提交
    submitted = []
    print("  提交任务中...")
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(submit_task, t): t for t in batch_tasks}
        for future in as_completed(futures):
            task = futures[future]
            try:
                result = future.result()
                if result["success"]:
                    print(f"    [已提交] {task['id']} -> {task['file']} (task_id={result['task_id']})")
                    submitted.append(result)
                else:
                    print(f"    [提交失败] {task['id']} -> {task['file']}: {result.get('error', 'unknown')}")
                    submitted.append(result)
            except Exception as e:
                print(f"    [异常] {task['id']}: {e}")
                submitted.append({"success": False, "task": task, "error": str(e)})

    # Step 2: 轮询等待（串行轮询，避免过多请求）
    print("\n  轮询任务状态...")
    completed = []
    for result in submitted:
        if not result.get("success"):
            completed.append(result)
            continue
        final = wait_for_task(result)
        completed.append(final)

    # Step 3: 下载图片
    print("\n  下载图片...")
    for r in completed:
        task = r["task"]
        if not r.get("completed"):
            print(f"    [跳过] {task['file']}: 未完成或失败")
            continue
        filepath = OUTPUT_DIR / task["file"]
        if "image_url" in r:
            dl = download_image(r["image_url"], filepath)
        elif "b64" in r:
            dl = save_b64(r["b64"], filepath)
        else:
            dl = {"success": False, "error": "No image data"}

        if dl["success"]:
            size_kb = dl["size"] / 1024
            print(f"    [下载成功] {task['file']} ({size_kb:.1f} KB)")
            r["downloaded"] = True
            r["size"] = dl["size"]
        else:
            print(f"    [下载失败] {task['file']}: {dl['error']}")
            r["downloaded"] = False
            r["dl_error"] = dl["error"]

    return completed


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 分4批
    batch_size = 7
    batches = [TASKS[i:i+batch_size] for i in range(0, len(TASKS), batch_size)]

    all_results = []
    for i, batch in enumerate(batches, 1):
        batch_results = run_batch(batch, i)
        all_results.extend(batch_results)
        if i < len(batches):
            print(f"\n  第 {i} 批完成，等待 10 秒后继续下一批...")
            time.sleep(10)

    # 汇总报告
    print("\n========== 生成汇总 ==========")
    success = sum(1 for r in all_results if r.get("downloaded"))
    failed = len(all_results) - success
    print(f"总任务: {len(all_results)}")
    print(f"成功: {success}")
    print(f"失败: {failed}")

    if failed > 0:
        print("\n失败项:")
        for r in all_results:
            if not r.get("downloaded"):
                t = r["task"]
                err = r.get("error", r.get("final_error", r.get("dl_error", "unknown")))
                print(f"  {t['id']} {t['file']}: {err}")

    # 保存报告
    report_path = OUTPUT_DIR / "GENERATION-REPORT.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# 教材配图批量生成报告\n\n")
        f.write(f"## 生成时间\n{time.strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write(f"## 统计\n- 总任务: {len(all_results)}\n")
        f.write(f"- 成功: {success}\n")
        f.write(f"- 失败: {failed}\n")
        f.write(f"- 中文文字渲染问题: 待人工检查\n\n")
        f.write("## 成功文件列表\n")
        f.write("| 编号 | 文件名 | 大小 | 中文文字质量 |\n")
        f.write("|------|--------|------|-------------|\n")
        for r in all_results:
            if r.get("downloaded"):
                t = r["task"]
                size_kb = r.get("size", 0) / 1024
                f.write(f"| {t['id']} | {t['file']} | {size_kb:.1f} KB | 待检查 |\n")
        f.write("\n## 失败项\n")
        f.write("| 编号 | 失败原因 |\n|------|----------|\n")
        for r in all_results:
            if not r.get("downloaded"):
                t = r["task"]
                err = r.get("error", r.get("final_error", r.get("dl_error", "unknown")))
                f.write(f"| {t['id']} | {err} |\n")
        f.write("\n## 后续建议\n")
        f.write("- 需要后期替换文字的图: 待人工检查所有成功图片中的中文渲染质量\n")
        f.write("- 需要重新生成的图: 见上方失败项列表\n")

    print(f"\n报告已保存: {report_path}")


if __name__ == "__main__":
    main()
