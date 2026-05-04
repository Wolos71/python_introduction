import requests
import json
import html
import random


key_get = requests.get('https://opentdb.com/api_token.php?command=request')
key_res = key_get.json()
key = key_res['token']

def fast_five(key):
    res = requests.get(f'https://opentdb.com/api.php?amount=10&token={key}')
    q = res.json()

    # with open('pytania.json', 'w') as f:
    #     json.dump(q, f)

    rescode = q['response_code']
    print(f'kody odpowiedzi: {rescode}')
    qr = q['results']

    # print(f'q= {type(q)}\n')
    # print(q)
    # print(f'qr= {type(qr)}\n')
    # print(qr)
    for i in qr:
        answers = i['incorrect_answers']
        answers.append(i['correct_answer'])
        random.shuffle(answers)
        print(i['correct_answer'])
        print(f"{html.unescape(i['question'])}\n")
        for indeks, element in enumerate(answers):
            print(f'{indeks, html.unescape(element)}\n')

        while True:
            try:
                respons = input("podaj odpowiedź")

                res = answers[int(respons)]
                if res == i['correct_answer']:
                    print('dobrze')
                    break
                else:
                    print('nope, spróbuj jeszcze raz')
            except ValueError:
                print('liczba ma być')
            except IndexError:
                print('wybierz coś z podanych wartości')

    # print(qr[0]['type'])

fast_five(key)
