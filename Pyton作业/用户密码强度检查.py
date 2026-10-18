# 读取输入密码
pwd = input("请输入密码：")

# 初始化四个标记
has_upper = False    # 大写字母
has_lower = False    # 小写字母
has_digit = False    # 数字
has_special = False  # 特殊字符 !@#$%^&*

# 特殊字符集合
special_chars = "!@#$%^&*"

# 条件1：长度至少8位
if len(pwd) >= 8:
    # 遍历每个字符
    for c in pwd:
        if c.isupper():
            has_upper = True
        elif c.islower():
            has_lower = True
        elif c.isdigit():
            has_digit = True
        elif c in special_chars:
            has_special = True
    # 全部满足
    if has_upper and has_lower and has_digit and has_special:
        print("符合要求")
    else:
        print("不符合要求")
else:
    print("不符合要求")
