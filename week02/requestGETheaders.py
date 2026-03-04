import requests
import json

url = "***"


response = requests.get(url, params={"format": "jsonv2"})
res = response.json()
print(response.text)


while True:
    response = requests.get(url, headers={"X-Secret": res["next_secret"]})
    res = response.json()
    print(response.text)
