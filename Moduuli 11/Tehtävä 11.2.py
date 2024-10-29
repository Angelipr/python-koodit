class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = int(huippunopeus)
        self.nopeusnyt = 40
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

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti_kwh):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti_kwh = akkukapasiteetti_kwh

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki_l):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki_l = bensatankki_l


sähkö = Sähköauto("ABC-15", 180, 52.5)
poltto = Polttomoottoriauto("ABC-123", 165, 32.3)

#sähkö.kiihdytä(100)
sähkö.kulje(3)
poltto.kulje(3)
print(f'Sähköauto on kulkenut {sähkö.kuljettumatka} km')
print(f'Polttomoottori auto on kulkenut {poltto.kuljettumatka} km')