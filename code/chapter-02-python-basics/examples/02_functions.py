# 02_functions.py
# 本文件演示 Python 函数的定义、调用和参数传递
# 函数是把重复的操作打包，写好一次，以后叫名字就能执行


def greet(name):
    """向某人问好"""
    message = "你好，" + name + "！"
    return message


def calculate_area(width, height):
    """计算矩形面积"""
    area = width * height
    return area


def calculate_price(original, is_member):
    """
    计算折扣后的价格
    规则：会员打 9 折，满 100 再打 95 折
    """
    price = original
    if is_member:
        price *= 0.9
    if original >= 100:
        price *= 0.95
    return round(price, 2)  # 保留两位小数


def introduce(name, age):
    """输出自我介绍"""
    future_age = age + 5
    print(f"你好，{name}！你今年 {age} 岁，5 年后你将 {future_age} 岁。")


def get_grade(score):
    """根据分数返回等级"""
    if score < 0 or score > 100:
        return "输入无效"
    elif score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 70:
        return "中等"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"


def main():
    """主函数：演示所有函数用法"""
    print("=== 基础函数调用 ===")

    # 调用 greet 函数
    result = greet("小明")
    print(result)
    print(greet("小红"))

    # 调用带多个参数的函数
    print("\n=== 多参数函数 ===")
    area = calculate_area(5, 3)
    print(f"矩形面积(5x3): {area}")

    # 调用计算价格函数
    print("\n=== 带逻辑的函数 ===")
    print(f"原价 120，会员价: {calculate_price(120, True)}")
    print(f"原价 80，非会员价: {calculate_price(80, False)}")

    # 调用自我介绍函数
    print("\n=== 自我介绍函数 ===")
    introduce("张三", 25)

    # 调用成绩等级函数
    print("\n=== 成绩等级函数 ===")
    test_scores = [95, 85, 75, 65, 55, -5, 105]
    for score in test_scores:
        print(f"分数: {score:3d} -> {get_grade(score)}")


if __name__ == "__main__":
    main()
