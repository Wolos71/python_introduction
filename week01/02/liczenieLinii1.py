
PLIK = ('/Users/wolos/Documents/nauka/python_introduction/week01/08.py') #put here file path

with open(PLIK, "r") as f:
    print(f)
    print(len(f.readlines()))