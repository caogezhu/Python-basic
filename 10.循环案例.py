# 生成随机数，猜随机数

# import random
# random_num = random.randint(1,100)
# while True:
#     num = int(input("请输入一个数字："))
#     if num > random_num:
#         print("猜的数字太大！")
#     elif num < random_num:
#         print("猜的数字太小")
#     else:
#         print("恭喜猜对了！")
#         break
# print("随机生成的数字为：",random_num)

# 将1-10000之间(含1000)所有的5的倍数的数字累加起来
# total = 0
# for i in range(0,10001,5):
#     total += i
# print(total)

# 统计字符串lhbcusfsdsdkbkalbvhbfea中有多少个a,k
count_a = 0
count_k = 0
msg = "lhbcusfsdsdkbkalbvhbfeka"
for a in msg:
    if a == "a":
        count_a+=1
    elif a == "k":
        count_k+=1
print(f"{count_a} {count_k}")