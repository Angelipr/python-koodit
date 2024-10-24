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



class Kilpailu:
    def __init__(self, nimi, pituus_km, määrä):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.määrä = määrä
        self.autot = []
        for i in range(1, määrä + 1):
            rekisteritunnus = f'ABC-{i}'
            huippunopeus = random.randint(100, 200)
            self.autot.append(Auto(rekisteritunnus, huippunopeus))


    def tunti_kuluu(self):
            for auto in self.autot:
                auto.kiihdytä(random.randint(-10, 15))
                auto.kulje(1)
                print(f'{auto.rekisteritunnus} nopeus on {auto.nopeusnyt} km/h ja on kulkenut {auto.kuljettumatka}')


    def tulosta_tilanne(self):
        print(f'\nTilanne: ')
        for auto in self.autot:
            print(f'{auto.rekisteritunnus}: {auto.kuljettumatka} km kuljettuna')


    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettumatka >= self.pituus_km:
                return True
        return False


kilpailu = Kilpailu("Tervetuloa suureen romuralliin!", 8000, 10)
tunnit = 0

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit = tunnit + 1
    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()



