import unittest

from defer import return_value
import prog
from unittest.mock import MagicMock

eps = 0.00001

def make_test(coeffs, true_res):
    prog.SquareIO.inputCoeff = MagicMock(side_effect=coeffs)
    prog.SquareIO.printResult = MagicMock()
    prog.solveSquare()
    res = prog.SquareIO.printResult.call_args.args[0]
    if type(res) is type(true_res):
        if type(res) is str:
            assert res == true_res
        elif type(res) is float:
            assert res - eps <= true_res <= res + eps
        elif type(res) is tuple and len(res) == len(true_res) == 2:
            assert res[0] - eps <= true_res[0] <= res[0] + eps and res[1] - eps <= true_res[1] <= res[1] + eps
        else:
            assert False
    else:
        assert False

class TestSolver(unittest.TestCase):

    def test_01_greater_zero(self):
        make_test((1, -3, 2), (1., 2.))
    def test_02_equal_zero(self):
        make_test((1, -2, 1), (1., 1.))
    def test_03_lower_zero(self):
        make_test((1, -2, 1231), 'No solutions exist')
    def test_04_all_zeros(self):
        make_test((0, 0, 0), 'All values of x are solutions')
    def test_05_a_b_zeros(self):
        make_test((0, 0, 5), 'No solutions exist')
    def test_06_a_zero(self):
        make_test((0, 5, 6), -1.2)

    