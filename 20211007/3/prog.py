def Bisect(a, x):
    l, r = 0, len(x)
    n = 0
    while r - l:
        n += 1
        m = (r + l - 1) // 2
        if x[m] == a:
            return True
        if x[m] > a:
            r = m
        else:
            l = m + 1
        if n == 20:
            break
    return False
print(Bisect(*eval(input())))
