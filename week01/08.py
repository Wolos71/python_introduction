import random
import csv


products = ("ziemniak", "marchew", "ogórek", "kalafior", "jabłko", "pomidor", "banan", "gruszka")
prices = []


for i in range(30):
    i = (random.choice(products), random.randint(7, 20))
    prices.append(i)


with open ("prices.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(prices)





