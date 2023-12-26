for n in range(1, 1000):
    i = bin(n)[2:]
    if n % 3 == 0:
        i = i + i[-3:]
    else:
        c = bin(3 * (n % 3))[2:]
        i = i + c
    r = int(i, 2)
    if r<100:
        print(n, "    ", r)
