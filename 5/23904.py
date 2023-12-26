for num in range(1, 1000):
    i = bin(num)[2:]
    if num % 2 == 0:
        i = i + "00"
    else:
        i = i + "11"
    if int(i,2) > 134:
        print( num, i)
