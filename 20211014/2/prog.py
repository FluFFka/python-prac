from math import *
w, h, *X, fun_str = input().strip().split(',')
w = int(w)
h = int(h)
X = [float(X[0]), float(X[1])]
if w == 1:
    X_vals = [X[0]]
else:
    X_vals = [X[0] + i * (X[1] - X[0]) / (w - 1) for i in range(w)]
Y_vals = []
for x in X_vals:
    Y_vals.append(eval(fun_str))
Y = [min(Y_vals), max(Y_vals)]
for i in range(h):
    for j in range(w):
        if h - i - 1 == int((h - 1) * (Y_vals[j] - Y[0]) / (Y[1] - Y[0])):
            print('#', end='')
        else:
            print('.', end='')
    print()
