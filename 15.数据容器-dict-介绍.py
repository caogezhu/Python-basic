# 字典 --> 键值对(key: value)存储
# 键(key)不能重复(如果重复，后面的值会覆盖前面的值)、必须是不可变类型(str,int,float,tuple)，不能是(列表list、集合set、字典dict)
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
dict1 = {"原神":1,"崩坏三":2,"崩铁":3,"绝区零":4}
print(dict1)

# 添加 - key不存在就是添加
dict1["崩坏·因缘精灵"] = 3
print(dict1)

# 添加 - key存在就是修改
dict1["崩坏·因缘精灵"] = 5
print(dict1)

# 查询
print(dict1["崩坏·因缘精灵"]) #根据key获取value
print(dict1.get("崩坏·因缘精灵")) #根据key获取value

print(dict1.keys()) #获取所有key
print(dict1.values()) #获取所有value
print(dict1.items()) #获取所有键值对

# 删除
num = dict1.pop("崩坏·因缘精灵")
print(num)
print(dict1)

del dict1["绝区零"]
print(dict1)

# 遍历
for k in dict1.keys():
    print(f"{k},{dict1[k]}")
for d in dict1.items():
    print(f"{d[0]},{d[1]}")
for key, value in dict1.items():
    print(f"{key}: {value}")
























