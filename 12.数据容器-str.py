# 字符串 基本操作 ---> 不可变的(无法修改)、有序性、可迭代性
s = "Hello-Python"

print(s[4])  # 正向索引
print(s[-8]) # 反向索引

for i in s:
    print(i)

# 切片
print(s[0:5:1])
print(s[:5:1])
print(s[:5:])
print(s[:5])

print(s[6:12:1])
print(s[6::1])

print("-----------------------------")
# 步长 --> 正数：从前往后截取 ; 负数：从后往前截取
print(s[-1:-7:-1])
print(s[::-1])