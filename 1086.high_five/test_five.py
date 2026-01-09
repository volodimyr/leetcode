import unittest
from five import Solution


class TestHighFive(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        items = [
            [1, 91], [1, 92], [2, 93], [2, 97],
            [1, 60], [2, 77], [1, 65], [1, 87],
            [1, 100], [2, 100], [2, 76]
        ]
        expected = [[1, 87], [2, 88]]
        self.assertEqual(self.solution.highFive(items), expected)

    def test_single_user_exact_five(self):
        items = [
            [1, 10], [1, 20], [1, 30], [1, 40], [1, 50]
        ]
        expected = [[1, 30]]
        self.assertEqual(self.solution.highFive(items), expected)

    def test_multiple_users_unsorted_input(self):
        items = [
            [3, 50], [2, 90], [3, 100], [2, 80],
            [3, 60], [2, 70], [3, 40], [2, 60],
            [3, 30], [2, 50]
        ]
        expected = [[2, 70], [3, 56]]
        self.assertEqual(self.solution.highFive(items), expected)

    def test_scores_with_duplicates(self):
        items = [
            [1, 100], [1, 100], [1, 100],
            [1, 90], [1, 90], [1, 80]
        ]
        expected = [[1, 96]]
        self.assertEqual(self.solution.highFive(items), expected)

    def test_large_scores(self):
        items = [[1, i] for i in range(1000)]
        expected = [[1, 997]]  # (999+998+997+996+995)//5
        self.assertEqual(self.solution.highFive(items), expected)


if __name__ == "__main__":
    unittest.main()
