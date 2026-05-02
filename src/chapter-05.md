# 05 实战案例：和AI一起解决真实问题

这一章是两个完整的实战项目。你不需要安装任何第三方库，只用Python自带的工具就能完成。每个案例都包含完整的"和AI一起写"的对话流程——你可以直接复制提示词，跟着做。

---

# 案例一：自动整理下载文件夹

> [配图占位：此处应有项目目录树形图（Python CLI），详见附录D]

## 需求描述

你的"下载"文件夹是不是这样的：图片、PDF、压缩包、安装程序全混在一起，找文件得翻半天？

我们要写一个脚本，让它自动扫描下载文件夹，按文件类型分类：

- 图片（.jpg, .png, .gif 等）→ 移到 "图片" 文件夹
- 文档（.pdf, .docx, .txt 等）→ 移到 "文档" 文件夹
- 压缩包（.zip, .rar, .7z 等）→ 移到 "压缩包" 文件夹
- 其他文件 → 移到 "其他" 文件夹

## 和AI的对话过程

> [配图占位：此处应有 Plan Mode & Normal Mode 切换示意图，详见附录D]

### 第一轮：描述需求

**你输入的提示词：**

```text
我想写一个Python脚本，自动整理我的下载文件夹。

需求：
1. 扫描我的下载文件夹（Windows系统，路径是 C:\Users\我的用户名\Downloads）
2. 根据文件扩展名分类：
   - 图片：jpg, jpeg, png, gif, bmp, webp
   - 文档：pdf, doc, docx, txt, xls, xlsx, ppt, pptx
   - 压缩包：zip, rar, 7z, tar, gz
   - 其他：不属于以上三类的文件
3. 把文件移动到对应的子文件夹里（图片/文档/压缩包/其他）
4. 如果子文件夹不存在，自动创建
5. 只移动文件，不移动文件夹本身

请用Python标准库实现，不要需要pip安装任何第三方包。
我是零基础，请在代码里加上详细的中文注释，解释每一行在做什么。
```

**AI回复的代码：**

```python
import os
import shutil
from pathlib import Path


def organize_downloads(downloads_path):
    """
    整理下载文件夹，按文件类型分类到子文件夹
    """
    # 定义分类规则：文件夹名称 -> 对应的文件扩展名列表
    categories = {
        "图片": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
        "文档": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
        "压缩包": [".zip", ".rar", ".7z", ".tar", ".gz"],
    }

    # 将 downloads_path 转成 Path 对象，方便后续操作
    downloads = Path(downloads_path)

    # 如果下载文件夹不存在，提示并退出
    if not downloads.exists():
        print(f"错误：文件夹不存在 -> {downloads}")
        return

    # 遍历下载文件夹里的所有内容
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

        # 创建目标子文件夹（如果不存在）
        target_path = downloads / target_folder
        target_path.mkdir(exist_ok=True)

        # 构建目标文件的完整路径
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

        # 移动文件
        shutil.move(str(item), str(dest))
        print(f"已移动: {item.name} -> {target_folder}/{dest.name}")

    print("\n整理完成！")


if __name__ == "__main__":
    # 获取当前用户的下载文件夹路径
    # Windows 上通常是 C:\Users\用户名\Downloads
    downloads_dir = Path.home() / "Downloads"

    print(f"开始整理: {downloads_dir}")
    organize_downloads(downloads_dir)
```

### 第二轮：运行验证

**你的操作：**

1. 打开记事本，把上面的代码复制进去
2. 保存为 `organize_downloads.py`（注意后缀名是 `.py`，不是 `.txt`）
3. 打开命令提示符（按 `Win+R`，输入 `cmd`，回车）
4. 输入以下命令运行：

```bash
python organize_downloads.py
```

**运行结果示例：**

```
开始整理: C:\Users\你的用户名\Downloads
已移动: 照片.jpg -> 图片/照片.jpg
已移动: 报告.pdf -> 文档/报告.pdf
已移动: 资料.zip -> 压缩包/资料.zip
已移动: setup.exe -> 其他/setup.exe
已移动: 笔记.txt -> 文档/笔记.txt

整理完成！
```

### 第三轮：发现问题，迭代优化

你运行后发现一个问题：有些文件被错误分类了。比如 `.doc` 文件被归到了"其他"。

**你输入的提示词：**

```text
我运行了上面的代码，发现 .doc 文件没有被正确归类到"文档"文件夹，而是去了"其他"。
帮我检查一下代码，找出原因并修复。

另外，我希望增加一个功能：在移动文件之前，先显示一个预览列表，告诉我哪些文件会被移动到哪里，然后问我"确认执行吗？(y/n)"，确认后再真正移动。这样更安全。
```

