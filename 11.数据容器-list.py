# # 列表操作
# # 定义列表 - list
# s = [60,50,801,51,54,4,"A","Hello",True]
# print(type(s))
#
# # 访问列表元素
# # 获取
# print(s[0]) # 正向索引，从0开始
# print(s[-9]) # 反向索引，从-1开始
#
# print(s[1])
# print(s[-8])
#
# # 修改
# s[5] = "B"
# print(s[5])
# print(s)
#
# # 注意：如果指定的索引，超出范围，将会报错 list assignment index out of range
# # s[10] = "DEF"
# # print(s[10])
# # print(s)
#
# # 删除
# del s[5]
# print(s)
#
# # 遍历
# for i in s:
#     print(i)
from hmac import new

# # -----------------------列表 list 切片 ------------------------------
# # 定义列表
# s = ["A","B","C","D","E","F","G","H","I","J"]
#
# # 切片操作 s[开始索引:结束索引:步长]
# print(s[0:5:1])
# print(type(s[0:5:1]))
#
# print(s[:5:1])
# print(s[:5:])
# print(s[:5])
#
# print(s[0:5:2])
# print(s[0:-2:1])

# # -----------------------列表 list 常用方法 ------------------------------
# # 列表定义
# s = [65,56,648,646,156,75,6,45,96,75,154]
# print(s)
#
# # append()：在列表末尾追加元素
# s.append(100)
# print(s)
#
# # insert()：在指定索引之前，插入元素
# s.insert(2,80)
# print(s)
#
# # remove()：移除列表中第一个匹配的元素
# s.remove(75)
# print(s)
#
# # pop()：删除列表中指定索引位置的元素并返回(如果未指定，默认删除最后一个)
# e = s.pop(1)
# print(e)
#
# e = s.pop()
# print(e)
#
# print(s)
#
# # sort()：排序
# s.sort()
# print(s)
#
# # reverse()：反转列表元素
# s.reverse()
# print(s)

# -----------------------列表 list 案例 ------------------------------
# 1.定义列表
# num_list = []
#
# for i in range(10):
#     num = int(input("请输入一个有效数字："))
#     num_list.append(num)
# print("数字列表：",num_list)
#
# num_list.sort()
# print("排序后的列表为：",num_list)
#
# print("最小值:",num_list[0])
# print("最大值:",num_list[-1])
# print("平均值:",sum(num_list)/len(num_list))



# #案例2：合并两个列表中的元素，并对合并的结果进行去重处理(去除列表中的重复元素)
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
#
# # 1.合并列表
# for num in num_list2:
#     num_list1.append(num)
# print("合并后的列表为：",num_list1)
#
# # 2.去除重复元素
# new_list = []
#
# for num in num_list1:
#     if num not in new_list:
#         new_list.append(num)
# print("去除重复元素后的列表为：",new_list)


# #案例2(简化)：合并两个列表中的元素，并对合并的结果进行去重处理(去除列表中的重复元素)
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
#
# # 1.合并列表
# # 解包：将列表这一类容器解开成一个一个独立的元素
# # num_list = [*num_list1, *num_list2]
#
# # 组包：将多个组合并列为一个容器
# num_list = num_list1 + num_list2
#
# print("合并后的列表为：",num_list)
#
# # 2.去除重复元素
# new_list = []
#
# for num in num_list:
#     if num not in new_list:
#         new_list.append(num)
# print("去除重复元素后的列表为：",new_list)

#案例3：生成1-20的平方列表
# 方式一: 传统方式
# num_list = []
# for i in range(1,21):
#     num_list.append(i**2)
# print(num_list)
#
# # 方式二：列表推导式 ---> 就是按照一定的规则快速生成一个列表的方法 --> 语法格式1：[要插入的值 for i in 序列/列表]
# num_list2 = [i**2 for i in range(1,21)]
# print(num_list2)


# 案例四：从一个数字列表中提取所有偶数，并计算其平方，组成一个新的列表
# 列表推导式 ---> 就是按照一定的规则快速生成一个列表的方法 --> 语法格式2：[要插入的值 for i in 序列/列表 if 条件]
# num_list = [15,54,15.8,51814,1515,515,46,158,948]
# new_list = [i**2 for i in num_list if i%2==0]
# print(new_list)


#合并列表后去重并排序
# list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
# list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
# list3 = ['W', 'A', 'S', 'D']
#
# num_list = list1.copy()
# for num in list2 + list3:
#     if num not in num_list:
#         num_list.append(num)
# num_list.sort()
# print(num_list)

# 将列表中能被3或5整除的数提出来，获取其平方，组成一个新列表
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
         17, 18,19, 20,21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
new_list = [i**2 for i in list1 if i%3==0 or i%5==0]
print(new_list)

















