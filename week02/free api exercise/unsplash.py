#dodanie obsługi wyjątków, wybór zakresu wyszukiwań, orientacja i zamknąć to w pętli

import requests
from dotenv import load_dotenv
import os
import webbrowser
import json
import random



load_dotenv()

key = os.getenv("ACCESS_KEY")


def losowo():
    res = requests.get('https://api.unsplash.com//photos/random', headers = {"Authorization": "Client-ID " + key} )
    res_search = res.json()

    link = res_search['urls']['full']
    return link

def wyszukaj(w):
    res = requests.get('https://api.unsplash.com//search/photos', headers = {"Authorization": "Client-ID " + key}, params={"query": w})
    res_search = res.json()

    losowe_zdjecie = random.choice(res_search['results'])
    link = losowe_zdjecie['urls']['full']
    opis = losowe_zdjecie['alt_description']
    return link, opis


while True:
    wybor = input('(W)yszukiwanie czy (L)osowe?\n')
    if wybor.upper() == 'W':
        search = input('podaj słowo kluczowe\n')
        link, opis = wyszukaj(search)

        print(f'{opis}\n\n{link}')
        webbrowser.open(link)

        break
    elif wybor.upper() == 'L':
        print('losujemy\n')
        rand = losowo()
        print(rand)
        webbrowser.open(rand)


        break
    else:
        print('nieprawidłowa odpowiedź')