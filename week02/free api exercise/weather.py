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
    print('długoterminowa:')
    for i, j in zip(day, temp):
        print(f'{i}: {j}')

city = input('podaj miasto\n')
days = input('na ile dni podać prognozy?\n')

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