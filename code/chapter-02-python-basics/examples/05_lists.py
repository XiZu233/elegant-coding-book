# 05_lists.py
# 本文件演示 Python 列表（list）的常用操作
# 列表是排好队的一组数据，用方括号 [] 包裹


def demo_create_and_access():
    """创建列表和访问元素"""
    fruits = ["苹果", "香蕉", "橙子"]

    print("=== 创建和访问列表 ===")
    print(f"水果列表: {fruits}")
    print(f"第一个元素: {fruits[0]}")     # 注意：索引从 0 开始！
    print(f"第二个元素: {fruits[1]}")
    print(f"最后一个元素: {fruits[-1]}")  # -1 表示最后一个
    print(f"列表长度: {len(fruits)}")


def demo_modify_list():
    """修改列表内容"""
    fruits = ["苹果", "香蕉", "橙子"]

    print("\n=== 修改列表 ===")
    print(f"原列表: {fruits}")

    # 添加元素
    fruits.append("葡萄")
    print(f"append('葡萄')后: {fruits}")

    # 插入到指定位置
    fruits.insert(1, "芒果")
    print(f"insert(1, '芒果')后: {fruits}")

    # 删除指定元素
    fruits.remove("香蕉")
    print(f"remove('香蕉')后: {fruits}")

    # 弹出最后一个元素
    last = fruits.pop()
    print(f"pop() 弹出: {last}, 剩余: {fruits}")


def demo_list_slicing():
    """列表切片"""
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    print("\n=== 列表切片 ===")
    print(f"原列表: {numbers}")
    print(f"前3个: {numbers[:3]}")
    print(f"第3到第6个: {numbers[3:7]}")
    print(f"后3个: {numbers[-3:]}")
    print(f"每隔一个取一个: {numbers[::2]}")


def demo_list_comprehension():
    """列表推导式（进阶但实用）"""
    print("\n=== 列表推导式 ===")

    # 生成 0-9 的平方数列表
    squares = [x ** 2 for x in range(10)]
    print(f"0-9 的平方: {squares}")

    # 只保留偶数
    evens = [x for x in range(20) if x % 2 == 0]
    print(f"0-19 的偶数: {evens}")


def demo_todo_list():
    """实际应用：简单的待办事项列表"""
    print("\n=== 实际应用：待办事项列表 ===")

    todos = []

    # 添加任务
    todos.append("学习 Python")
    todos.append("做练习题")
    todos.append("复习列表操作")
    print(f"添加任务后: {todos}")

    # 显示所有任务（带序号）
    print("\n任务清单:")
    for index, task in enumerate(todos, start=1):
        print(f"  {index}. [ ] {task}")

    # 完成任务（删除第一个）
    completed = todos.pop(0)
    print(f"\n已完成: {completed}")
    print(f"剩余任务: {todos}")


def main():
    """主函数"""
    demo_create_and_access()
    demo_modify_list()
    demo_list_slicing()
    demo_list_comprehension()
    demo_todo_list()


if __name__ == "__main__":
    main()
