print("欢迎来到文字西游！\n版本1.0\n这是一个用文字描述的西游冒险游戏，你将扮演一位英雄踏上西行之旅。")
word = input("请输入'start'开始游戏，或输入其他内容退出：")
if word == 'start':
    name = input("请输入你的角色名字：")
    print(f"欢迎{name}加入西游冒险！")
    print("游戏正式开始！")