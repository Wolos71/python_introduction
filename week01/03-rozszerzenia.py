import pathlib
import sys
import os


files = pathlib.Path(sys.argv[1]).rglob("*")

rozszerzenie = set()

for f in files:
  if f.is_file():
    x = os.path.splitext(f)
    ext = x[1]
    rozszerzenie.add(ext)


print(rozszerzenie)