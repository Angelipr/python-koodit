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


h = Hissi(ylinkerros=10, alinkerros=0)

print("Siirrytään kerrokseen 5:")
h.siirry_kerrokseen(5)

print("\nSiirrytään takaisin alimpaan kerrokseen:")
h.siirry_kerrokseen(0)
