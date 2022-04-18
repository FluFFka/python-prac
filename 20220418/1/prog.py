from cmath import sqrt


def solveSquare(a, b, c):
    D = b * b - 4 * a * c
    if D >= 0:
        return ((-b - D**0.5) / 2 / a, (-b + D**0.5) / 2 / a)
    else:
        return None