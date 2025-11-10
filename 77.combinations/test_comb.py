import unittest

from comb import Solution

class TestCombinations(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        n, k = 4, 2
        expected = [
            [1, 2], [1, 3], [1, 4],
            [2, 3], [2, 4], [3, 4]
        ]
        result = self.s.combine(n, k)
        self.assertCountEqual(result, expected)

    def test_example2(self):
        n, k = 1, 1
        expected = [[1]]
        result = self.s.combine(n, k)
        self.assertEqual(result, expected)

    def test_k_equals_n(self):
        n, k = 3, 3
        expected = [[1, 2, 3]]
        result = self.s.combine(n, k)
        self.assertEqual(result, expected)

    def test_k_equals_1(self):
        n, k = 4, 1
        expected = [[1], [2], [3], [4]]
        result = self.s.combine(n, k)
        self.assertCountEqual(result, expected)

    def test_n_equals_5_k_equals_3(self):
        n, k = 5, 3
        expected = [
            [1, 2, 3], [1, 2, 4], [1, 2, 5],
            [1, 3, 4], [1, 3, 5], [1, 4, 5],
            [2, 3, 4], [2, 3, 5], [2, 4, 5],
            [3, 4, 5]
        ]
        result = self.s.combine(n, k)
        self.assertCountEqual(result, expected)

    def test_invalid_k_greater_than_n(self):
        n, k = 3, 5
        result = self.s.combine(n, k)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
