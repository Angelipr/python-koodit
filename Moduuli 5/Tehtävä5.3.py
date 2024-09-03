
luku = int(input('Anna luku:'))
muuttuja = 1
if luku == 1 or luku == 0:
    print('Luku ei ole alkuluku')
    exit()
for n in range(2, luku):
    if (luku%n) == 0:
        muuttuja += 1
        break
if muuttuja == 2:
    print('Luku ei ole alkuluku')
elif muuttuja == 1:
    print('Luku on alkuluku')
