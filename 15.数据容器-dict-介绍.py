# 字典 --> 键值对(key: value)存储
# 键(key)不能重复(如果重复，后面的值会覆盖前面的值)、必须是不可变类型(str,int,float,tuple)，不能是(如：列表list、集合set、字典dict)
# value值可修改
# dict1 = {"原神":1,"崩坏三":2,"崩铁":3,"绝区零":4}
# print(dict1)
# print(type(dict1))
#
# #key必须是不可变类型(str,int,float,tuple)，不能是(列表list、集合set、字典dict)
# dict2 = {0:670,1.5:522,('A','B'):252}
# print(dict2)
# print(type(dict2))
#
# # 访问
# print(dict1["原神"])
# dict1["原神"]=5
# print(dict1)
from itertools import count

# ----------------------------字典 常用操作-------------------------------
# dict1 = {"原神":1,"崩坏三":2,"崩铁":3,"绝区零":4}
# print(dict1)
#
# # 添加 - key不存在就是添加
# dict1["崩坏·因缘精灵"] = 3
# print(dict1)
#
# # 添加 - key存在就是修改
# dict1["崩坏·因缘精灵"] = 5
# print(dict1)
#
# # 查询
# print(dict1["崩坏·因缘精灵"]) #根据key获取value
# print(dict1.get("崩坏·因缘精灵")) #根据key获取value
#
# print(dict1.keys()) #获取所有key
# print(dict1.values()) #获取所有value
# print(dict1.items()) #获取所有键值对
#
# # 删除
# # 方式一：
# num = dict1.pop("崩坏·因缘精灵")
# print(num)
# print(dict1)
#
# # 方式二：
# del dict1["绝区零"]
# print(dict1)
#
# # 遍历
# for k in dict1.keys():
#     print(f"{k},{dict1[k]}")
# print("---------------------------------")
# for d in dict1.items():
#     print(f"{d[0]},{d[1]}")
# print("---------------------------------")
# for key, value in dict1.items():
#     print(f"{key}: {value}")





"""
案例：
开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询和统计功能。系统使用嵌套字典结构存储商品数据，通过控制台菜单与用户交互。
具体功能如下：
    1．添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
    2．修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
    3．删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
    4．查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
    5．退出购物车

结构： shopping_cart = {"Meta80": {"price": 6999, "num": 2}, "鼠标": {...}}
"""
# shopping_cart = {}
# menu = """
# ############## 购物车管理系统 ###############
# #               1.添加购物车                #
# #               2.修改购物车                #
# #               3.删除购物车                #
# #               4.查询购物车                #
# #               5.退出购物车                #
# ###########################################
# """
#
# print("欢迎使用购物车管理系统~")
#
# while True:
#     # 1.制作菜单
#     print(menu)
#
#     # 2.执行的具体操作
#     choice = input("请选择要执行的操作(1-5):")
#
#     match choice:
#         case "1":  # 1.添加购物车
#             goods_name = input("请输入商品名称：")
#             goods_price = float(input("请输入商品价格："))
#             goods_num = int(input("请输入商品数量："))
#
#             # 如果商品存在，则不执行添加，提示信息
#             if goods_name in shopping_cart:
#                 print("该商品已存在，请重新选择！")
#             else:
#                 shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#                 print("商品添加完毕~")
#         case "2":  # 2.修改购物车
#             goods_name = input("请输入要修改的商品名称：")
#             # 如果商品不存在，则提示错误信息，重新选择
#             if goods_name not in shopping_cart:
#                 print("该商品不存在，请重新选择！")
#                 continue
#
#             goods_price = float(input("请输入商品最新的价格："))
#             goods_num = int(input("请输入商品最新的数量："))
#
#             shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#             print("商品修改完毕~")
#         case "3":  # 3.删除购物车
#             goods_name = input("请输入要删除的商品名称：")
#
#             # 如果商品不存在，则提示错误信息，重新选择
#             if goods_name not in shopping_cart:
#                 print("该商品不存在，请重新选择！")
#             else:
#                 del shopping_cart[goods_name]
#                 print("商品删除完毕~")
#         case "4":  # 4.查询购物车
#             for goods_name in shopping_cart.keys():
#                 goods_info = shopping_cart[goods_name]
#                 print(f"商品名称：{goods_name},商品价格：{goods_info['price']},商品数量：{goods_info['num']}")
#         case "5":  # 5.退出购物车
#             print("Bye ~")
#             break;
#         case _:  # 匹配其它操作
#             print("非法操作，不支持！")


