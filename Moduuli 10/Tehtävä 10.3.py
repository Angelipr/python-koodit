class Hissi:
    def __init__(self, ylinkerros, alinkerros):
        self.ylinkerros = ylinkerros
        self.alinkerros = alinkerros
        self.nykyinen = alinkerros


    def siirry_kerrokseen(self, kerros):
        #hissi ei voi ylittää ylintä kerrosta
        if kerros > self.ylinkerros:
            kerros = self.ylinkerros

        # Hissi ei voi alittaa alinta kerrosta
        elif kerros < self.alinkerros:
            kerros = self.alinkerros

        while self.nykyinen != kerros:
            if kerros > self.nykyinen:
                self.kerros_ylös(kerros)
            elif kerros < self.nykyinen:
                self.kerros_alas(kerros)
            print(f'Hissi on kerroksessa {self.nykyinen}')

    def kerros_ylös(self, kerros):
        if kerros > self.nykyinen :
            self.nykyinen += 1
        return self.nykyinen

    def kerros_alas(self, kerros):
        if self.nykyinen > kerros :
            self.nykyinen -= 1
        return self.nykyinen

class Talo:
    def __init__(self, ylinkerros, alinkerros, hissien_määrä):
        self.ylinkerros = ylinkerros
        self.alinkerros = alinkerros
        #lista hisseistä
        self.hissit = [Hissi(ylinkerros, alinkerros) for i in range(hissien_määrä)]


    def aja_hissiä(self, numero, kohdekerros):
        if 0 <= numero < len(self.hissit):
            print(f'\nHissi {numero} ajaa kerrokseen {kohdekerros}')
            self.hissit[numero].siirry_kerrokseen(kohdekerros)
        else:
            print("Hissiä ei ole olemassa")

    def palohälytys(self):
        print('\nPALOHÄLYTYS!')
        for i, hissi in enumerate(self.hissit):
            print(f'\nHissi {i} siirtyy alimpaan kerrokseen ')
            hissi.siirry_kerrokseen(self.alinkerros)


talo = Talo(alinkerros=0, ylinkerros=10, hissien_määrä=2)
talo.aja_hissiä(1, 5)
talo.aja_hissiä(0, 8)
talo.palohälytys()