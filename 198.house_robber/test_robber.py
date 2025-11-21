import unittest
from typing import List
from robber import Solution

class TestHouseRobber(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(Solution().rob([1,2,3,1]), 4)

    def test_example2(self):
        self.assertEqual(Solution().rob([2,7,9,3,1]), 12)

    def test_single_element(self):
        self.assertEqual(Solution().rob([5]), 5)

    def test_two_elements(self):
        self.assertEqual(Solution().rob([2,1]), 2)
        self.assertEqual(Solution().rob([1,2]), 2)

    def test_all_zeroes(self):
        self.assertEqual(Solution().rob([0,0,0,0]), 0)

    def test_strictly_increasing(self):
        # [1,2,3,4,5] → choose 1 + 3 + 5 = 9
        self.assertEqual(Solution().rob([1,2,3,4,5]), 9)

    def test_uniform_values(self):
        # [5,5,5,5,5] → 5+5+5 = 15
        self.assertEqual(Solution().rob([5,5,5,5,5]), 15)

    def test_large_input(self):
        arr = [400]*100
        # best = sum of every second: 50 * 400 = 20000
        self.assertEqual(Solution().rob(arr), 20000)

    # A brute-force solver for validation
    def brute(self, nums):
        from functools import lru_cache
        @lru_cache(None)
        def dfs(i):
            if i >= len(nums):
                return 0
            return max(nums[i] + dfs(i+2), dfs(i+1))
        return dfs(0)

    def test_random_small(self):
        import random
        for _ in range(30):
            n = random.randint(1, 8)
            arr = [random.randint(0, 20) for _ in range(n)]
            self.assertEqual(Solution().rob(arr), self.brute(tuple(arr)))


if __name__ == "__main__":
    unittest.main()
