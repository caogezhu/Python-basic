# 生成随机数，猜随机数

import random
random_num = random.randint(1,100)
while True:
    num = int(input("请输入一个数字："))
    if num > random_num:
        print("猜的数字太大！")
    elif num < random_num:
        print("猜的数字太小")
    else:
        print("恭喜猜对了！")
        break
print("随机生成的数字为：",random_num)