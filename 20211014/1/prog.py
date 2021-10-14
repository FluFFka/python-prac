from fractions import Fraction
def Fun(*inp):
    s, w, degA = Fraction(inp[0]), Fraction(inp[1]), int(inp[2])
    A = []
    for i in range(3, 4 + degA):
        A.append(Fraction(inp[i]))
    degB = int(inp[4 + degA])
    B = []
    for i in range(5 + degA, len(inp)):
        B.append(Fraction(inp[i]))
    resA = 0
    resB = 0
    for i in range(degA + 1):
        resA += s**i * A[degA - i]
    for i in range(degB + 1):
        resB += s**i * B[degB - i]
    if resB == 0:
        return False
    return resA / resB == w
a = input().strip().split(',')
print(Fun(*a))
