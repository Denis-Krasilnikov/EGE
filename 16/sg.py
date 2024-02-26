def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n // 10) + n % 10
    if n % 2 != 0:
        return f(n // 10)


c = 0
for i in range(999,2000):
    print(i,f(i))
