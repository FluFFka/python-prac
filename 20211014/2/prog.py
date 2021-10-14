from math import *

def scale(A, B, a, b, x):
    return (x - A) / (B - A) * (b - a) + a

w, h = 80, 25
F = sin
X = [-4, 4]
X_v = [scale(0, w + 1, X[0], X[1], x) for x in range(w+1)]
Y_v = [F(x) for x in X_v]
Y = [max(Y_v), min(Y_v)]

for y in Y:
    print(scale(Y[0], Y[1], 0, w+1, int(y)*' '+'*'))
