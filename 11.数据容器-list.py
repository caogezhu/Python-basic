# 列表操作
# 定义列表 - list
s = [60,50,801,51,54,4,"A","Hello",True]
print(type(s))

# 访问列表元素
# 获取
print(s[0]) # 正向索引，从0开始
print(s[-9]) # 反向索引，从-1开始

print(s[1])
print(s[-8])

# 修改
s[5] = "B"
print(s[5])
print(s)

# 注意：如果指定的索引，超出范围，将会报错 list assignment index out of range
# s[10] = "DEF"
# print(s[10])
# print(s)

# 删除
del s[5]
print(s)

# 遍历
for i in s:
    print(i)
