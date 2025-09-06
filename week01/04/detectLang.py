import os
import sys
import pathlib

langs = {
  "C/C++" : ["#include", "#define"],
  "php" : ["<?php"],
  "pyton" : ["def ", "import "],
  "HTML" : ["<html", "<body", "<div"],
}

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
      for jezyk, wyrazenie in langs.items():
        if any(x in content for x in wyrazenie):
#          print(f"    {openFile}        {jezyk}")  //debugowanie
          lang.add(jezyk)
  except UnicodeDecodeError:      # pomija pliki nietekstowe
    continue


# print(file)
for i in lang:
  print(i)