def f(s):
    while "00" not in s:
        s = s.replace('01', '210', 1)
        s = s.replace('02', '320', 1)
        s = s.replace('03', '3012', 1)
    return s


for x1 in range(100):
    for x2 in range(100):
        for x3 in range(100):
            s = '0' + x1 * '1' + x2 * '2' + x3 * '3' + '0'
            s = f(s)
            if s.count('1') == 26 and s.count('2') == 54 and s.count('3') == 48:
                print(x1 + x2 + x3 + 2)

