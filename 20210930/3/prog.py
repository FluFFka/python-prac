a = []
b = []
a.append(list(eval(input())))
n = len(a[0])
for i in range(n - 1):
    a.append(list(eval(input())))
for i in range(n):
    b.append(list(eval(input())))
c = []
for i in range(n):
    temp = []
    for j in range(n):
        s = 0
        for k in range(n):
            s += a[i][k] * b[k][j]
        temp.append(s)
    c.append(temp)
for i in c:
    print(i)

