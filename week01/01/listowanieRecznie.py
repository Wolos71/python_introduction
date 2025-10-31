import os
import sys


# home = sys.argv[1]
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
    
# for i in dir:
#   print(i)

for i, e in enumerate(file, start=1):
  print(f"{i}: {e}")


# for f in os.listdir(home):

#     if os.path.isfile(os.path.join(home, f)):
#       print(os.path.join(home, f))
#     elif os.path.isdir(os.path.join(home, f)):
#         print(os.path.join(home, f))
#         home = os.path.join(home, f)
#         print(home)