import math
functions = dict()
while True:
    inp = input().split()
    if inp[0] == 'quit':
        functions['quit'] = inp[1]
        break
    if len(inp) == 3:
        name, var, func = inp[0], inp[1], inp[2]
        functions[name[1:]] = (func, var)
    else:
        name, value = inp[0], eval(inp[1])
        func, var = functions[name]
        print(eval(func, math.__dict__, {var: value}))
print(len(functions))
