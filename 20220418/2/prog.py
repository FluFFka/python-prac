class SquareIO:
    
    def __init__(self):
        pass

    def inputCoeff(self, name):
        print(f"Input {name}: ", end='')
        return float(input())

    def printResult(self, result):
        print(f"Solution: {result}")

def solveSquare():
    iomanager = SquareIO()
    a = iomanager.inputCoeff('a')
    b = iomanager.inputCoeff('b')
    c = iomanager.inputCoeff('c')
    if a == 0:
        if b == 0:
            if c == 0:
                iomanager.printResult('All values of x are solutions')
            else:
                iomanager.printResult('No solutions exist')
        else:
            iomanager.printResult(-c / b)
    else:
        D = b * b - 4 * a * c
        if D >= 0:
            iomanager.printResult(((-b - D**0.5) / 2 / a, (-b + D**0.5) / 2 / a))
        else:
            iomanager.printResult('No solutions exist')


if __name__ == "__main__":
    solveSquare()