for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            if a * 100 + b * 10 + c == a * a * a + b * b * b + c * c * c:
                print(a * 100 + b * 10 + c)
