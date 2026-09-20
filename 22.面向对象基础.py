# 定义类 ----> 不推荐 动态的为对象添加属性
# class Car:
#     pass

# # 创建对象
# c1 = Car()

# # 动态的为对象添加属性
# c1.color = "red"
# c1.brand = "BMW"
# c1.name = "X5"
# c1.price = 500000

# print(c1)
# print(c1.brand)
# print(c1.__dict__)  # 会将对象中的所有属性以字典的形式输出来


# 定义类
class Car:  # 2 用法
    # __init__ 方法是初始化的方法，会在对象创建时自动调用，可以在该方法中为对象设置对应的属性；
    # self: 是第一个参数，表示当前所创建出来的实例对象
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car 类型的对象初始化完毕，对象属性已经添加完毕 .")


# 创建对象
c1 = Car(c_color="红色", c_brand="BMW", c_name="X7", c_price=800000)
print(c1.__dict__)

c2 = Car(c_color="白色", c_brand="奔驰", c_name="E300", c_price=450000)
print(c2.__dict__)
