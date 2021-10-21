s = input().lower()
if len(s) == 0:
    print(0)
    exit(0)
res = set()
prev = s[0]
for i in range(1, len(s)):
    if prev.isalpha() and s[i].isalpha():
        res.add(prev + s[i])
    prev = s[i]
print(len(res))
