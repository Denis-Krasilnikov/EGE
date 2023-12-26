"""
def sum(num):
    s = 0
    y = str(num)
    for i in y:
        s = s + int(i)
    return s


for n in range(17, 18):
    i = bin(n)[2:]
    g = sum(n)
    if g % 2 == 0:
        i = i + "0"
    else:
        i = i + "1"
    n = int(i,2)
    g = sum(n)
    i = bin(n)[2:]
    if g % 2 == 0:
        i = i + "0"
    else:
        i = i + "1"
    n = int(i,2)
    g = sum(n)
    i = bin(n)[2:]
    if g % 2 == 0:
        i = i + "0"
    else:
        i = i + "1"
    q = int(i,2)
    print(q)
"""

def sum(num):
    s = 0
    y = str(num)
    for i in y:
        s = s + int(i)
    return s


for n in range(1, 100):
    i = bin(n)[2:]
    i += str(sum(int(i, 2)) % 2)
    i += str(sum(int(i, 2)) % 2)
    i += str(sum(int(i, 2)) % 2)
    print(int(i,2)//n, n)