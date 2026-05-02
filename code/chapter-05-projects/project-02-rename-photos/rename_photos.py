# rename_photos.py
# 批量重命名照片
# 按文件修改日期分组，重命名为 "YYYY-MM-DD-001.jpg" 格式
# 只用 Python 标准库，无需安装第三方包

import os
import time
from pathlib import Path
from collections import defaultdict


def rename_photos(folder_path, prefix=""):
    """
    批量重命名照片，按修改日期分组编号

    参数:
        folder_path: 照片所在文件夹
        prefix: 文件名前缀，例如 "旅行-"
    """
    folder = Path(folder_path)

    if not folder.exists():
        print(f"错误：文件夹不存在 -> {folder}")
        return

    # 支持的图片扩展名
    photo_exts = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

    # 收集所有图片文件
    photos = []
    for item in folder.iterdir():
        if item.is_file() and item.suffix.lower() in photo_exts:
            photos.append(item)

    if not photos:
        print("没有找到图片文件。")
        return

    # 按修改日期分组
    # defaultdict(list) 的意思是：如果某个日期还没有记录，自动创建一个空列表
    date_groups = defaultdict(list)

    for photo in photos:
        # 获取文件的修改时间戳（秒数）
        mtime = photo.stat().st_mtime
        # 把时间戳转成 "YYYY-MM-DD" 格式的字符串
        date_str = time.strftime("%Y-%m-%d", time.localtime(mtime))
        date_groups[date_str].append(photo)

    # 准备重命名计划
    renames = []  # 存储 (原路径, 新路径) 的列表

    for date_str, files in date_groups.items():
        # 按文件名排序，保证编号顺序稳定
        files.sort()

        for index, photo in enumerate(files, start=1):
            # 如果有前缀，加到日期前面
            if prefix:
                new_name = f"{prefix}-{date_str}-{index:03d}{photo.suffix.lower()}"
            else:
                new_name = f"{date_str}-{index:03d}{photo.suffix.lower()}"
            new_path = folder / new_name

            # 处理重名：如果新文件名已存在且不是当前文件自己
            counter = 1
            while new_path.exists() and new_path != photo:
                if prefix:
                    new_name = f"{prefix}-{date_str}-{index:03d}_{counter}{photo.suffix.lower()}"
                else:
                    new_name = f"{date_str}-{index:03d}_{counter}{photo.suffix.lower()}"
                new_path = folder / new_name
                counter += 1

            renames.append((photo, new_path))

    # 预览
    print("=" * 60)
    print("即将重命名以下文件：")
    print("=" * 60)
    for old, new in renames:
        print(f"  {old.name:35s} -> {new.name}")
    print("=" * 60)
    print(f"共 {len(renames)} 个文件")

    # 确认
    confirm = input("\n确认执行吗？输入 y 继续，输入 n 取消: ").strip().lower()
    if confirm != "y":
        print("已取消操作。")
        return

    # 执行重命名
    for old, new in renames:
        os.rename(str(old), str(new))
        print(f"已重命名: {old.name} -> {new.name}")

    print("\n重命名完成！")


if __name__ == "__main__":
    # 默认处理当前文件夹，你也可以改成指定路径
    # 例如：folder = Path(r"C:\Users\你的用户名\Pictures\相机照片")
    folder = Path.cwd()  # cwd() = current working directory，即当前文件夹

    # 询问用户是否添加前缀
    user_prefix = input("请输入文件名前缀（直接回车表示不添加）: ").strip()

    print(f"目标文件夹: {folder}\n")
    rename_photos(folder, prefix=user_prefix)
