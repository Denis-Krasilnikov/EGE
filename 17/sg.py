f =list(map(int, open('17.txt').readlines()))

count =0
for i in range(2,len(f)):
    if (f[i] / 1000 > 1) and ((f[i] %3 ==0) or
