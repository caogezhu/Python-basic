# 录入课程名称
course = input("请输入课程名称：")
score_list = []

while True:
    s = input("请录入成绩(q退出)：")
    if s == 'q':
        break
    # 转为浮点数存入列表
    score = float(s)
    score_list.append(score)

# 计算平均分
count = len(score_list)
avg = sum(score_list) / count
# 保留2位小数输出
print(f"课程{course}，共录入{count}份成绩，平均分{avg:.2f}")
