def F(a, b):
    if b == 0:
        return a
    if (a>=b) and (b>0):
       return F(a-b,b)
    if b>a:
        return F(b,a)
for a in range(15,31):
    print(a,F(a,15))
