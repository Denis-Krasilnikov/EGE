for a in range(128):
    f = True
    for m in range(128):
        for n in range(128):
            if not (((2*m + 3*n) > 43) or (m < a) or (n <= a)):
                f = False
    if f:
        print(a)