import os
import pathlib
import time
from datetime import datetime, timezone

files = pathlib.Path("/users/Wolos/Documents/nauka/python_introduction")
cache = {}


                                                                
for f in files.rglob("*"):
  if f.is_file() and not any(part.startswith(".") for part in f.parts):
    times = os.stat(f)
    cache [str(f.relative_to(files))] = times.st_mtime  

for path, times in cache.items():
  print(f'{path}: {datetime.fromtimestamp(times).strftime("%Y-%m-%d %H:%M:%S")}')


try:
  while True:
    time.sleep(8)
    for f in files.rglob("*"):
      if f.is_file() and not any(part.startswith(".") for part in f.parts):
        times = os.stat(f)
        path = str(f.relative_to(files))
        currentTime = times.st_mtime
        if path not in cache:
          print(f'nowy plik: {path} {datetime.fromtimestamp(currentTime).strftime("%Y-%m-%d %H:%M:%S")}')
          cache[path] = currentTime
        elif cache[path] != currentTime:
          cache[path] = currentTime
          print(f'zmiana tu była: {path} {datetime.fromtimestamp(currentTime).strftime("%Y-%m-%d %H:%M:%S")}')
except KeyboardInterrupt:
  print("\n kończymy na dziś")
