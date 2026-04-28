import unittest
from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []

        for n in nums:
            if n > 0:
                pos.append(n)
            else:
                neg.append(n)
        
        res = []
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])

        return res


class TestRearrangeArray(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        nums = [3,1,-2,-5,2,-4]
        expected = [3,-2,1,-5,2,-4]
        self.assertEqual(self.sol.rearrangeArray(nums), expected)

    def test_example_2(self):
        nums = [-1,1]
        expected = [1,-1]
        self.assertEqual(self.sol.rearrangeArray(nums), expected)

    def test_already_alternating(self):
        nums = [1,-1,2,-2]
        expected = [1,-1,2,-2]
        self.assertEqual(self.sol.rearrangeArray(nums), expected)

    def test_all_positions_preserved(self):
        nums = [5,7,-1,-2,9,-3]
        result = self.sol.rearrangeArray(nums)
        
        # check alternating sign
        for i in range(len(result)):
            if i % 2 == 0:
                self.assertGreater(result[i], 0)
            else:
                self.assertLess(result[i], 0)

        # check order preservation
        pos_original = [x for x in nums if x > 0]
        neg_original = [x for x in nums if x < 0]
        pos_result = [result[i] for i in range(0, len(result), 2)]
        neg_result = [result[i] for i in range(1, len(result), 2)]

        self.assertEqual(pos_original, pos_result)
        self.assertEqual(neg_original, neg_result)

    def test_large_input(self):
        nums = []
        for i in range(1, 1001):
            nums.append(i)
            nums.append(-i)

        result = self.sol.rearrangeArray(nums)

        # alternating check
        for i in range(len(result)):
            if i % 2 == 0:
                self.assertGreater(result[i], 0)
            else:
                self.assertLess(result[i], 0)

        self.assertEqual(len(result), len(nums))

    def test_edge_minimum(self):
        nums = [1, -1]
        expected = [1, -1]
        self.assertEqual(self.sol.rearrangeArray(nums), expected)


if __name__ == "__main__":
    unittest.main()