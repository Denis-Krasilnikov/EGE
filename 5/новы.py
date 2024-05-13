m = 0
for n in range(11000000):
    r = bin(n)[2::]
    if n % 5 == 0:
        r = r + bin(5)[2::]
    else:
        r = r + '1'
    if int(r,2) % 7 == 0:
        r = r + bin(7)[2::]
    else:
        r = r + '1'
    if int(r,2) < 1855663:
        m = max(m,n)
print(m)
