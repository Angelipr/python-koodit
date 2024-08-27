kuhanpituus = float(input('Kuinka pitkä kuha on: '))
alamitta = 37
erotus = alamitta - kuhanpituus
if kuhanpituus < alamitta:
    print('laske kuha takaisin järveen')
    print(f'Kuhan mitasta puuttuu {erotus}')
