import unittest
from subsets import Solution

class TestSubsetsWithDup(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [1, 2, 2]
        expected = [
            [], [1], [2], [1, 2], [2, 2], [1, 2, 2]
        ]
        result = self.solution.subsetsWithDup(nums)
        self.assertCountEqual([sorted(x) for x in result], [sorted(x) for x in expected])

    def test_all_unique(self):
        nums = [1, 2, 3]
        expected = [
            [], [1], [2], [3],
            [1, 2], [1, 3], [2, 3],
            [1, 2, 3]
        ]
        result = self.solution.subsetsWithDup(nums)
        self.assertCountEqual([sorted(x) for x in result], [sorted(x) for x in expected])

    def test_all_duplicates(self):
        nums = [2, 2, 2]
        expected = [[], [2], [2, 2], [2, 2, 2]]
        result = self.solution.subsetsWithDup(nums)
        self.assertCountEqual([sorted(x) for x in result], [sorted(x) for x in expected])


if __name__ == "__main__":
    unittest.main()
