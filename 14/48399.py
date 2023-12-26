for x in '0123456789ABCD':
    res = int(f'3D4{x}', 16) + int(f'4{x}C4', 14)
    if res % 154 == 0:
        print(res/154, int(x,16))
