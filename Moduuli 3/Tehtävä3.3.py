sukupuoli = input("Sukupuoli: ")
hemoglobiini = float(input("Hemoglobiini arvo: "))
nainen_hemogma = 116
nainen_hemoko = 176
mies_hemoma = 133
mies_hemoko = 196
if sukupuoli == "nainen":
    if nainen_hemogma < hemoglobiini < nainen_hemoko:
        print('Hemoglobiiniarvot ovat normaalit')
    elif hemoglobiini <= nainen_hemogma:
        print('Hemoglobiiniarvot ovat matalat')
    elif hemoglobiini >= nainen_hemoko:
        print('Hemoglobiiniarvot ovat korkeat')
if sukupuoli == "mies":
    if mies_hemoma < hemoglobiini < mies_hemoko:
        print('Hemoglobiiniarvot ovat normaalit')
    elif hemoglobiini <= mies_hemoma:
        print('Hemoglobiiniarvot ovat matalat')
    elif hemoglobiini >= mies_hemoko:
        print('Hemoglobiiniarvot ovat korkeat')
