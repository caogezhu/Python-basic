# # ------------------------ 函数 - 变量的作用域 ------------------------
# # 全局变量 : 在函数外部 或 函数的内部都是可以访问的 ;
# num = 100
#
# # 定义函数
# def circle_area(r):
#     # 局部变量：只能在函数内部使用
#     pi = 3.14
#     area = pi * r * r
#     # 局部变量 num
#     # 函数内使用，声明接下来要使用全局变量，语法： global ***
#     global num
#     num = 10000
#     print("num = ", num)  # 10000
#
#     return area
#
# # 调用函数
# c_area = circle_area(10)
# print(c_area)
#
# print("num = ", num)  # 10000

# # ------------------------ 函数 - 传参方式 ------------------------
# # 定义函数
# def reg_stu(name, age, gender, city):
#     print(f"注册成功，姓名: {name}, 年龄: {age}, 性别: {gender}, 城市: {city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}
#
# # 传参方式一：位置参数
# stu = reg_stu("张三", 18, "男", "北京")
# print(stu)
#
# # 传参方式二：关键字参数
# stu = reg_stu(name="王林", age=28, gender="男", city="北京")
# print(stu)
#
# stu = reg_stu(age=20, gender="女", city="北京", name="李慕婉")
# print(stu)
#
# # 传参方式三：位置参数 + 关键字参数 ---> 位置参数在前，关键字参数在后
# stu = reg_stu("李慕婉", 20, gender="女", city="北京")
# print(stu)

# ------------------------ 函数 - 默认参数 ------------------------
# 定义函数
def reg_stu(name, age, gender="男", city="北京"):
    print(f"注册成功，姓名: {name}, 年龄: {age}, 性别: {gender}, 城市: {city}")
    return {"name": name, "age": age, "gender": gender, "city": city}

# 调用函数
stu = reg_stu("王林", 20)
print(stu)

stu = reg_stu("李慕婉", 18, gender="女")
print(stu)

stu = reg_stu("韩立", 22, city="上海")
print(stu)


