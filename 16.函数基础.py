# 函数的定义
def out_line():
    print("--------------------------------")

#函数的调用
out_line()

# 函数的参数与返回值
# 函数1：计算圆的面积 -- 半径
# def circle_area(r):
#     area = 3.14 * r ** 2
#     return area

# area = circle_area(10)
# print(area)


# 函数2：计算长方形的面积 -- 长，宽
def rectangle_area(l,w):
    area = l * w
    return area

print(rectangle_area(20, 10))

# 函数3：计算圆的面积，周长 -- 半径 ----> 如果返回值有多个，多个返回值之间逗号分隔 ----> 多个返回值会封装到元组之中
def circle_area_len(r):
    return round(3.14**r,1),round(2*3.14**r,1)
al = circle_area_len(10)
print(al)
print(type(al))





















