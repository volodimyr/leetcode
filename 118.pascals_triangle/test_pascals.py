import unittest
from pascals import Solution


class TestPascalsTriangle(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_single_row(self):
        self.assertEqual(
            self.sol.generate(1),
            [[1]]
        )

    def test_two_rows(self):
        self.assertEqual(
            self.sol.generate(2),
            [[1], [1, 1]]
        )

    def test_three_rows(self):
        self.assertEqual(
            self.sol.generate(3),
            [[1], [1, 1], [1, 2, 1]]
        )

    def test_five_rows(self):
        self.assertEqual(
            self.sol.generate(5),
            [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1],
            ]
        )

    def test_structure_and_values(self):
        res = self.sol.generate(10)
        self.assertEqual(len(res), 10)
        for i, row in enumerate(res):
            self.assertEqual(len(row), i + 1)
            self.assertEqual(row[0], 1)
            self.assertEqual(row[-1], 1)

    def test_max_rows(self):
        res = self.sol.generate(30)
        self.assertEqual(len(res), 30)
        self.assertEqual(res[0], [1])
        self.assertEqual(res[-1][0], 1)
        self.assertEqual(res[-1][-1], 1)


if __name__ == "__main__":
    unittest.main()
