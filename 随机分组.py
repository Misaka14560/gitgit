import random
import re
n = input("请输入要分组的同学数量\n")
number1 = int(n)
n = input("请输入每组的人数\n")
number2 = int(n)
name = input("请输入要分组同学的姓名 全选后粘贴即可\n")
pattern = re.compile(r"\w{2,3}")
classmates = pattern.findall(name)
random.shuffle(classmates)
number3 = int(number1 / number2)
for x in range(number3):
    print("第%s组是：" % (x + 1), end=(" "))
    print(classmates[0 + x * number2:number2 * (x + 1)])
if number1 % number2 != 0:
    print("因为人数无法整除，所以剩下%s人自成一组" % (number1 % number2))
    print("第%s组是：" % (1 + (number3)), end=(" "))
    print(classmates[number1 - (number1 % number2):number1])
