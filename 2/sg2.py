print('x y w z u F')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                for u in range(2):
                    f = ((x <= y) and (z == (not w))) <= (u == (x or z))
                    if not f:
                        print(x, y, w, z, u, f)

