def f(x, y):
    # Ограничение "не содержит"
    if x > y or x == 14:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y) + f(x * 3, y)


# Ограничение "содержит"
print(f(1, 10) * f(10, 15))