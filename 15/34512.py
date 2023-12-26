for a in range(200):
    f = True
    for x in range(2000):
        if not ((x & 77 != 0) <= ((x&12 == 0) <= (x&a != 0))):
            f = False
    if f:
        print(a)
