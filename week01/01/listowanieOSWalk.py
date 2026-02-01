import sys
import os


# if len(sys.argv) != 2:
#   sys.exit("usage: listowanie.py <path>")

x = 1
def pr():
  print(x)

pliki = []

for path, dirs, files in os.walk(sys.argv[1]):
  # print(files)
  # print(dirs)
  path_elements = path.split(os.path.sep)
  # print(path_elements)
  if any([x.startswith(".") for x in path_elements]):
    continue
  for file in path_elements:
    if not file.startswith("."):
      pliki.append(file)
      continue

  # print(files)

    # print(files)
    # pliki.append(file)
      print(files)

# print(f"{pliki}")