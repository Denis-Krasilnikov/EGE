with open('1_24.txt', 'r') as s:
    f = s.readline()
    count = 0
    mcount = 0
for i in range(1,len(f)):
    if (f[i] == "A" or f[i] == "B" or f[i] == "C") and (f[i-1] == "A" or f[i-1] == "B" or f[i-1] == "C"):
        mcount = max(mcount, count)
        count = 0
    count +=1
print(mcount)
