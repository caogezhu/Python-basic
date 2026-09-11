# # 案例1：定义一个函数：根据传入的底和高计算三角形的面积（三角形面积 = 底 * 高 / 2）。
# def triangle_area(b, h):
#     """
#     根据传入的底和高计算三角形面积
#     :param b: 底长
#     :param h: 高
#     :return: 三角形面积
#     """
#     return b * h / 2
#
#
# print("底长为 30，高度为 20 的三角形面积：", triangle_area(b=30, h=20))
#
#
# # 案例2：定义一个函数：计算传入的字符串中元音字母的个数（元音字母为 aeiouAEIOU）。
# def count_aeiou(s):
#     """
#     统计字符串中元音字母的个数
#     :param s: 字符串
#     :return: 元音字母的个数
#     """
#     num = 0
#     for w in s:
#         if w in "aeiouAEIOU":
#             num += 1
#     return num
#
#
# print(count_aeiou("Hello Python Hello World OK"))
#
#
# # 案例3：定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)，并返回。
# def calc_score(score_list):
#     """
#     计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分
#     :param score_list: 分数列表
#     :return: 最高分，最低分，平均分
#     """
#     max_s = max(score_list)
#     min_s = min(score_list)
#     avg_s = round(sum(score_list) / len(score_list), 1)
#     return max_s, min_s, avg_s
#
#
# s_list = [589, 609, 605, 643, 677, 455, 477, 489, 503]
# max_score, min_score, avg_score = calc_score(s_list)
# print("最高分：", max_score)
# print("最低分：", min_score)
# print("平均分：", avg_score)

# 1. 根据分数返回等级
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"


# 2. 判断回文字串
def is_palindrome(s):
    return s == s[::-1]


# 3. 秒转 时、分、秒
def sec_to_hms(total_sec):
    h = total_sec // 3600
    m = (total_sec % 3600) // 60
    s = total_sec % 60
    return f"{h}小时{m}分{s}秒"


# 4. 判断三角形类型
def tri_type(a, b, c):
    # 判断能否构成三角形
    if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "不能构成三角形"
    if a == b == c:
        return "等边三角形"
    elif a == b or a == c or b == c:
        return "等腰三角形"
    else:
        return "普通三角形"


# --------测试代码--------
print(get_grade(85))
print(is_palindrome("level"))
print(sec_to_hms(3700))
print(tri_type(3, 3, 3))























