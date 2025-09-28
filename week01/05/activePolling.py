import os
import pathlib
import time

files = pathlib.Path("/Users/wolos/Documents/nauka/python_introduction/week01/04")
cash = {}

try:
  while True:
    for f in files.rglob("*"):
      if f.is_file():
        # print(os.stat(f))
        times = os.stat(f)
        cash [str(f.relative_to(files))] = times.st_mtime
    print(cash)
    time.sleep(5)
except KeyboardInterrupt:
  pass



