# 定义字典
infos = {"姓名": "张三", "年龄": "18", None: "空空的，什么都没有"}
print("姓名的内容：%s" % infos["姓名"])
print("年龄的内容：%s" % infos["年龄"])
print("None的内容：%s" % infos[None])

# 使用dict函数定义字典
info = dict([["姓名", "张三"], ["年龄", "13"]])
info1 = dict(name="张三", age="132")
print(info)
print(info1)

# 在字典中使用in进行判断
if "姓名" in infos:
    print("key对应的是%s, value对应的是%s"% ("姓名", infos["姓名"]))

print("\n")

# 获取字典中的全部key  keys函数
for info2 in infos.keys():
    print(info2)

# 获取字典中的全部数据 itmes函数
for key , value in infos.items():
    print("key的值是：%s, value的值是：%s" % (key, value))

