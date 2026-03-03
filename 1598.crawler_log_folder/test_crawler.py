import unittest
from crawler import Solution


class TestCrawlerLogFolder(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        logs = ["d1/", "d2/", "../", "d21/", "./"]
        self.assertEqual(self.solution.minOperations(logs), 2)

    def test_example_2(self):
        logs = ["d1/", "d2/", "./", "d3/", "../", "d31/"]
        self.assertEqual(self.solution.minOperations(logs), 3)

    def test_example_3(self):
        logs = ["d1/", "../", "../", "../"]
        self.assertEqual(self.solution.minOperations(logs), 0)

    def test_only_current_directory(self):
        logs = ["./", "./", "./"]
        self.assertEqual(self.solution.minOperations(logs), 0)

    def test_only_child_directories(self):
        logs = ["a/", "b/", "c/"]
        self.assertEqual(self.solution.minOperations(logs), 3)

    def test_parent_at_root(self):
        logs = ["../", "../", "../"]
        self.assertEqual(self.solution.minOperations(logs), 0)

    def test_mixed_operations(self):
        logs = ["a/", "b/", "../", "c/", "../", "../"]
        self.assertEqual(self.solution.minOperations(logs), 0)

    def test_single_operation(self):
        logs = ["folder/"]
        self.assertEqual(self.solution.minOperations(logs), 1)


if __name__ == "__main__":
    unittest.main()