"""
No.	函数	类型	描述
1	len(seq)	函数	获取序列的长度
2	max(seq)	函数	获取序列中的最大值
3	min(seq)	函数	获取序列中的最小值
4	sum(seq)	函数	计算序列中的内容总和
5	any(seq)	函数	序列中有一个内容为True结果为True，全部为False时结果为False
6	all(seq)	函数	序列中有一个内容为False结果为False，全部为True时结果为True
"""
numbers = [1, 2, 3, 4, 5, 6, 7]
print("元素的个数： %d" % len(numbers))
print("元素最大值：%d" % max(numbers))
print("元素最小值： %d" % min(numbers))
print("元素总和：%d" % sum(numbers))

print(any((True, 1, "Hello")))  # 判断元组内的结果
print(all((True, None)))  # 判断元组内的结果

