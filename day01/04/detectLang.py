import os
import sys
import pathlib

c = ["#include", "#define", ] #zmienić na dicta
php = ["<?php"]
pyton = ["def ", "import "]
lang = set((""))

dir = []
file = []

dir.append(sys.argv[1])

for i in dir:
  for f in os.listdir(i):
    if os.path.isdir(os.path.join(i, f)):
      dir.append(os.path.join(i, f))
      continue
    elif os.path.isfile(os.path.join(i, f)):
      file.append(os.path.join(i, f))
      continue

for openFile in file:
  try:
    with open(openFile, "r") as plik:
      content = plik.read()
      for p in pyton:
        if p in content:
          lang.add("pyton")
      for ce in c:
        if ce in content:
          lang.add("c")
  except UnicodeDecodeError:
    continue


# print(file)
for i in lang:
  print(i)