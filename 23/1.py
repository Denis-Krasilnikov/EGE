def f(x, y):
    # Ограничение "не содержит"
    if x > y or x == 14:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y) + f(x * 3, y)


# Ограничение "содержит"
print(f(1, 10) * f(10, 15))

"""
a = [0] * 1000
a[1] = 1
for i in range(1, 11):
    a[i + 1] += a[i]
    a[i + 2] += a[i]
    a[i * 3] += a[i]
d = a[10]
a = [0] * 1000
a[10] = d
for i in range(10, 16):
    a[i + 1] += a[i]
    a[i + 2] += a[i]
    a[i * 3] += a[i]
    a[14] = 0
print(a[15])
"""