import shlex

while s := input():
    spl = shlex.split(s)
    if len(spl) < 1:
        break
    num = int(spl[0])
    if num < 1 or num > len(spl):
        break
    else:
        print(spl[num])

        

