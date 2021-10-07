from math import *
def Calc(s, t, u):
    def s_x(x, ss=s):
        return eval(s)
    def t_x(x, tt=t):
        return eval(t)
    def u_st(x, uu=u):
        x = s_x(x)
        y = t_x(x)
        return eval(uu)
    return u_st
