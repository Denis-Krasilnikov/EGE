print("x y w z F")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = ((x or y) <= (y and z)) and ((w == x) or (w <= z))
            if f:
                print(x,y,w,z,f)