import re
import sys
import os


dir = []
file = []

langs = {
    "c/cpp": ["#include", "intmain", "printf"],
    "php": ["<?php", "echo", "function"],
    "python": ["from.*import", "for.*in.*:"],
    "html": ["<!DOCTYPE html>", "<html ", "<head>"]
}

lang = set((""))

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
      linie = plik.readlines()
      for linia in linie:
        for jezyk, reg in langs.items():
          for i in reg:
            if re.match(i, linia):
              lang.add(jezyk)
  except UnicodeDecodeError:      # pomija pliki nietekstowe
    continue        


print(lang)