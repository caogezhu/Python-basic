# 读取输入
price, num, level = input().split()
price = float(price)
num = int(num)

if level == "高级会员":
    if num >= 10:
        rate = 0.8
    elif num >=5:
        rate = 0.85
    else:
        rate = 0.9
elif level == "普通会员":
    if num >= 10:
        rate = 0.85
    else:
        rate = 0.95
elif level == "非会员":
    if num >=5:
        rate = 0.85
    else:
        rate = 1.0
else:
    rate = 1.0

final = price * num * rate
print(final)
