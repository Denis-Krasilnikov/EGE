import itertools

listString = itertools.permutations('СВЕТЛАНА', 8)
count = 0
p = set()
for str in listString:
    line = "".join(str)
    if line.count('АА') == 0:
        p.add(line)
print(len(p))
