# 存学生：key=学生ID，value=姓名
students = {}
# 存课程：key=课程编号，value=课程名
courses = {}
# 存选课：key=学生ID，value=[选的课程编号列表]
select_course = {}


# 1.添加学生
def add_student(stu_id, name):
    students[stu_id] = name
    select_course[stu_id] = []


# 2.添加课程
def add_course(course_id, course_name):
    courses[course_id] = course_name


# 3.学生选课
def choose_course(stu_id, course_id):
    # 先判断学生和课程是否存在
    if stu_id in students and course_id in courses:
        select_course[stu_id].append(course_id)
        print("✅选课成功！")
    else:
        print("❌学生或者课程不存在！")


# 4.查看全部选课情况
def show_all():
    print("\n===== 选课情况 =====")
    for sid, name in students.items():
        print(f"学生ID:{sid} 姓名:{name}")
        clist = select_course[sid]
        if clist:
            for cid in clist:
                print(f"    已选课程：{cid} - {courses[cid]}")
        else:
            print("    还没有选课")
    print("====================")


# =====测试运行=====
if __name__ == "__main__":
    # 添加学生
    add_student("001", "张三")
    add_student("002", "李四")
    # 添加课程
    add_course("C01", "Python程序设计")
    add_course("C02", "大学物理")
    # 选课
    choose_course("001", "C01")
    choose_course("001", "C02")
    choose_course("002", "C02")
    # 查看所有选课
    show_all()
