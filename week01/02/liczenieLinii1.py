#liczy wszystkie linie


PLIK = ('***') #put here file path

with open(PLIK, "r") as f:
    print(f)
    print(len(f.readlines()))