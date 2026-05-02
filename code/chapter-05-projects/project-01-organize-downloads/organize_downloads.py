# organize_downloads.py
# 自动整理下载文件夹
# 按文件类型（图片/文档/压缩包/其他）分类移动到子文件夹
# 只用 Python 标准库，无需安装第三方包

import shutil
from pathlib import Path


def organize_downloads(downloads_path, dry_run=False):
    """
    整理下载文件夹，按文件类型分类到子文件夹

    参数:
        downloads_path: 下载文件夹的路径
        dry_run: 如果为 True，只预览不真正移动文件
    """
    # 定义分类规则：文件夹名称 -> 对应的文件扩展名列表
    categories = {
        "图片": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".ico"],
        "文档": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".md"],
        "压缩包": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    }

    # 将 downloads_path 转成 Path 对象，方便后续操作
    downloads = Path(downloads_path)

    # 如果下载文件夹不存在，提示并退出
    if not downloads.exists():
        print(f"错误：文件夹不存在 -> {downloads}")
        return

    # 先收集所有需要移动的文件信息（预览阶段）
    moves = []  # 存储 (原路径, 目标路径, 分类名) 的列表

    for item in downloads.iterdir():
        # 跳过文件夹本身，只处理文件
        if not item.is_file():
            continue

        # 获取文件扩展名（例如 .jpg），并转成小写方便匹配
        ext = item.suffix.lower()

        # 判断文件属于哪个分类
        target_folder = "其他"  # 默认归类到"其他"
        for folder_name, extensions in categories.items():
            if ext in extensions:
                target_folder = folder_name
                break

        # 构建目标文件的完整路径
        target_path = downloads / target_folder
        dest = target_path / item.name

        # 如果目标位置已经有同名文件，在文件名后面加数字避免覆盖
        counter = 1
        original_dest = dest
        while dest.exists():
            # 分离文件名和扩展名，例如 "report.pdf" -> "report", ".pdf"
            stem = original_dest.stem
            suffix = original_dest.suffix
            dest = target_path / f"{stem}_{counter}{suffix}"
            counter += 1

        moves.append((item, dest, target_folder))

    # 如果没有文件需要移动
    if not moves:
        print("没有需要整理的文件。")
        return

    # 显示预览
    print("=" * 50)
    print("即将执行以下操作：")
    print("=" * 50)
    for src, dest, folder in moves:
        print(f"  {src.name:30s} -> {folder}/{dest.name}")
    print("=" * 50)
    print(f"共 {len(moves)} 个文件")

    # 如果是预览模式，到此结束
    if dry_run:
        print("\n(这是预览模式，没有真正移动任何文件)")
        return

    # 询问确认
    confirm = input("\n确认执行吗？输入 y 继续，输入 n 取消: ").strip().lower()
    if confirm != "y":
        print("已取消操作。")
        return

    # 执行移动
    for src, dest, folder in moves:
        dest.parent.mkdir(exist_ok=True)  # 确保目标文件夹存在
        shutil.move(str(src), str(dest))
        print(f"已移动: {src.name} -> {folder}/{dest.name}")

    print("\n整理完成！")


if __name__ == "__main__":
    # 获取当前用户的下载文件夹路径
    # Windows 上通常是 C:\Users\用户名\Downloads
    downloads_dir = Path.home() / "Downloads"

    print(f"目标文件夹: {downloads_dir}\n")
    organize_downloads(downloads_dir)
