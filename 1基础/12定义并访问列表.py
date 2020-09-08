# 定义并访问列表
names = ["张三", "李四", "王五", "赵六"]

# 访问列表
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# 使用for循环遍历列表
for name in names:
    print(name)

# 通过索引修改列表的内容
names[0] = "无哈"
for name in names:
    print(name)

print("huanhang\n")

# 在列表上使用乘法操作
names = ["张三", "李四", "王五", "赵六"] * 3   # 数据重复3次
print(names)

# 数据分片操作
numbers = ["A", "B", "C", "D", "E", "F", "I", "J", "K"] # 定义列表
print(numbers[0:3])
print(numbers[-9:-2])
print(numbers[3:])
print(numbers[:3])
print(numbers[2:8:2])  # 设置步长为2

numbers[2:6] = ["1", "2", "3"]  # 分片内容替换
print(numbers)


