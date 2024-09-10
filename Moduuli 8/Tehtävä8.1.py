import mysql.connector

def get_airport_by_icao(icao):
    sql = f'SELECT name, municipality FROM airport WHERE ident = "{icao}"'
    #print(sql)
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

koodi = input('Anna lentokenttä koodi: ')
airport = (get_airport_by_icao(koodi))
print(f"Nimi on: {airport[0][0]} ja paikkakunta: {airport[0][1]}")