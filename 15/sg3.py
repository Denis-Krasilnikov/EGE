for a in range(128):
    f = True
    for x in range(128):
        for y in range(128):
            if not ((3 * x + y > 48) or (x > y) or (4 * x + y < a)):
                f = False
                print(((3 * x + y > 48) or (x > y) or (4 * x + y < a)), a)
