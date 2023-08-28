for a in range(128):
    f = True
    for x in range(128):
        if not ((x & 105 == 0) <= ((x & 58 != 0) <= (x & a != 0))):
            f = False
    if f:
        print(a)
