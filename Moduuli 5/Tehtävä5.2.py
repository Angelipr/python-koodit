luvut = []
luku_str = input('Anna luku: ')
luku = int(luku_str)
suurin = pienin = luku
while luku_str != "":
    luvut.append(luku)
    luku_str = input('Anna luku: ')
    if luku_str != "":
        luku = int(luku_str)
luvut.sort(reverse=True)
print(luvut[0:5])