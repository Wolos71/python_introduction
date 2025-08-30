import sys
import os


# if len(sys.argv) != 2:
#   sys.exit("usage: listowanie.py <path>")

x = 1
def pr():
  print(x)


for path, dirs, files in os.walk(sys.argv[1]):
  path_elements = path.split(os.path.sep)
  if any([x.startswith(".") for x in path_elements]):
    continue



  for file in files:
    print(pr(), f"{path}/{file}")
    x += 1
