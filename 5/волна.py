m = []
for n in range(1000000):
    i = bin(n)[2::]
    if n % 2 == 0:
        r = i + '01'
    else:
        r = '1' + i + '1'
    if int(r,2) > 156 and int(r,2) < 200:
        print(n,int(r,2))
