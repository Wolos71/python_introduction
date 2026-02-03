import os
import sys
import pathlib
import time


Langs = {
  ".c": "C/C++",
  ".cc": "C/C++",
  ".h": "C/C++",
  ".hpp": "C/C++",
  ".cpp": "C/C++",
  ".ino": "C/C++",
  ".py": "Python",
  ".pyw": "Python",
  ".html": "HTML",
  ".htm": "HTML",
  ".md": "Markdown",
  ".css": "CSS",
  ".js": "JavaScript",
  ".bat": "Batch",
  ".sh": "Bash",
}


dirToScan = sys.argv[1]
dirpath = pathlib.Path(dirToScan)


totalLang= {}
for ext, lang in Langs.items():
    if lang not in totalLang:
        totalLang[lang] = 0 

total = 0

cache = {}


def lineCount(fileArg):
  lines = 0
  with open(fileArg, "r") as f:
    for ln in f:
      if not ln.strip().startswith("#") and ln.strip():
        lines += 1
  return lines


for f in dirpath.rglob("*"):
  if f.is_file():
    times = os.stat(f)
    plik = str(f.relative_to(dirpath))
    cache [plik] = times.st_mtime
    ext = f.suffix.lower()      #.suffix wyciąga tylko rozszerzenie z obiektu path
    if ext not in Langs:
      continue

    lang = Langs[ext]
    linie = lineCount(f)
    totalLang[lang] += linie
    total += linie

    print(f"{plik}: {linie} linii ({lang})")


    

try:
  while True:
    time.sleep(30)
    for f in dirpath.rglob("*"):
      if f.is_file() and not any(part.startswith(".") for part in f.parts):
        times = os.stat(f)
        path = str(f.relative_to(dirpath))
        currentTime = times.st_mtime
        ext = f.suffix.lower()
        if ext not in Langs:
          continue
        
        if path not in cache:
          cache[path] = currentTime
          linie = lineCount(f)
          totalLang[lang] += linie
          total += linie

          print(f":Nowy plik: {path} — {linie} linii ({lang})")

        elif cache[path] != currentTime:
          cache[path] = currentTime
          linie = lineCount(f)
          totalLang[lang] += linie
          total += linie


    print("\033[2J\033[H", end="")
    for lang, lines in totalLang.items():
      if lines != 0:
        print(f"{lang}: {lines} linii")
    print(f"Łącznie: {total} linii\n")
    

except KeyboardInterrupt:
  print("\n kończymy na dziś")







# for path, dirs, files in os.walk(dirToScan):
#   # print("sciezka:", path)
#   # print("pliki:", files)
#   path_elements = path.split(os.path.sep)                   #rozbija ściezke na katalogi
#   if any([x.startswith(".") for x in path_elements]):       #sprawdz czy katalog zaczyna się na . i pomiija
#     continue

#   for file in files:
#     if file.startswith("."):
#       continue

#     fullPath = f"{path}/{file}"
#     _, ext = os.path.splitext(file)                         #wycina rozszerzenie
#     ext = ext.lower()

#     if ext not in Langs:
#       continue

#     # print(f"{fullPath}")
#     linie = lineCount(fullPath)
#     total += linie
#     lang = Langs[ext]
#     totalLang[lang] += linie
#     print(f"{fullPath}: {linie} {lang}")


# for lang, lines in totalLang.items():
#   if lines != 0:
#     print(f"{lang}: {lines}")
#   else:
#     continue


# print(f"w sumie wszystko: {total}")
