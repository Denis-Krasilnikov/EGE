for num in range(2, 10000):
    b = bin(num)[2:]
    b = b.replace('0', '*')
    b = b.replace('1', '0')
    b = b.replace('*', '1')
    b = b.lstrip('0')
    if len(b) > 0:
        res = int(b, 2)
        if num - res == 979:
            print(num)
