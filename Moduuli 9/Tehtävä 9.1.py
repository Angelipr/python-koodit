class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeusnyt = 0, kuljettumatka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeusnyt = nopeusnyt
        self.kuljettumatka = kuljettumatka

uusi = Auto('ABC-123', '142 km/h')

print(f'Auton rekisteritunnus on {uusi.rekisteritunnus} ja huippunopeus on {uusi.huippunopeus}')
