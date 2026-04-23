#dzisiejsza pogoda do funkcji i zapytanie, czy to odpowiednia miejscowość



import requests


def prognoza(citys):
    res = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={citys}&count=1&language=pl')
    res_city = res.json()
    try:
        long = res_city['results'][0]['longitude']
        lat = res_city['results'][0]['latitude']
    except KeyError:
        return None

    return lat, long




def dlugo_terminowa(lat, long, days):
    res = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&daily=temperature_2m_mean&forecast_days={days}')
    
    res_dluga = res.json()
    day = res_dluga['daily']['time']
    temp = res_dluga['daily']['temperature_2m_mean']
    print('\ndługoterminowa:')
    for i, j in zip(day, temp):
        print(f'{i}: {j}{res_dluga["daily_units"]["temperature_2m_mean"]}')


def coord():
    res = requests.get('http://ip-api.com/json/')
    res_coord = res.json()
    if res_coord['status'] != 'fail':

        long = res_coord['lon']
        lat = res_coord['lat']

        return long, lat

    else:
        return None   



while True:
    try:
        days = int(input('na ile dni podać prognozy?\n'))
        if 1 <= days and days <= 16:
            break
        else:
            print('\npodaj ilość dni z zakresu 1-16')
    except ValueError:
        print('panie to nie liczba')




coor = coord()


if coor == None:
    city = input('podaj miasto\n')
    x = prognoza(city)

    if x is None:
        print("nie ma takiej miejscowości")

    else:
        lat, long = x
        dlugo_terminowa(lat, long, days)

        res = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m,wind_speed_10m,weather_code')

        res_dict = res.json()
        temp = str(res_dict['current']['temperature_2m']) + res_dict['current_units']['temperature_2m']
        wind = str(res_dict['current']['wind_speed_10m']) + res_dict['current_units']['wind_speed_10m']



        print(f'\nDzisiejsza:\ntemperatura: {temp}\nwiatr: {wind}')
else:
    long, lat = coor
    print(lat, long)

    dlugo_terminowa(lat, long, days)

    res = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m,wind_speed_10m,weather_code')

    res_dict = res.json()
    temp = str(res_dict['current']['temperature_2m']) + res_dict['current_units']['temperature_2m']
    wind = str(res_dict['current']['wind_speed_10m']) + res_dict['current_units']['wind_speed_10m']

    print(f'\nDzisiejsza:\ntemperatura: {temp}\nwiatr: {wind}')