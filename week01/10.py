r = "\033[0m"

print(f"\x1b[0;30mblack{r} <- \\x1b[0;30m")
print(f"\x1b[0;31mred{r} <- \\x1b[0;31m")
print(f"\x1b[0;32mgreen{r} <- \\x1b[0;32m")
print(f"\x1b[0;33myelow{r} <- \\x1b[0;33m")
print(f"\x1b[0;34mblue{r} <- \\x1b[0;34m")
print(f"\x1b[0;35mmagenta{r} <- \\x1b[0;35m")
print(f"\x1b[0;36mcyan{r} <- \\x1b[0;36m")
print(f"\x1b[0;37mwhite{r} <- \\x1b[0;37m")
print(f"\x1b[0;90mbright black{r} <- \\x1b[0;90m")
print(f"\x1b[0;91mbright red{r} <- \\x1b[0;91m")
print(f"\x1b[0;92mbright green{r} <- \\x1b[0;92m")
print(f"\x1b[0;93mbright yellow{r} <- \\x1b[0;93m")
print(f"\x1b[0;94mbright blue{r} <- \\x1b[0;94m")
print(f"\x1b[0;95mbright magenta{r} <- \\x1b[0;95m")
print(f"\x1b[0;96mbright cyan{r} <- \\x1b[0;96m")
print(f"\x1b[0;97mbright white{r} <- \\x1b[0;97m")

i = 0
while i < 7:
    print(f"\x1b[0;3{i}mkolorek{r} <- \\x1b[0;3{i}m")
    print(f"\x1b[0;9{i}mkolorek{r} <- \\x1b[0;9{i}m")
    i += 1