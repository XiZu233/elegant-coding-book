"""
第05章实战项目测试
验证两个项目脚本的功能正确性
"""

import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

# 项目目录
PROJECTS_DIR = Path(__file__).parent.parent / "chapter-05-projects"
ORGANIZE_DIR = PROJECTS_DIR / "project-01-organize-downloads"
RENAME_DIR = PROJECTS_DIR / "project-02-rename-photos"


def _run_test_script(
    test_script: Path, input_data: str = ""
) -> subprocess.CompletedProcess:
    """辅助函数：运行测试脚本，处理编码问题"""
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    return subprocess.run(
        [sys.executable, str(test_script)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=env,
        input=input_data,
    )


def test_organize_downloads_dry_run():
    """测试整理下载文件夹脚本（预览模式）"""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)

        # 创建测试文件
        (tmp_path / "photo.jpg").write_text("fake image")
        (tmp_path / "report.pdf").write_text("fake pdf")
        (tmp_path / "archive.zip").write_text("fake zip")
        (tmp_path / "unknown.exe").write_text("fake exe")

        # 构造一个临时脚本来调用 organize_downloads
        test_script = tmp_path / "_test_run.py"
        test_script.write_text(
            f"""
import sys
sys.path.insert(0, r"{ORGANIZE_DIR}")
from organize_downloads import organize_downloads
from pathlib import Path

organize_downloads(r"{tmp_path}", dry_run=True)
""",
            encoding="utf-8",
        )

        result = _run_test_script(test_script)
        stdout = result.stdout or ""

        assert result.returncode == 0, f"脚本运行失败: {result.stderr}"
        assert "photo.jpg" in stdout
        assert "report.pdf" in stdout
        assert "archive.zip" in stdout
        assert "unknown.exe" in stdout
        assert "预览模式" in stdout

        # 确认文件没有被移动（dry_run 模式不应移动文件）
        assert (tmp_path / "photo.jpg").exists()
        assert (tmp_path / "report.pdf").exists()
        assert (tmp_path / "archive.zip").exists()
        assert (tmp_path / "unknown.exe").exists()


def test_organize_downloads_actual_run():
    """测试整理下载文件夹脚本（实际执行）"""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)

        # 创建测试文件
        (tmp_path / "photo.jpg").write_text("fake image")
        (tmp_path / "report.pdf").write_text("fake pdf")
        (tmp_path / "archive.zip").write_text("fake zip")

        # 构造测试脚本
        test_script = tmp_path / "_test_run.py"
        test_script.write_text(
            f"""
import sys
sys.path.insert(0, r"{ORGANIZE_DIR}")
from organize_downloads import organize_downloads
from pathlib import Path

organize_downloads(r"{tmp_path}")
""",
            encoding="utf-8",
        )

        result = _run_test_script(test_script, input_data="y\n")
        stdout = result.stdout or ""

        assert result.returncode == 0, f"脚本运行失败: {result.stderr}"
        assert "整理完成" in stdout

        # 确认文件已被移动到正确位置
        assert (tmp_path / "图片" / "photo.jpg").exists()
        assert (tmp_path / "文档" / "report.pdf").exists()
        assert (tmp_path / "压缩包" / "archive.zip").exists()


def test_rename_photos_dry_run():
    """测试批量重命名照片脚本（预览模式，通过导入调用）"""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)

        # 创建测试图片文件（用文本文件模拟，扩展名是图片）
        (tmp_path / "IMG_0001.jpg").write_text("fake photo 1")
        (tmp_path / "DSC_0002.jpg").write_text("fake photo 2")
        (tmp_path / "photo.png").write_text("fake photo 3")

        # 修改文件时间，让两个文件同一天，一个不同天
        now = time.time()
        yesterday = now - 86400
        os.utime(tmp_path / "IMG_0001.jpg", (yesterday, yesterday))
        os.utime(tmp_path / "DSC_0002.jpg", (yesterday, yesterday))
        os.utime(tmp_path / "photo.png", (now, now))

        # 构造测试脚本
        test_script = tmp_path / "_test_run.py"
        test_script.write_text(
            f"""
import sys
sys.path.insert(0, r"{RENAME_DIR}")
from rename_photos import rename_photos
from pathlib import Path

rename_photos(r"{tmp_path}")
""",
            encoding="utf-8",
        )

        result = _run_test_script(test_script, input_data="\nn\n")
        stdout = result.stdout or ""

        assert result.returncode == 0, f"脚本运行失败: {result.stderr}"
        assert "即将重命名" in stdout
        assert "IMG_0001.jpg" in stdout
        assert "DSC_0002.jpg" in stdout
        assert "photo.png" in stdout

        # 确认文件没有被重命名（因为输入了 n 取消）
        assert (tmp_path / "IMG_0001.jpg").exists()
        assert (tmp_path / "DSC_0002.jpg").exists()
        assert (tmp_path / "photo.png").exists()


def test_rename_photos_actual_run():
    """测试批量重命名照片脚本（实际执行）"""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)

        # 创建测试图片文件
        (tmp_path / "IMG_0001.jpg").write_text("fake photo 1")
        (tmp_path / "DSC_0002.jpg").write_text("fake photo 2")

        # 修改文件时间为同一天
        test_time = time.mktime((2024, 1, 15, 12, 0, 0, 0, 0, 0))
        os.utime(tmp_path / "IMG_0001.jpg", (test_time, test_time))
        os.utime(tmp_path / "DSC_0002.jpg", (test_time, test_time))

        # 构造测试脚本
        test_script = tmp_path / "_test_run.py"
        test_script.write_text(
            f"""
import sys
sys.path.insert(0, r"{RENAME_DIR}")
from rename_photos import rename_photos
from pathlib import Path

rename_photos(r"{tmp_path}")
""",
            encoding="utf-8",
        )

        result = _run_test_script(test_script, input_data="y\n")
        stdout = result.stdout or ""

        assert result.returncode == 0, f"脚本运行失败: {result.stderr}"
        assert "重命名完成" in stdout

        # 确认原文件已被重命名
        assert not (tmp_path / "IMG_0001.jpg").exists()
        assert not (tmp_path / "DSC_0002.jpg").exists()

        # 确认新文件存在（格式为 YYYY-MM-DD-NNN.jpg）
        jpg_files = list(tmp_path.glob("*.jpg"))
        assert len(jpg_files) == 2
        for f in jpg_files:
            assert f.name.startswith("2024-01-15-")


def test_rename_photos_with_prefix():
    """测试批量重命名照片脚本（带前缀）"""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)

        # 创建测试图片文件
        (tmp_path / "IMG_0001.jpg").write_text("fake photo 1")

        test_time = time.mktime((2024, 3, 8, 12, 0, 0, 0, 0, 0))
        os.utime(tmp_path / "IMG_0001.jpg", (test_time, test_time))

        # 构造测试脚本
        test_script = tmp_path / "_test_run.py"
        test_script.write_text(
            f"""
import sys
sys.path.insert(0, r"{RENAME_DIR}")
from rename_photos import rename_photos
from pathlib import Path

rename_photos(r"{tmp_path}", prefix="旅行")
""",
            encoding="utf-8",
        )

        result = _run_test_script(test_script, input_data="y\n")
        stdout = result.stdout or ""

        assert result.returncode == 0, f"脚本运行失败: {result.stderr}"
        assert "重命名完成" in stdout

        # 确认新文件包含前缀
        jpg_files = list(tmp_path.glob("*.jpg"))
        assert len(jpg_files) == 1
        assert "旅行-2024-03-08-" in jpg_files[0].name
