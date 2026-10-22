import json
import re
import os

# 通讯录数据文件路径
DATA_FILE = "contacts.json"
# 手机号正则校验规则：1开头，共11位数字
PHONE_PATTERN = re.compile(r"^1[3-9]\d{9}$")
# 邮箱正则校验规则
EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2}$")


def load_contacts() -> dict:
    """从本地文件加载联系人数据，若文件不存在则返回空字典"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_contacts(contacts: dict) -> None:
    """将联系人数据保存到本地json文件"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)


def add_contact(contacts: dict, name: str, phone: str, email: str) -> bool:
    """
    添加或更新联系人
    :param contacts: 联系人字典
    :param name: 联系人姓名
    :param phone: 手机号
    :param email: 邮箱地址
    :return: 添加成功返回True，参数非法返回False
    """
    # 校验手机号格式
    if not PHONE_PATTERN.match(phone):
        print("手机号格式错误，请输入11位合法手机号")
        return False
    # 校验邮箱格式
    if not EMAIL_PATTERN.match(email):
        print("邮箱格式错误，请输入合法邮箱地址")
        return False
    # 处理重名场景，提示用户确认覆盖
    if name in contacts:
        choice = input(f"联系人{name}已存在，是否覆盖原有信息？(y/n): ").strip().lower()
        if choice != "y":
            print("已取消添加操作")
            return False
    contacts[name] = {"phone": phone, "email": email}
    print(f"联系人{name}添加成功")
    return True


def search_contact(contacts: dict, name: str) -> None:
    """查询联系人信息，不存在则提示"""
    if name in contacts:
        info = contacts[name]
        print(f"姓名：{name}\n手机号：{info['phone']}\n邮箱：{info['email']}")
    else:
        print("通讯录中未找到该联系人")


def show_all_contacts(contacts: dict) -> None:
    """显示所有联系人，空通讯录时提示"""
    if not contacts:
        print("通讯录为空，暂无联系人信息")
        return
    print("===== 所有联系人 =====")
    for name, info in contacts.items():
        print(f"姓名：{name}，手机号：{info['phone']}，邮箱：{info['email']}")


def main():
    # 启动时加载本地数据
    contacts = load_contacts()
    while True:
        print("\n===== 简易通讯录 =====")
        print("1. 添加联系人")
        print("2. 查询联系人")
        print("3. 显示所有联系人")
        print("4. 退出通讯录")
        choice = input("请输入操作编号：").strip()
        if choice == "1":
            name = input("请输入联系人姓名：").strip()
            phone = input("请输入联系人手机号：").strip()
            email = input("请输入联系人邮箱：").strip()
            if add_contact(contacts, name, phone, email):
                # 保存数据到本地
                save_contacts(contacts)
        elif choice == "2":
            name = input("请输入要查询的联系人姓名：").strip()
            search_contact(contacts, name)
        elif choice == "3":
            show_all_contacts(contacts)
        elif choice == "4":
            print("已退出通讯录")
            break
        else:
            print("输入无效，请输入1-4之间的数字")


if __name__ == "__main__":
    main()