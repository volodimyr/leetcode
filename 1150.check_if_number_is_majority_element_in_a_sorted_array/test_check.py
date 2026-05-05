import unittest
from check import Solution

class TestIsMajorityElement(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertTrue(self.s.isMajorityElement([2,4,5,5,5,5,5,6,6], 5))

    def test_example2(self):
        self.assertFalse(self.s.isMajorityElement([10,100,101,101], 101))

    def test_target_not_in_array(self):
        self.assertFalse(self.s.isMajorityElement([1,2,3,4,5], 6))

    def test_single_element_is_majority(self):
        self.assertTrue(self.s.isMajorityElement([7], 7))

    def test_all_same_elements(self):
        self.assertTrue(self.s.isMajorityElement([3,3,3,3,3], 3))

    def test_exactly_half_not_majority(self):
        self.assertFalse(self.s.isMajorityElement([1,1,2,2], 1))

    def test_target_at_end_not_majority(self):
        self.assertFalse(self.s.isMajorityElement([1,1,1,2,2,2,3], 3))

    def test_target_majority_at_start(self):
        self.assertTrue(self.s.isMajorityElement([5,5,5,6,7], 5))

if __name__ == '__main__':
    unittest.main()
