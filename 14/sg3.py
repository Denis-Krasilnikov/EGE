m = 0
for x in range(0, 80):
    for z in range(0, 80):
        for y in range(0, 80):
            num = (1 * 80 ** 0) + (2 * 80 ** 1) + (6 * 80 ** 2) + (z * 80 ** 3) + (4 * 80 ** 4) + (5 * 80 ** 5) + (
                        7 * 80 ** 6) + (x * 80 ** 7) + (3 * 80 ** 8) + (8 * 80 ** 9) + (9 * 80 ** 10)
            num2 = (1 * 80 ** 0) + (0 * 80 ** 1) + (9 * 80 ** 2) + (4 * 80 ** 3) + (y * 80 ** 4) + (5 * 80 ** 5) + (
                        5 * 80 ** 6) + (3 * 80 ** 7) + (z * 80 ** 8) + (7 * 80 ** 9) + (8 * 80 ** 10)
            if (num * num2) % 79 == 0:
                c = (z * 80 ** 0) + (y * 80 ** 1) + (x * 80 ** 2)
                m = max(m, c)
print(m)
