def f(s):
    while '111' in s or '88888' in s:
        if '111' in s:
            s = s.replace('111', '88', 1)
        if '88888' in s:
            s = s.replace("88888", "8", 1)
    return s


print(f("1"*100))

