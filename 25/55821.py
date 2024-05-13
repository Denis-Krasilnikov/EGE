from fnmatch import fnmatch

for x in range(0,10**8,273):
    if fnmatch(str(x), r"12??36*1"):
        print(x)
