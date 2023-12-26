def f(s):
    while "01" in s or "02" in s:
        s = s.replace("02", '1110',1)
        s = s.replace('01', '220',1)
    return s


def K(n):
    k=0
    for i in range(2, n**0,5):
        if (n%i == 0):
            k=k+1
    if (k<=0):
        return True
    else:
        return False


g=0
for x1 in range(100):
    for x2 in range(100):
        s = '0' + x1 * '1' + x2 * '2'
        g = s.count('1') + (s.count('2')*2)
        if len(s) > 44 and K(g) == True:
            print(g)
            break

