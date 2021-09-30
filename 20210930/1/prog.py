a = list(eval(input()))
n = len(a)
for i in range(n):
    for j in range(n - 1):
        if a[j+1]**2 % 100 < a[j]**2 % 100:
            a[j+1], a[j] = a[j], a[j+1]
print(a)
