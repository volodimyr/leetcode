import unittest
from happy import Solution

class TestGetHappyString(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    # --- Examples from the problem statement ---

    def test_example_1(self):
        self.assertEqual(self.sol.getHappyString(1, 3), "c")

    def test_example_2(self):
        self.assertEqual(self.sol.getHappyString(1, 4), "")

    def test_example_3(self):
        self.assertEqual(self.sol.getHappyString(3, 9), "cab")

    # --- Basic correctness tests ---

    def test_n_1_all(self):
        self.assertEqual(self.sol.getHappyString(1, 1), "a")
        self.assertEqual(self.sol.getHappyString(1, 2), "b")
        self.assertEqual(self.sol.getHappyString(1, 3), "c")

    def test_n_2_all(self):
        expected = ["ab", "ac", "ba", "bc", "ca", "cb"]
        for i, s in enumerate(expected, start=1):
            self.assertEqual(self.sol.getHappyString(2, i), s)

    def test_n_2_out_of_range(self):
        self.assertEqual(self.sol.getHappyString(2, 7), "")

    # --- Ordering tests ---

    def test_lexicographical_order(self):
        # n = 3, first few strings should be lexicographically sorted
        expected = [
            "aba", "abc", "aca", "acb",
            "bab", "bac", "bca", "bcb",
            "cab", "cac", "cba", "cbc"
        ]
        for i, s in enumerate(expected, start=1):
            self.assertEqual(self.sol.getHappyString(3, i), s)

    # --- Edge cases ---

    def test_large_k_but_small_n(self):
        self.assertEqual(self.sol.getHappyString(1, 100), "")
        self.assertEqual(self.sol.getHappyString(2, 100), "")

    def test_max_n_small_k(self):
        # Just check it returns something valid, not empty
        result = self.sol.getHappyString(10, 1)
        self.assertTrue(len(result) == 10)
        for i in range(len(result) - 1):
            self.assertNotEqual(result[i], result[i + 1])


if __name__ == "__main__":
    unittest.main()
