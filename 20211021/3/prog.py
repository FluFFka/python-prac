from collections import Counter
w = int(input())
s = ''
while curr := input():
    s += '\n' + curr
s = s.split()
ss = []
for i in s:
    curr = ''
    for j in i:
        if j.isalpha():
            curr += j
        else:
            if curr:
                ss.append(curr.lower())
            curr = ''
    if curr:
        ss.append(curr.lower())
res = []
best = -1
for i, j in Counter(ss).items():
    if len(i) == w:
        if best < j:
            best = j
            res = [i]
        elif best == j:
            res.append(i)
for i in sorted(res):
    print(i, end=' ')
if res:
    print()
