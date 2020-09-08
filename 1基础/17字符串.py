"""字符串分片操作"""
title = "我最亲爱的，你过的怎么样啊"
sub_1 = title[7]
sub_2 = title[0:4]
print(sub_1)
print(sub_2)

print("\n")

"""字符串统计"""
title = "我最亲爱的，你过的怎么样啊"
print(len(title))
print(max(title))
print(min(title))

"""使用in 运算符"""
if "我" in title:
    print("哈哈哈哈哈")

"""使用format() 函数格式化字符串"""
name = "姚小达"
age = 109
score = 100
msage = "姓名是：{}、 年龄：{}、 成绩：{}".format(name, age, score)
print(msage)

name = "姚小达"
age = 109
score = 100
msage = "姓名是：{name_param}、 年龄：{age_param}、 成绩：{score_param}".format(age_param=age, name_param=name, score_param=score)
print(msage)

# 字符串大小写函数
info = "sdfskdfjskdbk"
print(info.upper())         			# 字符串转大写
print(info.lower())                     # 字符串转小写
print(info.title())
print("sdf".capitalize())