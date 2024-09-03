import random
luvut = []
arpaluku = random.randint(1, 6)
arpalukujen = float(input('Anna arpakuutioiden lukumäärä: '))
while arpalukujen > 0:
    luvut.append(random.randint (1,6))
    arpaluku = random.randint(1, 6)
    arpalukujen -= 1
print(sum(luvut))