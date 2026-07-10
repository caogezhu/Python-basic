# # 字符串 基本操作 ---> 不可变的(无法修改)、有序性、可迭代性
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
s = "     Hello-Python-Hello-World     "

# find() 查找指定字符串第一次出现的索引位置
index = s.find("-")
print(index)

# count() 统计子字符串在指定字符串中出现的次数
c = s.count("o")
print(c)

# upper() 转为大写
su = s.upper()
print(su)

# lower() 转为小写
sl = s.lower()
print(sl)

# split() 将字符串按照指定字符串切割，返回列表
slist = s.split("-")
print(slist)

# strip() 去除字符串两端的空格
ss = s.strip()
print(ss)

# replace() 将字符串中的指定字串替换为新的内容
sr = s.replace("-", "_")
print(sr)

# startswith()/endswith() 判断字符串是否是以指定的字符串开头 / 结尾，返回布尔值
print(s.startswith("Hello"))
print(s.endswith("Python"))

print("--------------------------")
print(s)