
PLIK = ('/home/wolos/Downloads/pyton/py10-day01-files/howmuchcode.py')

lines = 0

with open(PLIK, "r") as f:
    for ln in f:
        if not ln.strip().startswith("#") and ln.strip():
            lines += 1
print(lines)
