import os
import pathlib
import time
from datetime import datetime, timezone

files = pathlib.Path("/users/Wolos/Documents/nauka/python_introduction")
cash = {}


                                                                
for f in files.rglob("*"):
  if f.is_file():
    times = os.stat(f)
    cash [str(f.relative_to(files))] = times.st_mtime  

for path, times in cash.items():
  print(f'{path}: {datetime.fromtimestamp(times).strftime("%Y-%m-%d %H:%M:%S")}')


try:
  while True:
    time.sleep(8)
    for f in files.rglob("*"):
      if f.is_file():
        times = os.stat(f)
        path = str(f.relative_to(files))
        currentTime = times.st_mtime
        if path not in cash:
          print(f'nowy plik: {path} {datetime.fromtimestamp(currentTime).strftime("%Y-%m-%d %H:%M:%S")}')
          cash[path] = currentTime
        elif cash[path] != currentTime:
          cash[path] = currentTime
          print(f'zmiana tu była: {path} {datetime.fromtimestamp(currentTime).strftime("%Y-%m-%d %H:%M:%S")}')
except KeyboardInterrupt:
  print("\n kończymy na dziś")
