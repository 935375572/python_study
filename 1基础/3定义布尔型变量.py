flag = True
print(type(flag))  # 获取变量的类型

if flag:
    print("你好啊老哥")  # 条件满足时执行

"""字符串的连接操作"""
info = "hello"
info = info + "world"
info += "python"
info = "优拓软件学院\"www.yootk.com\"\n\t极限IT程序员：\'www.jixianit.com\'"
print(info)

"""input()函数 获取键盘输入的数据"""
msg = input("请输入你的内容：")
wc = int(msg)  # 将字符串转为int类型
if wc > 12:
    print("可以了")
print(msg)  # 打印输入的内容


"""格式化输出"""
name = "abc"
age = 13
print("姓名是：%s 年龄有：%d" % (name, age))
