#!/usr/bin/env python3
"""生成标准 Python Traceback 截图用于教材。"""

from PIL import Image, ImageDraw, ImageFont
import sys

def main():
    output_path = sys.argv[1] if len(sys.argv) > 1 else "traceback.png"

    width, height = 1200, 700
    bg_color = (30, 30, 30)
    text_color = (220, 220, 220)
    red_color = (255, 100, 100)
    yellow_color = (255, 220, 100)
    blue_color = (100, 180, 255)
    green_color = (100, 255, 150)
    comment_color = (150, 150, 150)

    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # 优先尝试支持中文的字体（必须支持中文标注）
    cn_font_paths = [
        "C:/Windows/Fonts/msyh.ttc",
        "C:/Windows/Fonts/msyhbd.ttc",
        "C:/Windows/Fonts/simhei.ttf",
        "C:/Windows/Fonts/simsun.ttc",
    ]
    # 英文等宽字体（用于 Traceback 代码，但若不支持中文会导致乱码）
    mono_font_paths = [
        "C:/Windows/Fonts/consola.ttf",
        "C:/Windows/Fonts/consolab.ttf",
        "C:/Windows/Fonts/cour.ttf",
        "C:/Windows/Fonts/Courier New.ttf",
        "C:/Windows/Fonts/lucon.ttf",
    ]
    font = None
    for fp in cn_font_paths + mono_font_paths:
        try:
            font = ImageFont.truetype(fp, 22)
            break
        except Exception:
            pass
    if font is None:
        font = ImageFont.load_default()

    # Title bar
    draw.rectangle([0, 0, width, 36], fill=(50, 50, 50))
    draw.text((20, 8), "hello.py - Python", fill=text_color, font=font)

    # Traceback lines
    lines = [
        ("Traceback (most recent call last):", comment_color),
        ('  File "hello.py", line 4, in <module>', yellow_color),
        ('    greet("Alice")', text_color),
        ('  File "hello.py", line 2, in greet', yellow_color),
        ('    print(message)', blue_color),
        ('          ^^^^^^^', red_color),
        ("NameError: name 'message' is not defined", red_color),
    ]

    x_start, y_start = 40, 70
    line_height = 36
    for i, (text, color) in enumerate(lines):
        y = y_start + i * line_height
        draw.text((x_start, y), text, fill=color, font=font)

    # Annotations
    # traceback 行 y 坐标: 行1=70, 行2=106, 行3=142, 行4=178, 行5=214, 行6=250, 行7=286
    annotations = [
        # 错误类型（红色）: 第7行 NameError, y=286
        {"box": [30, 280, 750, 325], "label": "错误类型", "color": red_color, "label_bg": (255, 230, 230)},
        # 出错文件和行号（黄色）: 第4行 File...line 2, y=178
        {"box": [30, 174, 500, 219], "label": "出错文件和行号", "color": yellow_color, "label_bg": (255, 250, 220)},
        # 出错的代码行（蓝色）: 第5行 print(message), y=214
        {"box": [30, 210, 350, 255], "label": "出错的代码行", "color": blue_color, "label_bg": (230, 245, 255)},
        # 错误详情（绿色）: 第1~3行 Traceback 开头, y=70~142
        {"box": [30, 66, 600, 147], "label": "错误详情", "color": green_color, "label_bg": (230, 255, 240)},
    ]

    for ann in annotations:
        draw.rectangle(ann["box"], outline=ann["color"], width=3)
        label_text = ann["label"]
        bbox = draw.textbbox((0, 0), label_text, font=font)
        label_w = bbox[2] - bbox[0] + 20
        label_h = 32
        label_x = ann["box"][2] + 15
        label_y = ann["box"][1] + (ann["box"][3] - ann["box"][1] - label_h) // 2
        draw.rectangle([label_x, label_y, label_x + label_w, label_y + label_h], fill=ann["label_bg"])
        draw.text((label_x + 10, label_y + 4), label_text, fill=(30, 30, 30), font=font)

    # Bottom instruction
    draw.text((40, 620), "阅读顺序：从下往上读", fill=comment_color, font=font)
    draw.text((40, 650), "（最下面的 NameError 是问题根源，往上追溯找到出错的代码行）", fill=comment_color, font=font)

    img.save(output_path, quality=95)
    print(f"Saved: {output_path}")

if __name__ == "__main__":
    main()
