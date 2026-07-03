# for循环：遍历输入的字符串

# msg = input("请输入需要遍历的字符串：")
#
# for c in msg:
#     print(f"元素：{c}")
# else:
#     print("循环结束！")

# 计算1-100奇数和

# total = 0
# for i in range(1,101,2):
#     total += i
#
# print(f"1-100奇数和：{i}")
#
# # 计算100-500奇数和
# total = 0
# for i in range(100,501,2):
#     total += i
#
# print(f"100-500奇数和：{i}")

# 打印长度为10，宽度为5的长方形

# print("*") ：自带换行效果，每一次执行都会输出新的一行中；
# print("*",end=""): end表示的是每一次输出以什么结束；默认 \n, 表示换行

# # 1.键盘录入m,n
# m = int(input("请输入长方形的长度："))
# n = int(input("请输入长方形的宽度："))
#
# # 2.打印长方形
# for j in range(n):
#     for i in range(m):
#
#         print("*",end=" ")
#     print()

# 打印99乘法表

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j} * {i} = {j*i}",end="\t")
#     print()

#打印等腰三角形

# for i in range(10):
#     for j in range(i):
#         print("*",end=" ")
#     print()

#打印数字金字塔
# num = int(input("请输入对应数字："))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#打印国际象棋棋盘
for i in range(1,9):
    for j in range(1,9):
        if j % 2 != 0:
            print("▪️",end="")
        else:
            print("▫️",end="")
    print()















