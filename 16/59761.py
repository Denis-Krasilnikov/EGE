import sys
sys.setrecursionlimit(5000)
def F(n):
    if n < 11:
        return 10
    if n == 11 or n > 11:
        return n + F(n - 1)


print(F(2124) - F(2122))
