import pathlib
import sys


files = pathlib.Path(sys.argv[1]).rglob("*")

for f in files:
  if f.is_file():
    print(f)
