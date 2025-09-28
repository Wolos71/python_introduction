import os
import pathlib

files = pathlib.Path("/Users/wolos/Documents/nauka/python_introduction/week01/04")
cash = {}


for f in files.rglob("*"):
  if f.is_file():
    # print(os.stat(f))
    time = os.stat(f)
    cash [str(f.relative_to(files))] = time.st_mtime


print(cash)