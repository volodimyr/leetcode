import unittest
from typing import List

from min import Solution

# Assuming your Solution class is already defined above
class TestMinSubArrayLen(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.minSubArrayLen(7, [2,3,1,2,4,3]), 2)

    def test_example2(self):
        self.assertEqual(self.solution.minSubArrayLen(4, [1,4,4]), 1)

    def test_example3(self):
        self.assertEqual(self.solution.minSubArrayLen(11, [1,1,1,1,1,1,1,1]), 0)

    def test_single_element_reach(self):
        self.assertEqual(self.solution.minSubArrayLen(5, [5]), 1)

    def test_single_element_not_reach(self):
        self.assertEqual(self.solution.minSubArrayLen(10, [5]), 0)

    def test_entire_array_needed(self):
        self.assertEqual(self.solution.minSubArrayLen(15, [1,2,3,4,5]), 5)

if __name__ == '__main__':
    unittest.main()
