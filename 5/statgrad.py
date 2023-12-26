'''s=0
for num in range(10, 100):
    i = bin(num)[2:]
    o = num % 3
    d = bin(o)[2:]
    d = d.zfill(2)
    i = i + d
    g = bin(int(i, 2) % 5)[2:]
    g = g.zfill(3)
    i = i + g
    print(num, int(i, 2), int(i, 2)//num, int(i, 2)-num) '''
i1 = 1111111110 / 32
i2 = 1444444416 / 32
print(i2 - i1)

