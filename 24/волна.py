with open('волна.txt', 'r') as s:
    f = s.readline()
c = 1
m = 0
f = f.replace('A','*')
f = f.replace('B','*')
f = f.replace('C','*')
f = f.replace('6','1')
f = f.replace('7','1')
f = f.replace('8','1')
f = f.replace('9','1')
for i in range(1,len(f)):
    if (f[i] == '1' and f[i-1] == "*" ) or (f[i] == '*' and f[i-1] == "1" ):
        c+=1
    else:
        m = max(c,m)
        c=1
print(m)
