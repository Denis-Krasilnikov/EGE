import itertools  # if line.count("32") == 0 and line.count("23") == 0 and line.count("3") == 2:

listString = itertools.product("123456780", repeat = 5)
p = set()
for str in listString:
    line = "".join(str)
    if line.count("32") == 0 and line.count("23") == 0 and line.count("3") == 2 and line[0] != "0" and line.count("12") == 0 and line.count("21") == 0 and line.count("52") == 0 and line.count("25") == 0 and line.count("72") == 0 and line.count("27") == 0:
        p.add(line)
print(len(p))
