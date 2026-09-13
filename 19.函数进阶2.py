# # 函数的参数类型
# # 加
# def add(x, y):
#     return x + y
#
# # 减
# def subtract(x, y):
#     return x - y
#
# # 乘
# def multiply(x, y):
#     return x * y
#
# # 除
# def divide(x, y):
#     return x / y
#
# # 计算
# def calc(x, y, oper):
#     return oper(x, y)
#
# print(calc(10, 2, multiply ))


# 匿名函数
# 需求1：打印一个分割线
# def out_line():
#     print("----------------------------")

out_line = lambda : print("----------------------------")
out_line()

# 需求2：计算两个数之和
# def add(a,b):
#     return a+b

add = lambda a,b: a+b
print(add(100,200))

# 需求3：完成下列列表的排序操作，按照每一个元素的字符个数，从小到大排序；
data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
print(data_list)

data_list.sort(key=lambda item: len(item))
print(data_list)






















