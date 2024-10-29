class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, sivumäärä, kirjoittaja):
        self.sivumäärä = sivumäärä
        self.kirjoittaja = kirjoittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f'{self.nimi} {self.kirjoittaja} {self.sivumäärä} sivua\n')


class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f'{self.nimi} {self.päätoimittaja}\n')


julkaisut = []
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(Kirja("Hytti n:o 6", "200", "Rosa Liksom"))

for j in julkaisut:
    j.tulosta_tiedot()