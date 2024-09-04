def kokonaisluvut(luvut):
    parillisetluvut = []
    for luku in luvut:
        if luku % 2 == 0:
            parillisetluvut.append(luku)
    return parillisetluvut

kokonaisluvu = [1,2,3,4,5,6,7,8,9]

print(kokonaisluvut(kokonaisluvu))