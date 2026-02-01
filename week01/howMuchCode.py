import os
import sys
import pathlib


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



def lineCount(fileArg):
  lines = 0
  with open(fileArg, "r") as f:
    for ln in f:
      if not ln.strip().startswith("#") and ln.strip():
        lines += 1
  return lines

total = 0


for path, dirs, files in os.walk(dirToScan):
  print("PATH:", path)
  print("FILES:", files)
  path_elements = path.split(os.path.sep)                   #rozbija ściezke na katalogi
  if any([x.startswith(".") for x in path_elements]):       #sprawdz czy katalog zaczyna się na . i pomiija
    continue

  for file in files:
    if file.startswith("."):
      continue

  fullPath = f"{path}/{file}"
  _, ext = os.path.splitext(file)                         #wycina rozszerzenie
  ext = ext.lower()

  # if ext not in Langs:
  #   continue

  print(f"{fullPath}")
  linie = lineCount(fullPath)
  total += linie
  print(f"{fullPath}: {linie}")

print(total)



    

  


