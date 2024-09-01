kayttajatunnus = 'python'
salasana = 'rules'
yritykset = 0
while yritykset < 5:
    asetakaytta = input('Anna käyttäjätunnus: ')
    asetasala = input('Anna salasana: ')
    if kayttajatunnus == asetakaytta and asetasala == salasana:
        print('Tervetuloa')
        break
    else:
        print('Pääsy evätty')
        yritykset += 1
    if yritykset == 5:
         break