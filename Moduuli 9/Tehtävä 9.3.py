class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeusnyt = 0
        self.kuljettumatka = 2000

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



uusi = Auto('ABC-123', 142)
#uusi.kiihdytä(30)
uusi.kiihdytä(60)
#uusi.kiihdytä(50)
print(uusi.nopeusnyt)

#hätäjarrutus
#uusi.kiihdytä(-200)
#print(uusi.nopeusnyt)
uusi
uusi.kulje(1.5)
print(uusi.kuljettumatka)
#print(f'Auton rekisteritunnus on {uusi.rekisteritunnus} ja huippunopeus on {uusi.huippunopeus} km/h')

