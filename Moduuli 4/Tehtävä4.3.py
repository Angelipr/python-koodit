luku = input('Anna luku: ')
pienin = suurin = luku
while luku != "":
    luku = input('Anna luku: ')
    if luku == "":
        break
    if (luku) < (pienin):
        pienin = luku
    if (suurin) < (luku):
        suurin = luku
print(f"Suurin oli: {suurin} ja pienin: {pienin}")