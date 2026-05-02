"""
第02章示例代码测试
验证所有示例文件都能正常运行并产生预期输出
"""

import os
import subprocess
import sys
from pathlib import Path

# 示例文件所在目录
EXAMPLES_DIR = Path(__file__).parent.parent / "chapter-02-python-basics" / "examples"


def run_script(script_name):
    """运行一个 Python 脚本，返回输出和返回码"""
    script_path = EXAMPLES_DIR / script_name
    # 设置环境变量强制 UTF-8 输出，避免 Windows 控制台编码问题
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=env,
    )
    return result


def test_01_variables():
    """测试 01_variables.py 正常运行"""
    result = run_script("01_variables.py")
    stdout = result.stdout or ""
    assert result.returncode == 0, f"脚本运行失败: {result.stderr}"
    assert "小明" in stdout
    assert "变量输出" in stdout
    assert "字符串操作" in stdout
    assert "数字运算" in stdout


def test_02_functions():
    """测试 02_functions.py 正常运行"""
    result = run_script("02_functions.py")
    stdout = result.stdout or ""
    assert result.returncode == 0, f"脚本运行失败: {result.stderr}"
    assert "你好，小明" in stdout
    assert "矩形面积" in stdout
    assert "优秀" in stdout


def test_03_conditions():
    """测试 03_conditions.py 正常运行"""
    result = run_script("03_conditions.py")
    stdout = result.stdout or ""
    assert result.returncode == 0, f"脚本运行失败: {result.stderr}"
    assert "良好" in stdout
    assert "可以进入" in stdout
    assert "闰年" in stdout


def test_04_loops():
    """测试 04_loops.py 正常运行"""
    result = run_script("04_loops.py")
    stdout = result.stdout or ""
    assert result.returncode == 0, f"脚本运行失败: {result.stderr}"
    assert "我喜欢吃苹果" in stdout
    assert "九九乘法表" in stdout
    assert "循环结束" in stdout


def test_05_lists():
    """测试 05_lists.py 正常运行"""
    result = run_script("05_lists.py")
    stdout = result.stdout or ""
    assert result.returncode == 0, f"脚本运行失败: {result.stderr}"
    assert "苹果" in stdout
    assert "列表切片" in stdout
    assert "待办事项" in stdout


def test_06_dictionaries():
    """测试 06_dictionaries.py 正常运行"""
    result = run_script("06_dictionaries.py")
    stdout = result.stdout or ""
    assert result.returncode == 0, f"脚本运行失败: {result.stderr}"
    assert "小明" in stdout
    assert "通讯录" in stdout
    assert "键值对" in stdout
