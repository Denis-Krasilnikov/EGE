def divs_count(n):
    divs = set()
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0:
            divs.add(div)
            divs.add(n // div)
    return sorted(divs)


for num in range(200000001, 200000100):
    divs = divs_count(num)
    if len(divs) > 5:
        p = divs[0] * divs[1] * divs[2] * divs[3] * divs[4]
        if p < num:
            print(p)
