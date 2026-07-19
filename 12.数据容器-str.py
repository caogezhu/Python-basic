# # 字符串 基本操作 ---> 不可变的(无法修改)、有序性、可迭代性(可通过for循环一个一个遍历出来)
# s = "Hello-Python"
#
# print(s[4])  # 正向索引
# print(s[-8]) # 反向索引
#
# for i in s:
#     print(i)
#
# # 切片
# print(s[0:5:1])
# print(s[:5:1])
# print(s[:5:])
# print(s[:5])
#
# print(s[6:12:1])
# print(s[6::1])
#
# print("-----------------------------")
# # 步长 --> 正数：从前往后截取 ; 负数：从后往前截取
# print(s[-1:-7:-1])
# print(s[::-1])


# ---------------------- 字符串常用方法 ----------------------
# s = "     Hello-Python-Hello-World     "
#
# # find() 查找指定字符串第一次出现的索引位置
# index = s.find("-")
# print(index)
#
# # count() 统计子字符串在指定字符串中出现的次数
# c = s.count("o")
# print(c)
#
# # upper() 转为大写
# su = s.upper()
# print(su)
#
# # lower() 转为小写
# sl = s.lower()
# print(sl)
#
# # split() 将字符串按照指定字符串切割，返回列表
# slist = s.split("-")
# print(slist)
#
# # strip() 去除字符串两端的空格
# ss = s.strip()
# print(ss)
#
# # replace() 将字符串中的指定字串替换为新的内容
# sr = s.replace("-", "_")
# print(sr)
#
# # startswith()/endswith() 判断字符串是否是以指定的字符串开头 / 结尾，返回布尔值
# print(s.startswith("Hello"))
# print(s.endswith("Python"))
#
# print("--------------------------")
# print(s)


# -----------------------字符串案例----------------------
# 输入邮箱，判断邮箱格式是否合法(只有一个@，至少一个.)

# 方法一:
# 1.接受用户的编码
# mail = input("请输入邮箱：")
#
# if mail.count("@")==1 and mail.count(".")>0:
#     print("邮箱合法！")
# else:
#     print("邮箱非法！")

# 方法二: in 运算符 --> 判断字串是否在字符串中，存在，返回True，否则false
# 1.接受用户的编码
# mail = input("请输入邮箱：")
#
# if mail.count("@")==1 and "." in mail:
#     print("邮箱合法！")
# else:
#     print("邮箱非法！")


# 输入字符串判断是否回文(两边对称 1234321 上海自来水来自海上)
# zf = input("请输入字符串：")
# total = 0
# for i in range(0,int(len(zf)/2)):
#     if zf[i] == zf[-(i+1)]:
#         total+=1
# if total == int(len(zf)/2):
#     print("回文")
# else:
#     print("不回文")

# 将输入的10个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容遍历输出
num_list = []
for i in range(0,3):
    zf2 = input("请输入字符串：")
    num_list.append(zf2[::-1].upper())
for i in range(0,3):
    print(num_list[i],end=" ")











