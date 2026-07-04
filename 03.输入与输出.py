# mood_index = int(input("心情指数："))
# if mood_index >= 60:
#     print("可以打游戏!")
# else:
#     print("不可以打游戏")

# 案例：银行卡ATM取款
total = 10000 #总金额

# 1.输入密码
password = input("请输入您的银行卡密码：")
print(f"密码正确，{password}")

# 2.输入取款金额
num = input("请输入您的取款金额：")

# 3.计算余额并输出 --> num 转为 int类型 ---> int()
print(f"取款后银行卡余额为：{total - int(num)}")