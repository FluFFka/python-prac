class InvalidInput(Exception):
    pass
class BadTriangle(Exception):
    pass

class TriangleSquare:
    a, b, c = None, None, None
    def __init__(self, inpStr):
        try:
            (x1, y1), (x2, y2), (x3, y3) = eval(inpStr)
        except Exception:
            raise InvalidInput
        try:
            self.a = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
            self.b = ((x3 - x2)**2 + (y3 - y2)**2)**0.5
            self.c = ((x1 - x3)**2 + (y1 - y3)**2)**0.5
        except Exception:
            raise BadTriangle
        try:
            s = self.get_square() <= 0
        except Exception as E:
            raise BadTriangle
        if s:
            raise BadTriangle
    def get_square(self):
        p = 0.5 * (self.a + self.b + self.c)
        return (p * (p - self.a) * (p - self.b) * (p - self.c))**0.5
while True:
    try:
        tri = TriangleSquare(input())
    except InvalidInput:
        print("Invalid input")
    except BadTriangle:
        print("Not a triangle")
    else:
        print(f"{tri.get_square():.2f}")
        break
