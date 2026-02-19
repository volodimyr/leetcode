import unittest
from queens import Solution


def is_valid_board(board):
    n = len(board)
    cols = set()
    pos_diag = set()
    neg_diag = set()

    for r in range(n):
        for c in range(n):
            if board[r][c] == "Q":
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    return False
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

    return True


class TestNQueens(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_n_equals_1(self):
        expected = [["Q"]]
        result = self.solution.solveNQueens(1)
        self.assertEqual(result, expected)

    def test_n_equals_4(self):
        result = self.solution.solveNQueens(4)

        expected_solutions = [
            [".Q..", "...Q", "Q...", "..Q."],
            ["..Q.", "Q...", "...Q", ".Q.."],
        ]

        # Order does not matter
        self.assertEqual(len(result), 2)
        for sol in expected_solutions:
            self.assertIn(sol, result)

    def test_solution_validity(self):
        # Validate every solution for n=5
        result = self.solution.solveNQueens(5)

        for board in result:
            self.assertTrue(is_valid_board(board))

    def test_solution_counts(self):
        # Known solution counts
        known_counts = {
            1: 1,
            2: 0,
            3: 0,
            4: 2,
            5: 10,
            6: 4,
            7: 40,
            8: 92,
            9: 352,
        }

        for n, expected_count in known_counts.items():
            with self.subTest(n=n):
                result = self.solution.solveNQueens(n)
                self.assertEqual(len(result), expected_count)


if __name__ == "__main__":
    unittest.main()
