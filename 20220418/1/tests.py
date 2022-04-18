import unittest
import prog


class TestSolver(unittest.TestCase):
    
    def test_greater_zero(self):
        self.assertEqual(prog.solveSquare(1, -3, 2), (1, 2))
    def test_equal_zero(self):
        self.assertEqual(prog.solveSquare(1, -2, 1), (1, 1))
    def test_lower_zero(self):
        self.assertEqual(prog.solveSquare(1, -2, 1231), None)
