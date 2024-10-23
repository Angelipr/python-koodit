import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeusnyt = 0
        self.kuljettumatka = 0

    def kiihdytä(self, nopeudenmuutos):
        self.nopeusnyt = self.nopeusnyt + nopeudenmuutos
        #katsoo että ei mene yli huippunopeuden
        if self.huippunopeus < self.nopeusnyt:
            self.nopeusnyt = self.huippunopeus
        #katsoo että nopeus hiljenee
        if self.nopeusnyt < 0:
            self.nopeusnyt = 0

    def kulje(self, tuntimäärä):
        self.kuljettumatka += self.nopeusnyt*tuntimäärä


autot = []
for i in range(1,11):
    rekisteritunnus = f'ABC-{i}'
    huippunopeus = random.randint(100,200)
    autot.append(Auto(rekisteritunnus, huippunopeus))
    #print(f'rekisteritunnus: {rekisteritunnus} ja huippunopeus: {huippunopeus}')

while True:
    for auto in autot:
        auto.kiihdytä(random.randint(-10,15))
        auto.kulje(1)
        print(f'{auto.rekisteritunnus} nopeus on {auto.nopeusnyt} km/h ja on kulkenut {auto.kuljettumatka}')
        if auto.kuljettumatka >= 10000:
            print('Peli loppui')
            break
    else:
        continue
    break