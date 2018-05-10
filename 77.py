import random
x = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
for y in range(1, 10):
    i = (random.randint(1, 5))
    print(x[i],end=(" "))