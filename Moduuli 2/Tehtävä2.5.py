luotiin_str = float(input("Anna luodit: "))
naulain_str = float(input("Anna naulat: "))
leiviskäin_srt = float(input("Anna leiviskät: "))
luoti_g = 13.3
naula_luoteina = 32
leiviskä_nauloina = 20
summa = (leiviskäin_srt*leiviskä_nauloina*naula_luoteina*luoti_g) + (naulain_str*naula_luoteina*luoti_g) + (luotiin_str*luoti_g)
kilogrammat = (summa//1000)
grammat = (summa % 1000)
print(f'Massa nykymittojen mukaan:\n{kilogrammat} kg ja {grammat} g')
