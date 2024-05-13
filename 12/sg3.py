for n in  range(2,100):
    sum = 0
    s = '2' + '5' * n
    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '5', 1)
        if '355' in s:
            s = s.replace('355', '52', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)
    for i in range(len(s)):
        sum = int(s[i]) + sum
    if sum == 17:
        print(n, s)


