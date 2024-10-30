import requests

paikkakunta = input('Anna paikkakunta: ')
key =  'fc01fc417b0cda5eee7f0303e20f2fe3'

pyyntö = f"http://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&units=metric&appid={key}"

try:
    vastaus = requests.get(pyyntö).json()
    sää = vastaus['weather'][0]['description']
    lämpötila = vastaus['main']['temp']

    print(f"Säätila {paikkakunta}: {sää}")
    print(f"Lämpötila: {lämpötila}")

except requests.exceptions.RequestException as e:
    print("Error")