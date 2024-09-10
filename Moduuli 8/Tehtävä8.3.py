import geopy
import mysql.connector

def get_airport_by_ICAOT(ICAO):
    sql = f'SELECT latitude_deg, longitude_deg FROM airport WHERE ident = "{ICAO}"'
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

eka = input('Anna ensimmäine ICAO koodi: ')
toka = input('Anna toinen ICAO koodi:')

from geopy import distance
sijainti1 = get_airport_by_ICAOT(eka)
sijainti2 = get_airport_by_ICAOT(toka)
print(f'{distance.distance(sijainti1, sijainti2).km} km')
