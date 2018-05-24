import random
n = input("请输入要分组的同学数量\n")
number1 = int(n)
n = input("请输入每组的人数\n")
number2 = int(n)
classmates = []
print("请输入要分组的同学的姓名\n每打完一个姓名就按一次回车")
for x in range(number1):
    name = input()
    classmates.append(name)
random.shuffle(classmates)
number3 = int(number1 / number2)
for x in range(number3):
    print("第%s组是：" % (x + 1), end=(" "))
    print(classmates[0 + x * number2:number2 * (x + 1)])
if number1 % number2 != 0:
    print("因为人数无法整除，所以剩下%s人自成一组" % (number1 % number2))
    print("第%s组是：" % (1 + (number3)), end=(" "))
    print(classmates[number1 - (number1 % number2):number1])
