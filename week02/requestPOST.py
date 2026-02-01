import requests
import json

url = "***"

key = None

while True:

    if key is None:
        response = requests.post(url)
        print(response.text)

    else:
        response = requests.post(url, data=key)
        print(response.text)
    
    try:
        res = response.json()
        key = res["next_secret"]
    except KeyError:
        break    




    print(res)
