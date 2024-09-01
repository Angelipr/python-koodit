import random
arvottu = random.randint (1,10)
while True:
    luku = int(input('Anna numero: '))
    if luku < arvottu:
        print('Liian pieni arvaus')
    elif luku > arvottu:
        print('Liian suuri arvaus')
    else:
        print('Oikea arvaus!')
        break