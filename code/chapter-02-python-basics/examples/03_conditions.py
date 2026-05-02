# 03_conditions.py
# 本文件演示 Python 条件判断：if / elif / else
# 让程序根据不同情况做出不同反应


def demo_basic_if():
    """基础 if/elif/else 演示"""
    score = 85

    if score >= 90:
        grade = "优秀"
    elif score >= 80:
        grade = "良好"
    elif score >= 60:
        grade = "及格"
    else:
        grade = "不及格"

    print(f"分数：{score}，等级：{grade}")


def demo_comparison_operators():
    """比较运算符演示"""
    print("\n=== 比较运算符 ===")
    a, b = 10, 20

    print(f"a = {a}, b = {b}")
    print(f"a == b: {a == b}")   # 等于
    print(f"a != b: {a != b}")   # 不等于
    print(f"a > b:  {a > b}")    # 大于
    print(f"a < b:  {a < b}")    # 小于
    print(f"a >= b: {a >= b}")   # 大于等于
    print(f"a <= b: {a <= b}")   # 小于等于


def demo_logical_operators():
    """逻辑运算符演示：and / or / not"""
    print("\n=== 逻辑运算符 ===")

    age = 25
    has_id = True

    # and：两个条件都要满足
    if age >= 18 and has_id:
        print("已成年且有身份证 -> 可以进入")
    else:
        print("不能进入")

    # or：至少一个满足
    is_vip = False
    if has_id or is_vip:
        print("有身份证或是VIP -> 可以通行")

    # not：反过来
    is_raining = False
    if not is_raining:
        print("没下雨 -> 可以出门")


def demo_file_exists():
    """实际例子：判断文件是否存在"""
    import os

    print("\n=== 实际应用：判断文件是否存在 ===")
    file_path = "data.txt"

    if os.path.exists(file_path):
        print(f"文件 {file_path} 存在")
    else:
        print(f"文件 {file_path} 不存在，请检查路径")


def demo_leap_year(year):
    """判断闰年：能被4整除但不能被100整除，或者能被400整除"""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


def main():
    """主函数"""
    print("=== 基础条件判断 ===")
    demo_basic_if()

    demo_comparison_operators()
    demo_logical_operators()
    demo_file_exists()

    print("\n=== 闰年判断 ===")
    test_years = [2000, 1900, 2024, 2023]
    for year in test_years:
        result = "是闰年" if demo_leap_year(year) else "不是闰年"
        print(f"{year} 年: {result}")


if __name__ == "__main__":
    main()
