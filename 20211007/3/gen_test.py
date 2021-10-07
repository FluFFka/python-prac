from random import randint
a = []
for i in range(300):
    a.append(randint(-1000000000000, 1000000000000))
print(str(randint(0, 10)) + ", " + str(tuple(sorted(a))))
