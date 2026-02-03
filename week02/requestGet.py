import requests
import json

url = "https://py10-day2-577570284557.europe-west1.run.app/ex1"



while True:
    response = requests.get(url, params={"format": "jsonv2"})
    res = response.json()
    print(response.text)

    try:
        url = res["next_url"]
    except KeyError:
        break



# tez działa

# x = requests.get(url,
#     params={
#         format:"jsonv2"
# })
# res = json.loads(x.text)
# next_url = res["next_url"]
# print(next_url)

# try:
#     for n in url:
#         y = requests.get(url)
#         res = json.loads(y.text)
#         url = res["next_url"]
#         print(y.text)
# except KeyError as e:
#     y = requests.get(url)
#     res = json.loads(y.text)
#     url = res["flag"]
#     print(y.text)

