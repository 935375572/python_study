"""
循环控制语句
continue ： 退出当前循环
break : 结束本次循环
"""

age = 19
for num in range(30):
    if num == 3:
        continue
    print(num)


age1 = 19
for num in range(30):
    if num == 3:
        break
    print(num)
