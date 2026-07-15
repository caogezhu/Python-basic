# # 元组的基本操作 - tuple ----> 元素可以重复，有序，不可修改
# # 定义
# t1 = (80,50,46,58,24,24,22,80,20)
#
# print(t1)
# print(type(t1))
#
# # 索引访问
# print(t1[0])
# print(t1[-1]) #最后一位元素
#
# # 切片
# print(t1[0:5:1])
#
# # count() 统计元素的个数
# print(t1.count(80))
#
# # index() 获取元素的索引(第一个元素的位置)
# print(t1.index(50))
#
# # 注意点：如果定义单元素的元组，单个元素之后需要加上逗号，比如(100,)
# t2 = ()
# print(t2)
# print(type(t2))
#
# t3 = (100,)
# print(t3)
# print(type(t3))


# # -----------------------------元组 tuple 组包与解包 --------------------------------
# # 组包操作
# t1 = (1,5,19,81,41,52)
# t2 = 1,5,19,81,41,52
#
# print(t1)
# print(t2)
#
# # 解包操作
# # 基础解包 (变量数量要与容器个数一致)
# a,b,c,d,e,f = t1
# print(a,b,c,d,e,f)
#
# # 扩展解包 (* 收集剩余元素，封装到列表list中)
# first,second,*other,last = t1
# print(first,second,other,last)
#
# *other,last2,last1 = t1
# print(other,last2,last1)


# # 案例一：现有两个变量，分别为 a = 10,b = 20,现需要这两个变量值交换，然后输出到控制台
# a = 10
# b = 20
#
# # 组包
# # t = b,a
# # # 解包
# # a,b = t
#
# # 合并
# a,b = b,a
# print(a,b)
#
#
# # 案例一：现有三个变量，分别为 a = 100,b = 200,c = 300,现需要这三个变量值交换，将a,b,c的值分别赋值给c,a,b,并将其输出到控制台
# a = 100
# b = 200
# c = 300
#
# # 组包与解包操作
# c,a,b = a,b,c
# print(a,b,c)

students = (
     ("S001", "王林", 85, 92, 78),
     ("S002", "李慕婉",92, 88, 95),
     ("S003", "十三", 78, 85, 82),
     ("S004", "曾牛", 88, 79, 91),
     ("S005", "周轶", 95, 96, 89),
     ("S006", "王卓", 76, 82, 77),
     ("S007", "红蝶", 89, 91, 94),
     ("S008", "徐立国",75, 69, 71),
     ("S009", "许木", 86, 89, 83),
     ("S010", "通天", 66, 59, 72)
)
# 1. 计算每个学生的总分、各科平均分，然后一并输出出来
print("学号 \t 姓名\t\t语文\t\t数学 \t\t 英语\t\t 总分 \t\t 平均分")
# 方式一：
# for s in students:
#     total = s[2] + s[3] + s[4]
#     avg = total / 3
#     print(f"{s[0]} \t {s[1]} \t\t {s[2]} \t {s[3]} \t\t {s[4]} \t\t {total} \t\t {avg:.1f}")

# 方式二：
for id,name,chinese,math,english in students:
    total = chinese + math + english
    avg = total / 3
    print(f"{id} \t {name} \t\t {chinese} \t {math} \t\t {english} \t\t {total} \t\t {avg:.1f}")

print()

# 统计各科成绩最高分、最低分、平均分
# 各科成绩表
chinese_scores = [s[2]for s in students]
math_scores = [s[3]for s in students]
english_scores = [s[4]for s in students]

print(f"语文最高分：{max(chinese_scores)},最低分：{min(chinese_scores)},"
      f"平均分：{sum(chinese_scores)/len(chinese_scores)}")
print(f"数学最高分：{max(math_scores)},最低分：{min(math_scores)},"
      f"平均分：{sum(math_scores)/len(math_scores)}")
print(f"英语最高分：{max(english_scores)},最低分：{min(english_scores)},"
      f"平均分：{sum(english_scores)/len(english_scores)}")

print()
# 查找成绩优秀(平均分 > 90)学生并输出
print("优秀学生名单：")
# 方式一：
# for s in students:
#     total = s[2] + s[3] + s[4]
#     avg = total / 3
#     if avg > 90:
#         print(f"优秀学生学号：{s[0]},姓名：{s[1]},平均分：{avg:.1f}")

# 方式二：
for id,name,chinese,math,english in students:
    total = chinese + math + english
    avg = total / 3
    if avg > 90:
        print(f"优秀学生学号：{id},姓名：{name},平均分：{avg:.1f}")


















