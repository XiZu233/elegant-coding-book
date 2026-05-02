# 06_dictionaries.py
# 本文件演示 Python 字典（dict）的常用操作
# 字典是带标签的储物柜，用花括号 {} 包裹，每个数据都有一个"钥匙"（key）


def demo_create_and_access():
    """创建字典和访问元素"""
    student = {"name": "小明", "age": 20, "major": "计算机"}

    print("=== 创建和访问字典 ===")
    print(f"学生信息: {student}")
    print(f"姓名: {student['name']}")
    print(f"年龄: {student['age']}")

    # 用 get 方法安全访问（key 不存在时不会报错）
    print(f"城市: {student.get('city', '未填写')}")


def demo_modify_dict():
    """修改字典内容"""
    student = {"name": "小明", "age": 20, "major": "计算机"}

    print("\n=== 修改字典 ===")
    print(f"原字典: {student}")

    # 修改值
    student["age"] = 21
    print(f"修改年龄后: {student}")

    # 添加新项
    student["city"] = "北京"
    print(f"添加城市后: {student}")

    # 删除项
    del student["major"]
    print(f"删除专业后: {student}")


def demo_dict_methods():
    """字典常用方法"""
    scores = {"数学": 90, "语文": 85, "英语": 88}

    print("\n=== 字典方法 ===")
    print(f"所有键: {list(scores.keys())}")
    print(f"所有值: {list(scores.values())}")
    print(f"所有键值对: {list(scores.items())}")

    # 遍历字典
    print("\n遍历键值对:")
    for subject, score in scores.items():
        print(f"  {subject}: {score} 分")


def demo_contact_book():
    """实际应用：个人通讯录"""
    print("\n=== 实际应用：个人通讯录 ===")

    # 用字典存储联系人信息
    contacts = {
        "张三": {"phone": "13800138000", "address": "北京市"},
        "李四": {"phone": "13900139000", "address": "上海市"},
    }

    # 显示所有联系人
    print("通讯录列表:")
    for name, info in contacts.items():
        print(f"  {name}: {info['phone']}, {info['address']}")

    # 添加新联系人
    contacts["王五"] = {"phone": "13700137000", "address": "广州市"}
    print(f"\n添加王五后: {contacts}")

    # 查找联系人
    name = "张三"
    if name in contacts:
        print(f"\n找到 {name}: {contacts[name]}")
    else:
        print(f"\n未找到 {name}")

    # 删除联系人
    del contacts["李四"]
    print(f"\n删除李四后，剩余联系人: {list(contacts.keys())}")


def main():
    """主函数"""
    demo_create_and_access()
    demo_modify_dict()
    demo_dict_methods()
    demo_contact_book()


if __name__ == "__main__":
    main()
