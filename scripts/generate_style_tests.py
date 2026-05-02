#!/usr/bin/env python3
"""
9种风格「重庆大礼堂」配图批量生成脚本

适配 toapis.com 异步图像生成端点：
  1. POST /v1/images/generations  → 获取 task_id
  2. GET  /v1/images/generations/{task_id} → 轮询至 completed

用法：
  python scripts/generate_style_tests.py
"""

from __future__ import annotations

import os
import sys
import time
from pathlib import Path
from typing import Any

import requests

# ---------------------------------------------------------------------------
# 配置：从 .env 读取
# ---------------------------------------------------------------------------

def load_env(env_path: Path) -> dict[str, str]:
    """解析 KEY=VALUE 格式的 .env 文件。"""
    env: dict[str, str] = {}
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                env[key.strip()] = value.strip()
    return env


PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV = load_env(PROJECT_ROOT / ".env")

OPENAI_API_KEY = ENV.get("OPENAI_API_KEY", "")
OPENAI_BASE_URL = ENV.get("OPENAI_BASE_URL", "https://toapis.com/v1")
POLL_INTERVAL = 10   # 轮询间隔秒数
MAX_POLL_TIME = 600  # 最大轮询时间（10分钟）

OUTPUT_DIR = PROJECT_ROOT / "src" / "assets" / "images" / "style-tests"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# 9 种风格的英文 Prompt（从 prompts.md 提取，不含 negative prompt）
# ---------------------------------------------------------------------------
STYLE_TASKS: list[dict[str, Any]] = [
    {
        "id": "01-warm-cute",
        "prompt": (
            "Chongqing Great Hall of the People, iconic Chinese architecture with circular dome, "
            "three-tier red walls, golden glazed tiles, traditional Chinese palatial style, "
            "front-facing perspective, centered composition. Warm-cute illustration style, "
            "pastel color palette (coral pink #FF9AA2, sky blue #B5EAD7, mint green #C7CEEA), "
            "soft rounded shapes, large rounded corners on all elements, diffused soft shadows, "
            "cream white background #FFFEF9. Decorative elements: tiny stars and clouds with 0.2 opacity, "
            "playful scattered placement. Children's book illustration aesthetic, gentle and encouraging mood, "
            "no harsh lines, no dark colors, high brightness, vector-like clean edges with organic softness. "
            "16:9 horizontal composition."
        ),
        "size": "1536x1024",
    },
    {
        "id": "02-modern-minimal",
        "prompt": (
            "Chongqing Great Hall of the People, iconic Chinese architecture with circular dome, "
            "three-tier red walls, golden glazed tiles, traditional Chinese palatial style, "
            "front-facing perspective, centered composition. Modern minimal illustration style, "
            "geometric simplification, pure white background #FFFFFF, restrained color palette "
            "(deep indigo #6366F1, neutral gray #1F2937, subtle gold accent). Small rounded corners (4-8px), "
            "subtle micro-shadows (0 2px 4px rgba(0,0,0,0.04)), grid-aligned elements. "
            "Clean geometric sans-serif aesthetic, high contrast (WCAG AAA), professional and efficient mood, "
            "no decoration, no organic shapes, no gradients, flat design with precise geometry. "
            "16:9 horizontal composition."
        ),
        "size": "1536x1024",
    },
    {
        "id": "03-tech-future",
        "prompt": (
            "Chongqing Great Hall of the People, iconic Chinese architecture with circular dome, "
            "three-tier red walls, golden glazed tiles, traditional Chinese palatial style, "
            "front-facing perspective, centered composition. Tech-future illustration style, "
            "deep blue and purple gradient accents (#1E3A5F to #6366F1), cyan highlights (#06B6D4), "
            "subtle dot-grid decoration in background, geometric simplification. Pure white or very light gray "
            "background #F9FAFB, small rounded corners (4-8px), micro-shadows, clean geometric lines. "
            "Digital aesthetic, AI-inspired subtle glow effects on edges, futuristic yet professional, "
            "no photorealism, flat vector with tech accents. 16:9 horizontal composition."
        ),
        "size": "1536x1024",
    },
    {
        "id": "04-business-pro",
        "prompt": (
            "Chongqing Great Hall of the People, iconic Chinese architecture with circular dome, "
            "three-tier red walls, golden glazed tiles, traditional Chinese palatial style, "
            "front-facing perspective, centered composition. Business professional illustration style, "
            "corporate color palette (deep navy #1F2937, forest green #059669, neutral gray #6B7280, "
            "restrained gold accent). Geometric simplification, pure white background #FFFFFF, "
            "minimal geometric line decorations, grid-aligned. Small rounded corners (6-8px), subtle shadows, "
            "high contrast, trustworthy and stable mood. Clean infographic aesthetic, no gradients, "
            "no playful elements, strictly professional. 16:9 horizontal composition."
        ),
        "size": "1536x1024",
    },
    {
        "id": "05-premium-black-gold",
        "prompt": (
            "Chongqing Great Hall of the People, iconic Chinese architecture with circular dome, "
            "three-tier red walls, golden glazed tiles, traditional Chinese palatial style, "
            "front-facing perspective, centered composition. Premium black-gold illustration style, "
            "dark background #1A1A1A or deep charcoal, gold line art details #D4AF37, "
            "subtle gold gradient accents. Minimalist luxury aesthetic, thin precise geometric lines, "
            "small rounded corners (4-6px), very subtle depth. Elegant and sophisticated mood, "
            "high-end brand feeling, no clutter, restrained decoration (<3% area), "
            "matte black with metallic gold contrast. 16:9 horizontal composition."
        ),
        "size": "1536x1024",
    },
    {
        "id": "06-flat-illustration",
        "prompt": (
            "Chongqing Great Hall of the People, iconic Chinese architecture with circular dome, "
            "three-tier red walls, golden glazed tiles, traditional Chinese palatial style, "
            "front-facing perspective, centered composition. Flat illustration style, solid color blocks "
            "with no gradients and no shadows, geometric simplification of architectural details, "
            "bold and clean shapes. Color palette: vibrant but flat red #E63946 for walls, "
            "flat gold #F4A261 for tiles, flat sky blue #A8DADC for background, flat cream #F1FAEE for highlights. "
            "No texture, no shading, no depth, pure 2D vector aesthetic, clean edges, minimal detail, "
            "modern UI illustration style, infographic look. 16:9 horizontal composition."
        ),
        "size": "1536x1024",
    },
    {
        "id": "07-isometric",
        "prompt": (
            "Chongqing Great Hall of the People, iconic Chinese architecture with circular dome, "
            "three-tier red walls, golden glazed tiles, traditional Chinese palatial style. "
            "Isometric 3D illustration style, 30-degree axonometric projection, no perspective distortion "
            "(parallel lines stay parallel), building shown from front-top-right angle with visible roof "
            "and three wall tiers. Solid 3D blocks with subtle flat shading to show depth, "
            "clean geometric construction, miniature model aesthetic. Color palette: warm red walls #C0392B, "
            "golden roof #F1C40F, soft gray ground plane #ECF0F1, light blue sky gradient background. "
            "No photorealistic textures, stylized 3D, game asset look, clean vector-like 3D render. "
            "16:9 horizontal composition."
        ),
        "size": "1536x1024",
    },
    {
        "id": "08-hand-drawn-doodle",
        "prompt": (
            "Chongqing Great Hall of the People, iconic Chinese architecture with circular dome, "
            "three-tier red walls, golden glazed tiles, traditional Chinese palatial style, "
            "front-facing perspective, centered composition. Hand-drawn doodle illustration style, "
            "bold marker lines with organic rough edges, imperfect wobbly outlines, chunky brush-pen strokes, "
            "dry brush texture with tiny ink gaps. Warm color fills (red walls, gold roof) with slight "
            "color bleeding outside lines, white or light cream paper texture background. "
            "Playful and approachable mood, sketchbook aesthetic, slightly childlike but charming, "
            "no perfect geometry, natural line weight variation, warm handmade feel. 16:9 horizontal composition."
        ),
        "size": "1536x1024",
    },
    {
        "id": "09-line-art",
        "prompt": (
            "Chongqing Great Hall of the People, iconic Chinese architecture with circular dome, "
            "three-tier red walls, golden glazed tiles, traditional Chinese palatial style, "
            "front-facing perspective, centered composition. Pure line art illustration style, "
            "black ink lines on pure white background, no color fill, no shading, no gradients. "
            "Varied line weight: bold outlines for main structure, medium lines for architectural details, "
            "thin lines for decorative patterns. Clean and precise ink drawing aesthetic, "
            "technical illustration feel, suitable for black-and-white print. Crisp edges, "
            "high contrast between black lines and white paper, elegant contour drawing, "
            "architectural blueprint inspiration. 16:9 horizontal composition."
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


def poll_task(task_id: str, api_key: str, base_url: str, max_wait: int = 600, interval: int = 10) -> tuple[bool, str]:
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
        print("错误: 未在 .env 中找到 OPENAI_API_KEY")
        return 1

    print("=" * 60)
    print("9种风格「重庆大礼堂」配图批量生成")
    print(f"端点: {OPENAI_BASE_URL}")
    print(f"输出目录: {OUTPUT_DIR}")
    print(f"任务数: {len(STYLE_TASKS)}")
    print("=" * 60)
    print()

    # -----------------------------------------------------------------------
    # Phase 1: 顺序提交所有任务
    # -----------------------------------------------------------------------
    print("[Phase 1] 提交任务...")
    submitted: dict[str, str] = {}  # img_id -> task_id
    sync_urls: dict[str, str] = {}  # img_id -> url（同步返回）
    results: list[tuple[str, bool, str]] = []

    for task in STYLE_TASKS:
        img_id, task_id, ok, msg = submit_task(task, OPENAI_API_KEY, OPENAI_BASE_URL)
        if ok and task_id:
            submitted[img_id] = task_id
            print(f"  [OK] {img_id}: {msg}")
        elif ok and not task_id:
            # 同步返回了 URL
            sync_urls[img_id] = msg.replace("同步返回: ", "")
            print(f"  [OK] {img_id}: {msg}")
        else:
            print(f"  [FAIL] {img_id}: {msg}")
            results.append((img_id, False, msg))

    # -----------------------------------------------------------------------
    # Phase 2: 轮询所有异步任务状态
    # -----------------------------------------------------------------------
    completed_urls: dict[str, str] = {}  # img_id -> url
    completed_urls.update(sync_urls)

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
    # Phase 3: 下载所有完成的图片
    # -----------------------------------------------------------------------
    if completed_urls:
        print(f"\n[Phase 3] 下载图片... ({len(completed_urls)} 张)")
        for img_id, url in completed_urls.items():
            img_id, ok, msg = download_image(img_id, url, OUTPUT_DIR)
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

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
