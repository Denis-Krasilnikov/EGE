c = ['0', '1', '2', '3', '4', '5', '6', '7', '8', ]
chet = ['2', '4', '6', '8', ]
nec = ['1', '3', '5', '7']
count = 0
flag = 0
for q in chet:
    for w in nec:
        for e in chet:
            for r in nec:
                for t in chet:
                    for y in nec:
                        for u in chet:
                            for i in nec:
                                for o in chet:
                                    for p in nec:
                                        for a in chet:
                                            num = q + w + e + r + t + y + u + i + o + p + a
                                            for x in range(len(num)):
                                                m = num[x]
                                                if num.count(m) < 5:
                                                    flag +=1
                                                if flag == 11:
                                                    count+=1
                                            flag = 0

print(count)
