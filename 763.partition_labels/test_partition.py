import unittest
from partition import Solution


class TestPartitionLabels(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "ababcbacadefegdehijhklij"
        expected = [9, 7, 8]
        self.assertEqual(self.solution.partitionLabels(s), expected)

    def test_example_2(self):
        s = "eccbbbbdec"
        expected = [10]
        self.assertEqual(self.solution.partitionLabels(s), expected)

    def test_single_character(self):
        s = "a"
        expected = [1]
        self.assertEqual(self.solution.partitionLabels(s), expected)

    def test_all_unique_characters(self):
        s = "abc"
        expected = [1, 1, 1]
        self.assertEqual(self.solution.partitionLabels(s), expected)

    def test_all_same_characters(self):
        s = "aaaaa"
        expected = [5]
        self.assertEqual(self.solution.partitionLabels(s), expected)

    def test_two_partitions(self):
        s = "abac"
        expected = [3, 1]
        self.assertEqual(self.solution.partitionLabels(s), expected)

    def test_complex_case(self):
        s = "caedbdedda"
        expected = [1, 9]
        self.assertEqual(self.solution.partitionLabels(s), expected)

    def test_minimum_length(self):
        s = "z"
        expected = [1]
        self.assertEqual(self.solution.partitionLabels(s), expected)


if __name__ == "__main__":
    unittest.main()