import unittest
from wiggle import Solution

def is_wiggle(nums):
    for i in range(len(nums) - 1):
        if i % 2 == 0 and nums[i] > nums[i + 1]:
            return False
        if i % 2 == 1 and nums[i] < nums[i + 1]:
            return False
    return True

class TestWiggleSort(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        nums = [3, 5, 2, 1, 6, 4]
        self.sol.wiggleSort(nums)
        self.assertTrue(is_wiggle(nums))

    def test_example2(self):
        nums = [6, 6, 5, 6, 3, 8]
        self.sol.wiggleSort(nums)
        self.assertTrue(is_wiggle(nums))

    def test_single_element(self):
        nums = [1]
        self.sol.wiggleSort(nums)
        self.assertTrue(is_wiggle(nums))

    def test_two_elements(self):
        nums = [2, 1]
        self.sol.wiggleSort(nums)
        self.assertTrue(is_wiggle(nums))

    def test_all_equal(self):
        nums = [4, 4, 4, 4]
        self.sol.wiggleSort(nums)
        self.assertTrue(is_wiggle(nums))

    def test_sorted_ascending(self):
        nums = [1, 2, 3, 4, 5]
        self.sol.wiggleSort(nums)
        self.assertTrue(is_wiggle(nums))

    def test_sorted_descending(self):
        nums = [5, 4, 3, 2, 1]
        self.sol.wiggleSort(nums)
        self.assertTrue(is_wiggle(nums))

if __name__ == "__main__":
    unittest.main()
