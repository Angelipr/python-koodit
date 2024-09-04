
def pizza(halkaisija, hinta):
    import math
    säde1 = halkaisija/2
    ympyränala1 = (säde1**2*math.pi)/10000
    yksikkohinta = hinta/ympyränala1
    return yksikkohinta


halkaisija = float(input('Anna pizzan halkaisija sentteinä: '))
hinta = float(input('Anna pizzan hinta euroina: '))

halkaisija_2 = float(input('Anna toisen pizzan halkaisija sentteinä: '))
hinta_2 = float(input('Anna toisen pizzan hinta euroina: '))

yksikkohinta1 = pizza(halkaisija, hinta)
yksikkohinta2 = pizza(halkaisija_2, hinta_2)

print()
print(f'Ensimmäisen pizzan hinta per neliömetri: {yksikkohinta1:.2f} euroa')
print(f'Toisen pizzan hinta per neliömetri: {yksikkohinta2:.2f} euro')
print()
if yksikkohinta1 <  yksikkohinta2:
    print('Ensimmäisellä pizzalla on parempi hinta')
elif yksikkohinta2 < yksikkohinta1:
    print('Toisella pizza on parempi hinta')



