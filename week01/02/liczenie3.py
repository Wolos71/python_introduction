
PLIK = ('***') #put here file path

lines = 0

with open(PLIK, "r") as f:
    for ln in f:
        if not ln.strip().startswith("#") and ln.strip():
            lines += 1
print(lines)
