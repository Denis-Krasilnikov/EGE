z = ['2', '4', '6','8']
x = ['1','3', '5','7']
c = 0
for q in z:
    for w in x:
        for e in z:
            for t in x:
                for y in z:
                    for u in x:
                        for r in z:
                            for o in x:
                                for p in z:
                                    num = q + w + e + t + y + u + r + o + p
                                    if num.count('1') < 4 and num.count('2') < 4 and num.count('3') < 4 and num.count('4') < 4 and num.count('5') < 4 and num.count('6') < 4 and num.count('7') < 4 and num.count('8') < 4:
                                        c += 1
print(c )
