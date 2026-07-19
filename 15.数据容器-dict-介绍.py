# 字典 --> 键值对(key: value)存储
# 键(key)不能重复(如果重复，后面的值会覆盖前面的值)、必须是不可变类型(str,int,float,tuple)，不能是(列表list、集合set、字典dict)
# value值可修改
dict1 = {"原神":1,"崩坏三":2,"崩铁":3,"绝区零":4}
print(dict1)
print(type(dict1))

#key必须是不可变类型(str,int,float,tuple)，不能是(列表list、集合set、字典dict)
dict2 = {0:670,1.5:522,('A','B'):252}
print(dict2)
print(type(dict2))

# 访问
print(dict1["原神"])
dict1["原神"]=5
print(dict1)
