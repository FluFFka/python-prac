import sys

s = sys.stdin.buffer.read()
n = s[0]
res = s[0:1]
l = len(s) - 1
outs = []
s = s[1:]
for i in range(n):
    outs.append(s[i*l//n:(i+1)*l//n])
outs.sort()
for i in outs:
    res += i
sys.stdout.buffer.write(res)
