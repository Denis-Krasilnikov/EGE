mas = [0] * 100000
for n in range(1, 1000):
    r = bin(n)[2::]
    o = n % 4
    r = r + bin(o)[2::]
    r = int(r,2)
    mas[r] = 1
count = 0
for i in range(100000 - 49):
    count = max(count, sum(mas[i:i+49]))
print(count)





