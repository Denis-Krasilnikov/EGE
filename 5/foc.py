for i in range(1, 100):
    s = bin(i)[2:]
    s = str(s)
    if s.count('1') % 2 == 0:
        s = "10" + s[2:] + '1'
    else:
        s = '1' + s[:-1] + '11'
    r = int(s, 2)
    if r > 85:
        print(i)
        break
