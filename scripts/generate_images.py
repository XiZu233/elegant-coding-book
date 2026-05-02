#!/usr/bin/env python3
"""
教材配图批量生成脚本（异步并发版）

适配 toapis.com 等异步图像生成端点：
  1. POST /v1/images/generations  → 获取 task_id
  2. GET  /v1/images/generations/{task_id} → 轮询至 completed

用法：
  export OPENAI_API_KEY="sk-xxx"
  export OPENAI_BASE_URL="https://toapis.com/v1"
  python scripts/generate_images.py
"""

from __future__ import annotations

import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

import requests

# ---------------------------------------------------------------------------
# 配置（环境变量优先）
# ---------------------------------------------------------------------------
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL", "https://toapis.com/v1")
MAX_WORKERS = int(os.environ.get("MAX_WORKERS", "5"))
POLL_INTERVAL = int(os.environ.get("POLL_INTERVAL", "10"))  # 轮询间隔秒数
MAX_POLL_TIME = int(os.environ.get("MAX_POLL_TIME", "300"))  # 最大轮询时间

PROJECT_ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = PROJECT_ROOT / "src" / "assets" / "images"
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# 配图任务（附录D中提取的10张概念插图）
# ---------------------------------------------------------------------------
IMAGE_TASKS: list[dict[str, Any]] = [
    {
        "id": "00-traditional-vs-ai",
        "prompt": (
            "A split-screen flat illustration comparing Traditional Programming vs AI Programming. "
            "Left side: a stressed person drowning in lines of chaotic code on multiple monitors, dark blue tone, labeled 'Traditional'. "
            "Right side: a relaxed person speaking naturally to a friendly robot assistant that writes clean code, bright warm orange tone, labeled 'AI Programming'. "
            "A large curved arrow in the middle points from left to right labeled 'Paradigm Shift'. "
            "Clean infographic style, minimal text, white background, vector aesthetic, no fine details."
        ),
        "size": "1536x1024",
    },
    {
        "id": "06-docker-container",
        "prompt": (
            "A flat illustration showing Docker container concept as a shipping metaphor. "
            "Left: a laptop with scattered app icons and dependency gears in chaos. "
            "Middle: a large shipping container encapsulating app + runtime + dependencies + config into one neat sealed box. "
            "Right: another laptop opening the same container, app runs identically. "
            "Soft blue and orange palette, white background, clean infographic style, minimal text labels, vector aesthetic."
        ),
        "size": "1536x1024",
    },
    {
        "id": "07-ai-security-redline",
        "prompt": (
            "A bold warning infographic for AI security red lines. "
            "A large red prohibition sign (circle with diagonal slash) in the center. "
            "Around it: four danger icons — (1) a key token, (2) a user profile with privacy lock, "
            "(3) a terminal window with danger symbol, (4) a mysterious package box with question mark. "
            "Bold red and dark gray colors, white background, flat vector illustration, minimal text."
        ),
        "size": "1536x1024",
    },
    {
        "id": "07-t-shaped-skills",
        "prompt": (
            "An infographic of a T-shaped skills model. A large letter 'T' in the center. "
            "The vertical bar represents 'Depth' with icons for coding and engineering. "
            "The horizontal bar represents 'Breadth' with icons for AI tools, product design, and community. "
            "The intersection glows with 'Judgment + Taste'. "
            "Clean minimal style, soft purple and teal colors, white background, flat vector illustration, no fine text."
        ),
        "size": "1536x1024",
    },
    {
        "id": "06-virtual-environment",
        "prompt": (
            "A flat illustration comparing global vs virtual environment. "
            "Left side: a single messy room with all Python packages piled in chaos, labeled 'Global'. "
            "Right side: three clean separate rooms, each with its own Python and packages neatly arranged, labeled 'Virtual Environments'. "
            "Soft green and blue palette, white background, clean infographic style, minimal text, vector aesthetic."
        ),
        "size": "1536x1024",
    },
    {
        "id": "07-open-source-ladder",
        "prompt": (
            "A 4-step ascending ladder infographic for open-source community participation. "
            "Step 1 (bottom): Reader with book icon. "
            "Step 2: Questioner with question-mark icon. "
            "Step 3: Contributor with code icon. "
            "Step 4 (top): Maintainer with crown icon. "
            "Each step wider and brighter ascending. Warm orange and gold tones, white background, minimal text, clean vector look."
        ),
        "size": "1536x1024",
    },
    {
        "id": "06-http-request-response",
        "prompt": (
            "A clean diagram showing HTTP request-response cycle. "
            "Left: a client device (browser/phone). Right: a server rack. "
            "Top arrow from client to server labeled 'Request'. "
            "Bottom arrow from server to client labeled 'Response'. "
            "Small package icons on arrows representing JSON data. "
            "Blue and green colors, white background, flat infographic style, minimal text, vector aesthetic."
        ),
        "size": "1536x1024",
    },
    {
        "id": "04-context-window",
        "prompt": (
            "An illustration of Context Window as a transparent container. "
            "A rectangular glass box labeled 'Context Window' filled with colored blocks: "
            "conversation history (blue), file contents (green), command output (yellow), system instructions (purple). "
            "A small orange warning sign on the right edge. "
            "Below: four tool icons — trash can, compress, speech bubble, clone. "
            "Soft blue and gray tones, white background, clean flat design, minimal text, vector style."
        ),
        "size": "1536x1024",
    },
    {
        "id": "04-agent-loop",
        "prompt": (
            "A circular loop infographic showing the Agentic Loop cycle with three stages. "
            "Top: 'Explore' with magnifying glass icon. "
            "Right: 'Act' with hammer/tool icon. "
            "Left: 'Validate' with checkmark icon. "
            "Curved arrows connecting them in a clockwise cycle. "
            "Outside the circle: text 'Auto-adjust iterations based on task complexity'. "
            "Soft blue and green palette, white background, clean flat vector style, minimal text."
        ),
        "size": "1536x1024",
    },
    {
        "id": "02-function-lego",
        "prompt": (
            "A flat illustration showing function decomposition as LEGO bricks. "
            "Left: a large messy tangled code blob labeled 'Monolithic'. "
            "Middle: an arrow pointing right labeled 'Split into Functions'. "
            "Right: 4 clean colorful LEGO bricks stacked neatly, each representing a function — 'get_input', 'calculate', 'format_output', 'save_result'. "
            "Bright playful colors, white background, clean infographic style, minimal text, vector aesthetic."
        ),
        "size": "1536x1024",
    },
]


