import unittest
from genetic import Solution

class TestMinMutation(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()

    def test_single_mutation(self):
        start = "AACCGGTT"
        end = "AACCGGTA"
        bank = ["AACCGGTA"]
        self.assertEqual(self.sol.minMutation(start, end, bank), 1)

    def test_two_mutations(self):
        start = "AACCGGTT"
        end = "AAACGGTA"
        bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
        self.assertEqual(self.sol.minMutation(start, end, bank), 2)

    def test_no_possible_mutation(self):
        start = "AAAAACCC"
        end = "AACCCCCC"
        bank = ["AAAACCCC", "AAACCCCC"]
        self.assertEqual(self.sol.minMutation(start, end, bank), -1)

    def test_start_equals_end(self):
        start = "AACCGGTT"
        end = "AACCGGTT"
        bank = ["AACCGGTA"]
        # Should be 0 since start == end
        self.assertEqual(self.sol.minMutation(start, end, bank), 0)

    def test_empty_bank(self):
        start = "AACCGGTT"
        end = "AACCGGTA"
        bank = []
        # No valid mutation possible
        self.assertEqual(self.sol.minMutation(start, end, bank), -1)

    def test_longer_path(self):
        start = "AAAAACCC"
        end = "CCCCCCCC"
        bank = ["AAAAACCC","AAAACCCC","AAACCCCC","AACCCCCC","ACCCCCCC","CCCCCCCC"]
        self.assertEqual(self.sol.minMutation(start, end, bank), 5)

if __name__ == "__main__":
    unittest.main()
