def f(s, m, to):
    if s >= 103:
        return m % 2 == to % 2
    if m == to:
        return False
    h = []
    if (s + 1) % 3 != 0:
        h.append(f(s + 1, m + 1, to))
    if (s + 2) % 3 != 0:
        h.append(f(s + 2, m + 1, to))
    if (s * 2) % 3 != 0:
        h.append(f(s * 2, m + 1, to))

    return any(h) if (m + 1) % 2 == to % 2 else all(h)


print(f'19: {min(s for s in range(1, 101) if not f(s, 0, 1) and f(s, 0, 2))}')
print(f'20: {[s for s in range(1, 106) if not f(s, 0, 1) and f(s, 0, 3)]}')
print(f'21: {min(s for s in range(1, 106) if not f(s, 0, 2) and f(s, 0, 4))}')