"""
基于现有知识开发一个教务管理系统
 
开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
1．添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
 
2．修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
 
3．删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
 
4．查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
 
5．列出所有学生：遍历所有学生信息并输出。
 
6．统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
 
7．退出系统。
"""

menu = """
############## 购物车管理系统 ###############
#               1.添加学生信息                #
#               2.修改学生信息                #
#               3.删除学生信息                #
#               4.查询学生信息                #
#               5.列出所有学生                #
#               6.统计班级成绩                #
#               7.退出系统                   #
###########################################
"""
student_news = {"cd":{"chinese":15,"math":16,"english":76},"ln":{"chinese":42,"math":76,"english":68}}
while True:
    # 1.制作菜单
    print(menu)

    # 2.执行的具体操作
    choice = input("请选择要执行的操作(1-7):")

    match choice:
        case "1":
            s_name = input("请输入学生姓名：")
            s_chinese = float(input("请输入语文成绩："))
            s_math = float(input("请输入数学成绩："))
            s_english = float(input("请输入英语成绩："))
            # 如果学生存在，则不执行添加，提示信息
            if s_name in student_news:
                print("该学生已存在，请重新选择！")
            else:
                student_news[s_name] = {"chinese": s_chinese, "math": s_math, "english": s_english}
                print(f"添加【{s_name}】添加完毕~")
        case "2":
            s_name = input("请输入需更改的学生姓名：")
            if s_name not in student_news:
                print("该学生不存在，请重新输入！")
                continue
            s_chinese = float(input("请输入正确的语文成绩："))
            s_math = float(input("请输入正确的数学成绩："))
            s_english = float(input("请输入正确的英语成绩："))
            student_news[s_name] = {"chinese":s_chinese, "math":s_math, "english":s_english}
            print("学生信息修改完毕!")
        case "3":
            s_name = input("请输入需删除的学生姓名：")
            if s_name not in student_news:
                print("该学生不存在，请重新输入！")
                continue
            del student_news[s_name]
            print("学生删除完毕！")
        case "4":
            s_name = input("请输入需查询的学生姓名：")
            if s_name not in student_news:
                print("该学生不存在，请重新输入！")
                continue
            s_cj = student_news[s_name]
            print(f"学生名称：{s_name},语文成绩：{s_cj["chinese"]},数学成绩：{s_cj["math"]},英语成绩：{s_cj["english"]}")
        case "5":
            for s_name,s_cj in student_news.items():
                print(f"学生名称：{s_name},语文成绩：{s_cj["chinese"]},数学成绩：{s_cj["math"]},英语成绩：{s_cj["english"]}")
        case "6":
            if not student_news:
                print("暂无学生数据！")
                break

            chi_list = []
            mat_list = []
            eng_list = []

            for name, s in student_news.items():
                chi_list.append([s["chinese"], name])
                mat_list.append([s["math"], name])
                eng_list.append([s["english"], name])

            # 语文
            chi_list.sort()
            max_chi, max_chi_name = chi_list[-1]
            min_chi, min_chi_name = chi_list[0]
            avg_chi = sum(i[0] for i in chi_list) / len(chi_list)

            # 数学
            mat_list.sort()
            max_mat, max_mat_name = mat_list[-1]
            min_mat, min_mat_name = mat_list[0]
            avg_mat = sum(i[0] for i in mat_list) / len(mat_list)

            # 英语
            eng_list.sort()
            max_eng, max_eng_name = eng_list[-1]
            min_eng, min_eng_name = eng_list[0]
            avg_eng = sum(i[0] for i in eng_list) / len(eng_list)

            print("====班级统计====")
            print(f"语文 最高{max_chi}({max_chi_name}) 最低{min_chi}({min_chi_name}) 平均{avg_chi:.2f}")
            print(f"数学 最高{max_mat}({max_mat_name}) 最低{min_mat}({min_mat_name}) 平均{avg_mat:.2f}")
            print(f"英语 最高{max_eng}({max_eng_name}) 最低{min_eng}({min_eng_name}) 平均{avg_eng:.2f}")
        case "7":
            print("感谢使用！")
            break

























