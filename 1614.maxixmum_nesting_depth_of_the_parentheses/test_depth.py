import unittest
from depth import Solution


class TestMaxDepth(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.maxDepth("(1+(2*3)+((8)/4))+1"), 3)

    def test_example2(self):
        self.assertEqual(self.solution.maxDepth("(1)+((2))+(((3)))"), 3)

    def test_example3(self):
        self.assertEqual(self.solution.maxDepth("()(())((()()))"), 3)

    def test_single_pair(self):
        self.assertEqual(self.solution.maxDepth("(1)"), 1)

    def test_flat_pairs(self):
        self.assertEqual(self.solution.maxDepth("()()()"), 1)


if __name__ == "__main__":
    unittest.main()
