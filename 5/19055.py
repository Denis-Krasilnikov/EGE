for N in range(1, 1000):
    i = bin(N)[2:]
    count = i.count("1")
    count = count % 2
    if count == 0:
        i = i + "0"
    else:
        i = i + "1"
    count = i.count("1")
    count = count % 2
    if count == 0:
        i = i + "0"
    else:
        i = i + "1"
    if int(i, 2) > 97:
        print(int(i, 2), i)
