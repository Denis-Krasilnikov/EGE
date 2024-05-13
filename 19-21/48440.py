def f(s, m):
    if s >= 103:
        return m % 2 == 0
    if m == 0:
        return 0
    h = []
    if (s+1)%3 != 0:
        h.append(f(s+1,m+1))
    if (s+2)%3 != 0:
        h.append(f(s+2,m-1))
    if (s*2)%3 != 0:
        h.append(f(s*2,m-1))

    if (m-1) %2 == 0:
        return any(h)
    else:
        return all(h)

print('19', [s for s in range(1,101) if f(s,2)])
print('20', [s for s in range(1,101) if f(s,3) and not f(s,1)])
print('21', [s for s in range(1,101) if f(s,4) and not f(s,2)])
