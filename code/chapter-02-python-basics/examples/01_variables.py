# 01_variables.py
# 本文件演示 Python 变量的声明、命名规则以及四种基础数据类型
# 适合零基础初学者理解"给数据贴标签"的概念


def demo_variables():
    """变量声明和基础类型演示"""
    # 给数据贴上名字标签
    name = "小明"  # 字符串（str）：一串文字
    age = 25  # 整数（int）：没有小数点的数字
    height = 1.75  # 浮点数（float）：有小数点的数字
    is_student = True  # 布尔值（bool）：True（真）或 False（假）

    # 使用变量
    print("=== 变量输出 ===")
    print(f"姓名: {name}")
    print(f"年龄: {age}")
    print(f"年龄 + 1 = {age + 1}")  # 数字可以做运算
    print(f"身高: {height} 米")
    print(f"是否学生: {is_student}")


def demo_string_operations():
    """字符串操作演示"""
    message = "你好，世界！"
    print("\n=== 字符串操作 ===")
    print(f"原字符串: {message}")
    print(f"转大写: {message.upper()}")  # 中文不变，英文会转大写
    print(f"字符串长度: {len(message)}")  # 6 个字符

    # 字符串拼接
    first = "张"
    last = "三"
    full = first + last
    print(f"拼接结果: {full}")


def demo_number_operations():
    """数字运算演示"""
    apples = 5  # 整数
    price = 3.5  # 浮点数

    print("\n=== 数字运算 ===")
    total = apples * price
    print(f"{apples} 个苹果，每个 {price} 元，总价: {total}")

    # 取整和取余
    print(f"17 // 5 = {17 // 5}")  # 整除：3
    print(f"17 % 5 = {17 % 5}")  # 取余：2


def demo_naming_rules():
    """命名规则演示：好的命名 vs 不好的命名"""
    print("\n=== 命名规范 ===")

    # 好的命名（snake_case，看到名字就知道用途）
    user_name = "张三"
    max_login_attempts = 3
    print(f"好的命名示例: user_name = {user_name}")
    print(f"好的命名示例: max_login_attempts = {max_login_attempts}")

    # 布尔值用 is_ 或 has_ 开头
    is_valid = True
    has_permission = False
    print(f"布尔值命名: is_valid = {is_valid}, has_permission = {has_permission}")


if __name__ == "__main__":
    demo_variables()
    demo_string_operations()
    demo_number_operations()
    demo_naming_rules()
