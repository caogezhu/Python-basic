# 集合 set
# 定义

# s1 = {15,15,19,1,51,1,51,165}
# print(s1)
# print(type(s1))
#
# # 定义空集合
# s2 = set()
# print(s2)
# print(type(s2))


# 常用方法：
# add()：添加元素到集合
s1 = {86,661,54,89,6,158,16,96,19}
print(s1)

s1.add(200)
print(s1)


# remove() : 移除集合中的指定元素(指定元素不存在将报错)
s1.remove(200)
print(s1)

# pop() : 随机删除集合中的元素并返回
e = s1.pop()
print(e)
print(s1)


# clear() : 清空集合
s1.clear()
print(s1)

s2 = {"A","B","C","D","E","X","Y"}
s3 = {"C","E","Y","Z"}
# difference() : 求两个集合的差集(存在在第一个集合，但不存在于第二个集合)
print(s2.difference(s3))
print(s3.difference(s2))


# union() : 求两个集合的并集
print(s2.union(s3))
print(s3.union(s2))

# intersection() : 求两个元素的交集
print(s2.intersection(s3))
print(s3.intersection(s2))















