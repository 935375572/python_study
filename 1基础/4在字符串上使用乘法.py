info = "msg" * 5  # 重复5遍
print(info)

"""使用与逻辑运算符 and"""
name = "张三"
age = 13
result = name == "张三" and age == 13
print(result)

"""使用或逻辑运算符 or"""
name = "张三"
age = 13
result = name == "张三" or age == 13
print(result)

"""使用非逻辑运算符 and"""
name = "张三"
age = 13
result = not age == 13
print(result)


"""身份运算符：通过一个id()函数以获取数据对应的内存地址"""
nub = 2
print("nub的内存地址是：%s" % id(nub))
nub = 100
print("nub的内存地址是：%s" % id(nub))