import itertools

listString = itertools.permutations('ГЕОРГИЙ',  7)
p = set()
for str in listString:
    line = "".join(str)
    if line.count("ГГ") == 0:
        p.add(line)
print(len(p))
