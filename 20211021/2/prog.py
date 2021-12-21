import math
functions = dict()
strings_num = 0
while True:
    inp = input().split()
    strings_num += 1
    if inp[0] == 'quit':
        if (inp[1][0] == '"' and inp[1][-1] == '"') or (inp[1][0] == "'" and inp[1][-1] == "'"):
            print(inp[1][1:-1].format(len(functions)+1, strings_num))
        else:
            print(inp[1].format(len(functions)+1, strings_num))
        break
    if inp[0][0] == ':':
        name = inp[0]
        variables = []
        for i in range(1, len(inp) - 1):
            variables.append(inp[i])
        func = inp[-1]
        functions[name[1:]] = (func, variables)
    else:
        values = []
        for i in range(1, len(inp)):
            values.append(eval(inp[i]))
        name = inp[0]
        func, variables = functions[name]
        local = dict()
        if len(variables) != 0:
            local = dict(zip(variables, values))
        print(eval(func, math.__dict__, local))

