import unittest
from game import TicTacToe


class TestTicTacToe(unittest.TestCase):
    def test_leetcode_example(self):
        t = TicTacToe(3)
        self.assertEqual(t.move(0, 0, 1), 0)
        self.assertEqual(t.move(0, 2, 2), 0)
        self.assertEqual(t.move(2, 2, 1), 0)
        self.assertEqual(t.move(1, 1, 2), 0)
        self.assertEqual(t.move(2, 0, 1), 0)
        self.assertEqual(t.move(1, 0, 2), 0)
        self.assertEqual(t.move(2, 1, 1), 1)

    def test_horizontal_win(self):
        t = TicTacToe(3)
        t.move(0, 0, 1)
        t.move(1, 0, 2)
        t.move(0, 1, 1)
        t.move(1, 1, 2)
        self.assertEqual(t.move(0, 2, 1), 1)

    def test_vertical_win(self):
        t = TicTacToe(3)
        t.move(0, 0, 1)
        t.move(0, 1, 2)
        t.move(1, 0, 1)
        t.move(1, 1, 2)
        self.assertEqual(t.move(2, 0, 1), 1)

    def test_main_diagonal_win(self):
        t = TicTacToe(3)
        t.move(0, 0, 1)
        t.move(0, 1, 2)
        t.move(1, 1, 1)
        t.move(0, 2, 2)
        self.assertEqual(t.move(2, 2, 1), 1)

    def test_anti_diagonal_win(self):
        t = TicTacToe(3)
        t.move(0, 2, 1)
        t.move(0, 0, 2)
        t.move(1, 1, 1)
        t.move(1, 0, 2)
        self.assertEqual(t.move(2, 0, 1), 1)

    def test_player2_wins(self):
        t = TicTacToe(3)
        t.move(0, 0, 1)
        t.move(1, 0, 2)
        t.move(0, 1, 1)
        t.move(1, 1, 2)
        t.move(2, 2, 1)
        self.assertEqual(t.move(1, 2, 2), 2)

    def test_winner(self):
        t = TicTacToe(2)
        t.move(0, 0, 1)
        t.move(0, 1, 2)
        self.assertEqual(t.move(1, 1, 1), 1)

    def test_minimal_board(self):
        t = TicTacToe(2)
        t.move(0, 0, 1)
        self.assertEqual(t.move(1, 1, 1), 1)


if __name__ == "__main__":
    unittest.main()
