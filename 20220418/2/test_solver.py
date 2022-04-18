import io
from unittest import TestCase
from unittest.mock import MagicMock, patch

import solver


class Test(TestCase):

    @patch('sys.stdin', io.StringIO('\n'.join(map(lambda x: str(x), [3, 2, 1]))))
    @patch('sys.stdout', io.StringIO())
    @patch('solver.SquareIO.printResult')
    def test_solve_square_less_zero(self, result):
        solver.main()
        result.assert_called_once_with(None)

    @patch('sys.stdin', io.StringIO('\n'.join(map(lambda x: str(x), [2, 3, 1.125]))))
    @patch('sys.stdout', io.StringIO())
    @patch('solver.SquareIO.printResult')
    def test_solve_square_more_zero(self, result):
        solver.main()
        result.assert_called_once_with((-3.0, -3.0,))

    @patch('sys.stdin', io.StringIO('\n'.join(map(lambda x: str(x), [2, 3, 1]))))
    @patch('sys.stdout', io.StringIO())
    @patch('solver.SquareIO.printResult')
    def test_solve_square_zero(self, result):
        solver.main()
        result.assert_called_once_with((-2.0, -4.0,))