# ---------------------------------------------------------------------------
# 异步任务操作
# ---------------------------------------------------------------------------

def submit_task(task: dict[str, Any], api_key: str, base_url: str) -> tuple[str, str, bool, str]:
    """提交生成任务，返回 (img_id, task_id, success, message)。"""
    img_id = task["id"]
    prompt = task["prompt"]
    size = task.get("size", "1024x1024")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "gpt-image-2",
        "prompt": prompt,
        "size": size,
        "n": 1,
    }

    url = f"{base_url.rstrip('/')}/images/generations"
    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=30)
        resp.raise_for_status()
        data = resp.json()

        if "id" in data:
            return (img_id, data["id"], True, f"已提交 task={data['id']}")
        if "data" in data and len(data["data"]) > 0:
            # 同步返回（兼容标准OpenAI格式）
            return (img_id, "", True, f"同步返回: {data['data'][0].get('url', 'N/A')}")
        return (img_id, "", False, f"未知响应: {data}")

    except requests.exceptions.HTTPError as exc:
        return (img_id, "", False, f"HTTP {exc.response.status_code}: {exc.response.text[:200]}")
    except Exception as exc:
        return (img_id, "", False, f"异常: {exc}")


def poll_task(task_id: str, api_key: str, base_url: str, max_wait: int = 300, interval: int = 10) -> tuple[bool, str]:
    """轮询任务状态直到完成或超时。返回 (success, url_or_message)。"""
    headers = {"Authorization": f"Bearer {api_key}"}
    url = f"{base_url.rstrip('/')}/images/generations/{task_id}"

    elapsed = 0
    while elapsed < max_wait:
        try:
            resp = requests.get(url, headers=headers, timeout=30)
            resp.raise_for_status()
            data = resp.json()

            status = data.get("status", "")
            if status == "completed":
                result = data.get("result", {})
                if result.get("type") == "image" and result.get("data"):
                    return (True, result["data"][0]["url"])
                return (True, data.get("data", [{}])[0].get("url", ""))
            if status in ("failed", "error"):
                return (False, f"任务失败: {data}")

            time.sleep(interval)
            elapsed += interval

        except requests.exceptions.HTTPError as exc:
            return (False, f"HTTP {exc.response.status_code}: {exc.response.text[:200]}")
        except Exception as exc:
            return (False, f"异常: {exc}")

    return (False, f"轮询超时 ({max_wait}s)")


