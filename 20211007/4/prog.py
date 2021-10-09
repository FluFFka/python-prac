from math import *
def Calc(s, t, u):
    s_x = lambda x: eval(s)
    t_x = lambda x: eval(t)
    def u_xy(z):
        x = s_x(z)
        y = t_x(z)
        return eval(u, {**locals(), **globals()})
    return u_xy
L = eval(input())
F = Calc(*L)
print(F(eval(input())))
