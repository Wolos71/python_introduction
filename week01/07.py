import json

dict = {
  "C/C++" : ["#include", "#define"],
  "php" : ["<?php"],
  "pyton" : ["def ", "import "],
  "HTML" : ["<html", "<body", "<div"]
}

with open ("langs.json", "w") as f:
  json.dump(dict, f, indent = 5)

with open ("langs.json", "r") as f:
  print(json.load(f))