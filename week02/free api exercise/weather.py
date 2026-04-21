import requests


res = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.23&longitude=21.01&current=temperature_2m,wind_speed_10m,weather_code')

res_dict = res.json()
temp = str(res_dict['current']['temperature_2m']) + res_dict['current_units']['temperature_2m']
wind = str(res_dict['current']['wind_speed_10m']) + res_dict['current_units']['wind_speed_10m']

print(f'temperatura: {temp}\nwiatr: {wind}')