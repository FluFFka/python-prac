def SUB(a, b):
    if (type(a) is tuple) or (type(b) is list):
        res = []
        for i in a:
            if i not in b:
                res.append(i)
        return type(a)(res)
    else:
        return a - b
print(SUB(*eval(input())))
