def yh():
    L = [1]  # 作为三角形开头只有1的list
    while True:  # 无限循环
        yield L
        L = [L[x] + L[x + 1] for x in range(len(L) - 1)]
        L.insert(0, 1)  # 在开头插入1
        L.append(1)  # 在结尾插入1
        if len(L) > 10:  # 限制三角形的长度
            break  # 用于结束while ture语句的无限循环
for a in yh():
    print(a)