def F(a, b):
    if b == 0:
        return a
    if (a>=b) and (b>0):
       return F(a-b,b)
    if b>a:
        return F(b,a)
for a in range(123456798,1234):
    if F(a,15) == 1:
        print(a)