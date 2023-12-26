def f(s):
    while "111" in s or "222" in s:
        if '111' in s:
            s = s.replace('111', '22', 1)
        if '222' in s:
            s = s.replace('222', '1', 1)
    return s


'''for x in range(201,500):
    s = "1" * x
    if f(s).count("1") == 0:
        print(s.count("1"))'''

print(f("1"*206))

