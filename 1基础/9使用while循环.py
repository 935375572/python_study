# 使用while循环实现1~100的累加
sum = 0  # 和
num = 1  # 初始值
while num <= 100:
    sum += num  # sum = sum + num
    num += 1  # num = num + 1
else:  # 循环执行完毕后执行此语句
    print(sum)
print("计算完毕")