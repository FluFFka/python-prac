from random import randint
from random import uniform
import struct

f = ''
res = []
for i in range(10):
    f += "fi"
    res.append(uniform(0, 1) * 1000000)
    res.append(randint(-1000000000, 1000000000))
file = open("dd.bin", "wb")
file.write(struct.pack(f, *res))
file.close()
