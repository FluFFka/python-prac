import unittest
from eq import eq

class TestSolver(unittest.TestCase):
    
    def test_a_greater_zero(self):
        self.assertEqual(eq(1, 1), -1)
    def test_a_equal_zero(self):
        self.assertEqual(eq(0, 1), None)
    def test_a_lower_zero(self):
        self.assertEqual(eq(-2, 1), 0.5)

if __name__ == "__main__":
    unittest.main()