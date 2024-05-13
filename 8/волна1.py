c = 0
for q in "01234":
    for w in "01234":
        for e in "01234":
            for r in "01234":
                for t in "01234":
                    num = q + w + e + r + t
                    c += 1
                    if num.count('4') <= 1:
                        if num.count('00') == 0:
                            print(num,c)