**AI修复后的代码：**

```python
import os
import shutil
from pathlib import Path


def organize_downloads(downloads_path, dry_run=False):
    """
    整理下载文件夹，按文件类型分类到子文件夹
    
    参数:
        downloads_path: 下载文件夹的路径
        dry_run: 如果为 True，只预览不真正移动文件
    """
    # 定义分类规则
    categories = {
        "图片": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".ico"],
        "文档": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".md"],
        "压缩包": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    }

    downloads = Path(downloads_path)

    if not downloads.exists():
        print(f"错误：文件夹不存在 -> {downloads}")
        return

    # 先收集所有需要移动的文件信息（预览阶段）
    moves = []  # 存储 (原路径, 目标路径, 分类名) 的列表

    for item in downloads.iterdir():
        if not item.is_file():
            continue

        ext = item.suffix.lower()

        # 判断分类
        target_folder = "其他"
        for folder_name, extensions in categories.items():
            if ext in extensions:
                target_folder = folder_name
                break

        target_path = downloads / target_folder
        dest = target_path / item.name

        # 处理重名
        counter = 1
        original_dest = dest
        while dest.exists():
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
    downloads_dir = Path.home() / "Downloads"
    print(f"目标文件夹: {downloads_dir}\n")
    organize_downloads(downloads_dir)
```

### 第四轮：再次运行

```bash
python organize_downloads.py
```

这次你会先看到预览列表，确认后才真正执行。更安全、更可控。

## 小结：你学到了什么

1. **用 `pathlib.Path` 处理文件路径**——比直接用字符串拼接更可靠，自动适配 Windows 和 macOS/Linux
2. **用 `shutil.move` 移动文件**——Python 标准库自带，不需要额外安装
3. **先预览、再执行**——对可能修改数据的脚本，加一个确认步骤是良好的安全习惯
4. **和AI协作的迭代流程**——先做出能用的，发现问题再优化，而不是一次性追求完美

---

# 案例二：批量重命名照片

> [配图占位：此处应有项目目录树形图（Next.js 仪表盘），详见附录D]

## 需求描述

从相机或手机导出的照片，文件名通常是一串无意义的数字，比如 `IMG_20240115_143022.jpg`、`DSC_0001.jpg`。你想把它们改成有意义的格式，比如按日期编号：`2024-01-15-001.jpg`、`2024-01-15-002.jpg`。

## 和AI的对话过程

### 第一轮：描述需求

**你输入的提示词：**

```text
我想写一个Python脚本，批量重命名照片文件。

需求：
1. 扫描指定文件夹里的所有图片文件（jpg, jpeg, png）
2. 读取每张照片的"修改日期"（不是文件名里的日期，而是文件属性里的修改时间）
3. 按日期分组：同一天的照片归为一组
4. 每组按顺序编号，重命名为 "YYYY-MM-DD-001.jpg" 这样的格式
5. 如果目标文件名已存在，自动加序号避免覆盖
6. 同样先预览、确认后再执行

请用Python标准库实现，加详细中文注释。我是零基础。
```

**AI回复的代码：**

```python
import os
import time
from pathlib import Path
from collections import defaultdict


def rename_photos(folder_path):
    """
    批量重命名照片，按修改日期分组编号
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
            # 生成新文件名：日期-三位编号.扩展名
            new_name = f"{date_str}-{index:03d}{photo.suffix.lower()}"
            new_path = folder / new_name

            # 处理重名：如果新文件名已存在且不是当前文件自己
            counter = 1
            original_new_path = new_path
            while new_path.exists() and new_path != photo:
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

    print(f"目标文件夹: {folder}\n")
    rename_photos(folder)
```

### 第二轮：运行验证

**你的操作：**

1. 在桌面新建一个文件夹，命名为 `测试照片`
2. 往里面放几张图片文件（可以从网上随便下载几张，或者复制现有的照片）
3. 把上面的代码保存为 `rename_photos.py`，也放到 `测试照片` 文件夹里
4. 打开命令提示符，进入这个文件夹：

```bash
cd "C:\Users\你的用户名\Desktop\测试照片"
python rename_photos.py
```

**运行结果示例：**

