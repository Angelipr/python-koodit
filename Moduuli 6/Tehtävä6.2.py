import random
lukumäärä = int(input('Anna maksimisimläluku: '))
def noppa(lukumäärä):
    while True:
        heitto = int(random.randint(1,lukumäärä))
        print(heitto)
        if heitto == lukumäärä:
            break
noppa(lukumäärä)