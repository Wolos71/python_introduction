import sys
from pygments.lexers import guess_lexer

file = sys.argv[1]



with open(file, "r") as f:
    lang = guess_lexer(f.read()).name

print(lang)