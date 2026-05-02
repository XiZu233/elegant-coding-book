"""一次性 PNG 压缩脚本（Pillow 12.x），原地处理 src/assets/images/ 下大于阈值的 PNG。"""
from __future__ import annotations
from pathlib import Path
from PIL import Image

IMAGES_DIR = Path("src/assets/images")
SIZE_THRESHOLD_BYTES = 800 * 1024  # 仅处理 > 800KB 的图
SKIP_SUBDIRS = {"screenshots", "skill-tests", "style-tests", "archive"}


def compress_one(path: Path) -> tuple[int, int, str]:
    """返回 (原大小, 新大小, 模式标记)。失败时抛异常。"""
    original_size = path.stat().st_size
    with Image.open(path) as img:
        mode = img.mode
        # 保持模式：RGBA 走原模式 optimize；RGB 走 256 色调色板量化
        if mode in ("RGB", "L"):
            quantized = img.quantize(colors=256, method=Image.Quantize.MEDIANCUT)
            quantized.save(path, format="PNG", optimize=True)
            tag = "P"
        elif mode == "RGBA":
            # 保留透明通道，仅 optimize 重新编码
            img.save(path, format="PNG", optimize=True, compress_level=9)
            tag = "RGBA"
        elif mode == "P":
            img.save(path, format="PNG", optimize=True)
            tag = "P-keep"
        else:
            converted = img.convert("RGB").quantize(colors=256)
            converted.save(path, format="PNG", optimize=True)
            tag = f"{mode}->P"
    new_size = path.stat().st_size
    return original_size, new_size, tag


def fmt_kb(n: int) -> str:
    return f"{n / 1024:>8.1f} KB"


def main() -> None:
    candidates = sorted(
        p for p in IMAGES_DIR.glob("*.png")
        if p.is_file()
        and p.stat().st_size > SIZE_THRESHOLD_BYTES
        and not any(s in p.parts for s in SKIP_SUBDIRS)
    )
    print(f"找到 {len(candidates)} 张待压缩 PNG（> {SIZE_THRESHOLD_BYTES // 1024} KB）\n")
    print(f"{'文件名':<35} {'原':>10} {'新':>10} {'节省':>8} {'模式':<10}")
    print("-" * 78)

    total_original = total_new = 0
    failures: list[tuple[Path, Exception]] = []

    for path in candidates:
        try:
            orig, new, tag = compress_one(path)
            saved_pct = (1 - new / orig) * 100
            total_original += orig
            total_new += new
            print(f"{path.name:<35} {fmt_kb(orig)} {fmt_kb(new)} {saved_pct:>6.1f}% {tag:<10}")
        except Exception as exc:
            failures.append((path, exc))
            print(f"{path.name:<35} {'FAILED':>10} {repr(exc)[:40]}")

    print("-" * 78)
    if total_original:
        total_saved = (1 - total_new / total_original) * 100
        print(f"总计: {fmt_kb(total_original)} -> {fmt_kb(total_new)}  节省 {total_saved:.1f}%")
    if failures:
        print(f"\n{len(failures)} 张失败，详情:")
        for p, e in failures:
            print(f"  {p}: {e}")


if __name__ == "__main__":
    main()
