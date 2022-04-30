from unittest import TestCase

from task import solve


class Test(TestCase):
    def test_solve1(self):
        self.assertEqual(solve(0, 2), None)

    def test_solve2(self):
        self.assertEqual(solve(2, 2), -1.0)

    def test_solve3(self):
        self.assertEqual(solve(100, 500), -5.0)

    def test_solve4(self):
        self.assertEqual(solve(-100, 500), 5.0)
