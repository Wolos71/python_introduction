import pathlib
import sys
import os


langs = {
  "C/C++" : ["#include", "#define"],
  "php" : ["<?php"],
  "pyton" : ["def ", "import "],
  "HTML" : ["<html", "<body", "<div"],
  "Shell": ["#!/bin/bash", "#!/bin/sh", "echo ", "export "]
}

html = open('raport.html', 'w')
dir = pathlib.Path(sys.argv[1]).rglob("*")
zmienna = dict()



def files():
  for f in dir:
    if f.is_file():
      lines = 0
      lang = ""
      with open(f, "r") as file:
        try:
            content = file.read()
            for jezyk, wyrazenie in langs.items():
              if any(x in content for x in wyrazenie):
                lang = jezyk
        except UnicodeDecodeError:      # pomija pliki nietekstowe
          continue
      with open(f, "r") as file:
        for ln in file:
          if not ln.strip().startswith("#") and ln.strip():
            lines += 1
      zmienna [str(f)] = f"lang: {lang}, lines: {lines}"
  return zmienna



# print(f"{files()}")

raport = files()

htmlList = "<ul>\n"
for path, info in raport.items():
    htmlList += f"<li>{path} → {info}</li>\n"
htmlList += "</ul>"



html_template = f"""<html>
<head>
<title>Raport</title>
</head>
<body>

<p>{htmlList}</p>

</body>
</html>
"""

# writing the code into the file
html.write(html_template)

# close the file
html.close()