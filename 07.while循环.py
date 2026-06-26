# while 循环 ：打印10遍 “使用python”

# i = 0
# while i < 10:
#     print("使用python")
#     i += 1
# else:
#     print("循环正常结束")

# while案例 ：计算1-100之间所有偶数之间的和
sum = 0
i = 1
while i < 100:
    if i % 2 == 0:
        sum += i
    i += 1

print("1-100之间偶数之间的和："+str(sum))