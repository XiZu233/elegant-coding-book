# 04_loops.py
# 本文件演示 Python 循环：for 循环和 while 循环
# 让程序重复执行某些操作


def demo_for_list():
    """for 循环遍历列表"""
    fruits = ["苹果", "香蕉", "橙子"]

    print("=== for 循环遍历列表 ===")
    for fruit in fruits:
        print(f"我喜欢吃{fruit}")


def demo_for_range():
    """用 range 生成数字序列"""
    print("\n=== range 函数 ===")

    print("range(5):")
    for i in range(5):
        print(i, end=" ")
    print()

    print("range(1, 11):")
    for i in range(1, 11):
        print(i, end=" ")
    print()

    print("range(0, 10, 2) 步长为2:")
    for i in range(0, 10, 2):
        print(i, end=" ")
    print()


def demo_while_loop():
    """while 循环：条件控制"""
    print("\n=== while 循环 ===")

    count = 0
    while count < 5:
        print(f"当前计数：{count}")
        count = count + 1  # 别忘了更新条件，否则会无限循环！

    print("循环结束")


def demo_multiplication_table():
    """九九乘法表"""
    print("\n=== 九九乘法表 ===")
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j}x{i}={i * j:2d}", end="  ")
        print()


def demo_guess_number():
    """猜数字游戏（简化版，不依赖 input，直接演示逻辑）"""
    import random

    print("\n=== 猜数字游戏演示 ===")
    target = random.randint(1, 100)  # 随机生成 1-100 的数字

    # 模拟几次猜测（实际游戏中用 input() 获取用户输入）
    guesses = [50, 75, 60, 65, target]

    for guess in guesses:
        if guess == target:
            print(f"恭喜！你猜对了！数字是 {target}")
            break  # 猜对了，退出循环
        elif guess < target:
            print(f"猜测 {guess}: 太小了，再大一点")
        else:
            print(f"猜测 {guess}: 太大了，再小一点")


def main():
    """主函数"""
    demo_for_list()
    demo_for_range()
    demo_while_loop()
    demo_multiplication_table()
    demo_guess_number()


if __name__ == "__main__":
    main()
