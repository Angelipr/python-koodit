nimet = set()
while True:
    nimi = input("Syötä nimi: ")
    if nimi == "":
        break
    if nimi in nimet:
        print("aiemmin syötetty nimi")
    else:
        print("uusi nimi")
        nimet.add(nimi)

for nimi in nimet:
    print(nimi)