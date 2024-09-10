import mysql.connector

def get_airport_by_iso_country(iso_country):
    sql = f'SELECT type, count(*) FROM airport WHERE iso_country = "{iso_country}"group by type'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='angeli',
    password='bixAIE-5Wk=P1&#P',
    autocommit=True
    )
maakoodi = input('Anna maakoodi: ')
maakoodi = get_airport_by_iso_country(maakoodi)
print(maakoodi)