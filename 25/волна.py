'''c = ['','0', '1', '2', '3', '4', '5', '6', '7', '8', '10']
c1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '10']
h = []
for q in c:
    for w in c:
        for e in c:
            for r in c:
                for t in c1:
                    n = '1' + q + w + e + r + '2322'+ t + "2"
                    if int(n) % 2024 == 0:
                        if n not in h:
                            h.append(n)
print(len(h))'''
from fnmatch import fnmatch

for x in range(0,10**10,2024):
    if fnmatch(str(x), r"1*2322?2"):
        print(x,x//2024)

