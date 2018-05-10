for x in range(1, 10):
    for y in range(1, x + 1):

        print("".join(" ".join("%s*%s=%2s" % (x, y, x * y))))
