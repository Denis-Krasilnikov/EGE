def f(s):
    while "00" not in s:
        s = s.replace('01', '220', 1)
        s = s.replace('02', '1013', 1)
        s = s.replace('03', '120', 1)
    return s


for x in range(100):
    for y in range(100):
        for d in range(100):
            g = '0' + "1" * x + '2' * y + "3" * d + "0"
            c = f(g)
            if c.count("1") == 13 and c.count("2") == 18:
                print(g, c)
                print(2 + x + y + d)
