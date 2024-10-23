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


uusi = Auto('ABC-123', 142)
uusi.kiihdytä(30)
uusi.kiihdytä(70)
uusi.kiihdytä(50)
print(uusi.nopeusnyt)

#hätäjarrutus
uusi.kiihdytä(-200)
print(uusi.nopeusnyt)
print(f'Auton rekisteritunnus on {uusi.rekisteritunnus} ja huippunopeus on {uusi.huippunopeus} km/h')

