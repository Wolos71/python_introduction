import requests
import json

url = "https://py10-day2-577570284557.europe-west1.run.app/ex3"

key = None

while True:

    if key is None:
        response = requests.post(url)
        print(response.text)
        res = response.json()
        key = res["next_secret"]
    else:
        response = requests.post(url, data=key)
        print(response.text)
        res = response.json()
        key = res["next_secret"]


    print(res)