def Pareto(*x):
    res = []
    for i in range(len(x)):
        for j in range(len(x)):
            if i != j and (x[i][0] < x[j][0] or x[i][1] < x[j][1]) and \
                x[i][0] <= x[j][0] and x[i][1] <= x[j][1]:
                break
        else:
            res.append(x[i])
    return tuple(res)
import sys
exec(sys.stdin.read())
