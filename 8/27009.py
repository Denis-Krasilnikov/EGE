import itertools

listString = itertools.product("НИКОЛАЙ", repeat=4)
count = 0
for str in listString:
    line = "".join(str)
    if line[0] != 'Й' and (line.count('И') + line.count('О') + line.count('А') > 0):
        count += 1
print(count)
