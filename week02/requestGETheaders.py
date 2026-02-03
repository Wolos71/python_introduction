import requests
import json

url = "https://py10-day2-577570284557.europe-west1.run.app/ex3"


response = requests.get(url, params={"format": "jsonv2"})
res = response.json()
print(response.text)


while True:
    response = requests.get(url, headers={"X-Secret": res["next_secret"]})
    res = response.json()
    print(response.text)
