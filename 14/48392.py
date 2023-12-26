for x in "012345678":
    for y in "012345678":
        res = (int(f'2{y}66{x}', 9) + int(f'{x}0{y}1', 12))
        if res % 170 == 0:
            print(res // 170)