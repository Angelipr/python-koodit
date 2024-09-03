
def muunnos(maara):
    kerto = maara * 3.785
    return kerto

while True:
    maara = float(input("Gallonamäärä: "))
    if maara < 0:
        break
    litra = muunnos(maara)
    print(litra)