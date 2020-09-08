infos = []
print("初始的长度 %d" % len(infos))
infos.append("张三")  # 在列表末尾增加数据
infos.insert(0, "李四") # 指定索引增加数据
infos.extend(["王五", "赵六"])  # 扩充列表数据
print("扩充后的长度 %d" % len(infos))
for info in infos:
    print(info)

print("\n")

# 列表拷贝
msgs = infos.copy()
for msg in msgs:
    print(msg)

# 使用remove删除  根据值删除
infos.remove("李四")
print(infos)

# 使用pop方法让列表数据弹出
ma = infos.pop(1)  # 还可以继续使用被弹出的值
print(infos)
print(ma)

# 反转数据
numbers = [3, 5, 1, 6, 8, 9, 0]
numbers.reverse()
print(numbers)

# count()  统计出现的次数
ms = numbers.count(3)
print(ms)

# 使用index查找数据
ss = numbers.index(3)  # 从第0个开始查找
print(ss)


