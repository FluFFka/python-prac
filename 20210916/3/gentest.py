import random

a = []
for i in range(9):
    a.append(random.randint(1, 100))
a.append(int(input()))
random.shuffle(a)
print(a)