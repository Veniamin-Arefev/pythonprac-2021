from unittest import TestCase

from solver import solveSquare


class Test(TestCase):

    def test_solve_square_less_zero(self):
        self.assertEqual(solveSquare(3, 2, 1), None)

    def test_solve_square_more_zero(self):
        self.assertEqual(solveSquare(2, 3, 1.125), (-3.0, -3.0))

    def test_solve_square_zero(self):
        self.assertEqual(solveSquare(2, 3, 1), (-2.0, -4.0))
