def f(x, y, c):
    if x > y:
        return 0
    if x == y and c == 1:
        return 1
    if c == 1:
        return f(x + 1, y, c) + f(x + 2, y, c)
    else:
        return f(x + 1, y, c) + f(x + 2, y, c) + f(x * 2, y, c + 1) + f(x * 3, y, c + 1)


print(f(1, 10, 0))