```
目标文件夹: C:\Users\你的用户名\Desktop\测试照片

============================================================
即将重命名以下文件：
============================================================
  IMG_20240115_143022.jpg           -> 2024-01-15-001.jpg
  DSC_0001.jpg                      -> 2024-01-15-002.jpg
  photo_2024_03_08.png              -> 2024-03-08-001.png
  IMG_20240308_090000.jpg           -> 2024-03-08-002.jpg
============================================================
共 4 个文件

确认执行吗？输入 y 继续，输入 n 取消: y
已重命名: IMG_20240115_143022.jpg -> 2024-01-15-001.jpg
已重命名: DSC_0001.jpg -> 2024-01-15-002.jpg
已重命名: photo_2024_03_08.png -> 2024-03-08-001.png
已重命名: IMG_20240308_090000.jpg -> 2024-03-08-002.jpg

重命名完成！
```

### 第三轮：增加新功能

你想让脚本更灵活：支持按"拍摄日期"（EXIF信息）而不是"修改日期"来命名。但EXIF读取需要第三方库，你决定先用标准库实现一个简化版——支持自定义前缀。

**你输入的提示词：**

```text
我想在上面的重命名脚本基础上增加一个功能：

运行脚本时，可以输入一个自定义前缀。比如我输入"旅行"，文件名就变成 "旅行-2024-01-15-001.jpg"。
如果不输入前缀，就保持原来的 "2024-01-15-001.jpg" 格式。

请帮我修改代码，实现这个功能。
```

**AI修改后的代码（关键部分）：**

```python
def rename_photos(folder_path, prefix=""):
    """
    批量重命名照片，按修改日期分组编号
    
    参数:
        folder_path: 照片所在文件夹
        prefix: 文件名前缀，例如 "旅行-"
    """
    # ... 前面的代码不变 ...

    for date_str, files in date_groups.items():
        files.sort()

        for index, photo in enumerate(files, start=1):
            # 如果有前缀，加到日期前面
            if prefix:
                new_name = f"{prefix}-{date_str}-{index:03d}{photo.suffix.lower()}"
            else:
                new_name = f"{date_str}-{index:03d}{photo.suffix.lower()}"
            # ... 后面的代码不变 ...


if __name__ == "__main__":
    folder = Path.cwd()

    # 询问用户是否添加前缀
    user_prefix = input("请输入文件名前缀（直接回车表示不添加）: ").strip()

    print(f"目标文件夹: {folder}\n")
    rename_photos(folder, prefix=user_prefix)
```

### 第四轮：最终运行

```bash
python rename_photos.py
```

输入 `旅行` 作为前缀，确认后文件变成 `旅行-2024-01-15-001.jpg`。

## 小结：你学到了什么

1. **用 `os.rename` 重命名文件**——Python 最基础的重命名操作
2. **用 `time.strftime` 格式化时间**——把时间戳变成人类可读的字符串
3. **用 `defaultdict` 自动分组**——不用写复杂的"如果键不存在就创建列表"的逻辑
4. **用 `Path.stat().st_mtime` 获取文件修改时间**——文件属性也是标准库能读取的
5. **参数化让脚本更灵活**——通过输入前缀，同一个脚本可以适应不同场景

---

# 两个案例的对比总结

| 维度 | 案例一：整理下载文件夹 | 案例二：批量重命名照片 |
|------|----------------------|----------------------|
| **核心操作** | 移动文件 | 重命名文件 |
| **用到的标准库** | `os`, `shutil`, `pathlib` | `os`, `time`, `pathlib`, `collections` |
| **关键数据结构** | 字典（分类规则） | `defaultdict`（按日期分组） |
| **安全机制** | 预览 + 确认 + 重名处理 | 预览 + 确认 + 重名处理 |
| **扩展方向** | 增加更多分类规则、按日期细分 | 读取EXIF拍摄日期、支持正则匹配 |

---

# 通用提示词模板（可直接复用）

**启动一个新脚本：**
```text
我想写一个Python脚本，实现以下功能：
[用大白话描述你的需求，越具体越好]

要求：
1. 只用Python标准库，不需要pip安装任何包
2. 加上详细的中文注释
3. 包含错误处理（比如文件夹不存在的情况）
4. 先预览再执行，避免误操作
```

**修复问题：**
```text
我运行了上面的代码，遇到了以下问题：
[描述现象，或者粘贴报错信息]

请帮我找出原因并修复。
```

**增加功能：**
```text
我想在现有代码基础上增加一个功能：
[描述新功能]

请帮我修改代码，保持原有功能不变。
```

---

这两个案例展示了 AI 编程中最典型的工作方式：**用自然语言描述需求 → AI生成代码 → 你运行验证 → 发现问题 → 继续对话优化**。你不需要记住任何语法细节，只需要清晰地表达你想要什么。这就是 AI 时代编程的核心能力。
