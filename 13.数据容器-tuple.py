# 元组的基本操作 - tuple ----> 元素可以重复，有序，不可修改
# 定义
t1 = (80,50,46,58,24,24,22,80,20)

print(t1)
print(type(t1))

# 索引访问
print(t1[0])
print(t1[-1]) #最后一位元素

# 切片
print(t1[0:5:1])

# count() 统计元素的个数
print(t1.count(80))

# index() 获取元素的索引(第一个元素的位置)
print(t1.index(50))

# 注意点：如果定义单元素的元组，单个元素之后需要加上逗号，比如(100,)
t2 = ()
print(t2)
print(type(t2))

t3 = (100,)
print(t3)
print(type(t3))