def download_image(img_id: str, image_url: str, output_dir: Path) -> tuple[str, bool, str]:
    """下载图片到本地。返回 (img_id, success, message)。"""
    output_path = output_dir / f"{img_id}.png"
    try:
        resp = requests.get(image_url, timeout=60)
        resp.raise_for_status()
        output_path.write_bytes(resp.content)
        return (img_id, True, f"已保存 {output_path.name} ({len(resp.content)} bytes)")
    except Exception as exc:
        return (img_id, False, f"下载失败: {exc}")


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------

def main() -> int:
    if not OPENAI_API_KEY:
        print("错误: 未设置 OPENAI_API_KEY 环境变量")
        return 1

    print("=" * 60)
    print("教材配图批量生成脚本（异步并发版）")
    print(f"端点: {OPENAI_BASE_URL}")
    print(f"输出目录: {IMAGES_DIR}")
    print(f"并发数: {MAX_WORKERS}")
    print(f"任务数: {len(IMAGE_TASKS)}")
    print("=" * 60)
    print()

    # -----------------------------------------------------------------------
    # Phase 1: 并发提交所有任务
    # -----------------------------------------------------------------------
    print("[Phase 1] 提交任务...")
    submitted: dict[str, str] = {}  # img_id -> task_id
    results: list[tuple[str, bool, str]] = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {
            executor.submit(submit_task, task, OPENAI_API_KEY, OPENAI_BASE_URL): task
            for task in IMAGE_TASKS
        }
        for future in as_completed(futures):
            img_id, task_id, ok, msg = future.result()
            if ok and task_id:
                submitted[img_id] = task_id
                print(f"  [OK] {img_id}: {msg}")
            else:
                print(f"  [FAIL] {img_id}: {msg}")
                results.append((img_id, False, msg))

    if not submitted:
        print("\n没有成功提交的任务，退出。")
        return 1

    print(f"\n已提交 {len(submitted)} 个任务，等待生成完成...")

    # -----------------------------------------------------------------------
    # Phase 2: 轮询所有任务状态
    # -----------------------------------------------------------------------
    completed_urls: dict[str, str] = {}  # img_id -> url
    pending = dict(submitted)
    elapsed = 0

    while pending and elapsed < MAX_POLL_TIME:
        print(f"\n[Phase 2] 轮询中... 剩余 {len(pending)} 个任务 ({elapsed}s/{MAX_POLL_TIME}s)")
        newly_done: list[str] = []

        for img_id, task_id in list(pending.items()):
            ok, result = poll_task(task_id, OPENAI_API_KEY, OPENAI_BASE_URL, max_wait=5, interval=0)
            if ok and result:
                completed_urls[img_id] = result
                newly_done.append(img_id)
                print(f"  [DONE] {img_id}: {result[:60]}...")
            elif not ok and "超时" not in result:
                # 真正失败了
                results.append((img_id, False, result))
                newly_done.append(img_id)
                print(f"  [FAIL] {img_id}: {result}")

        for img_id in newly_done:
            pending.pop(img_id, None)

        if pending:
            time.sleep(POLL_INTERVAL)
            elapsed += POLL_INTERVAL

    # 处理超时未完成的任务
    for img_id in pending:
        results.append((img_id, False, "轮询超时"))

    # -----------------------------------------------------------------------
    # Phase 3: 并发下载所有完成的图片
    # -----------------------------------------------------------------------
    if completed_urls:
        print(f"\n[Phase 3] 下载图片... ({len(completed_urls)} 张)")
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = {
                executor.submit(download_image, img_id, url, IMAGES_DIR): img_id
                for img_id, url in completed_urls.items()
            }
            for future in as_completed(futures):
                img_id, ok, msg = future.result()
                status = "OK" if ok else "FAIL"
                print(f"  [{status}] {img_id}: {msg}")
                results.append((img_id, ok, msg))

    # -----------------------------------------------------------------------
    # 汇总
    # -----------------------------------------------------------------------
    success_count = sum(1 for _, ok, _ in results if ok)
    fail_count = len(results) - success_count

    print()
    print("=" * 60)
    print(f"完成: 成功 {success_count} / 失败 {fail_count}")
    print("=" * 60)

    if success_count:
        print("\n在 Markdown 中的引用方式:")
        print("-" * 60)
        for img_id, ok, _ in results:
            if ok:
                print(f'![{img_id}](assets/images/{img_id}.png)')
        print("-" * 60)

    print("\n提示：确认图片效果后，执行以下命令同步到 GitHub:")
    print("  git add src/assets/images/*.png")
    print("  git commit -m 'Add AI-generated chapter illustrations'")
    print("  git push origin main")

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
