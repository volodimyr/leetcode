import unittest
from verify import Solution

class TestVerifyPreorder(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        preorder = [5, 2, 1, 3, 6]
        self.assertTrue(self.solution.verifyPreorder(preorder))

    def test_example_2(self):
        preorder = [5, 2, 6, 1, 3]
        self.assertFalse(self.solution.verifyPreorder(preorder))

    def test_single_element(self):
        preorder = [1]
        self.assertTrue(self.solution.verifyPreorder(preorder))

    def test_valid_left_skewed(self):
        preorder = [5, 4, 3, 2, 1]
        self.assertTrue(self.solution.verifyPreorder(preorder))

    def test_valid_right_skewed(self):
        preorder = [1, 2, 3, 4, 5]
        self.assertTrue(self.solution.verifyPreorder(preorder))

    def test_invalid_after_right_subtree(self):
        preorder = [8, 5, 1, 7, 10, 6]
        self.assertFalse(self.solution.verifyPreorder(preorder))

    def test_valid_complex(self):
        preorder = [8, 5, 1, 7, 10, 12]
        self.assertTrue(self.solution.verifyPreorder(preorder))

    def test_invalid_small_case(self):
        preorder = [3, 2, 4, 1]
        self.assertFalse(self.solution.verifyPreorder(preorder))

    def test_valid_balanced(self):
        preorder = [10, 5, 2, 7, 15, 12, 20]
        self.assertTrue(self.solution.verifyPreorder(preorder))

    def test_invalid_balanced(self):
        preorder = [10, 5, 2, 15, 7, 20]
        self.assertFalse(self.solution.verifyPreorder(preorder))


if __name__ == "__main__":
    unittest.main()