import unittest
from dota import Solution


class TestPredictPartyVictory(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    # --- Given Examples ---

    def test_example_1(self):
        self.assertEqual(self.sol.predictPartyVictory("RD"), "Radiant")

    def test_example_2(self):
        self.assertEqual(self.sol.predictPartyVictory("RDD"), "Dire")

    # --- Edge Cases ---

    def test_single_radiant(self):
        self.assertEqual(self.sol.predictPartyVictory("R"), "Radiant")

    def test_single_dire(self):
        self.assertEqual(self.sol.predictPartyVictory("D"), "Dire")

    def test_all_radiant(self):
        self.assertEqual(self.sol.predictPartyVictory("RRRR"), "Radiant")

    def test_all_dire(self):
        self.assertEqual(self.sol.predictPartyVictory("DDDD"), "Dire")

    # --- Alternating Patterns ---

    def test_alternating_start_r(self):
        self.assertEqual(self.sol.predictPartyVictory("RDRD"), "Radiant")

    def test_alternating_start_d(self):
        self.assertEqual(self.sol.predictPartyVictory("DRDR"), "Dire")

    # --- More Complex Cases ---

    def test_longer_case_1(self):
        self.assertEqual(self.sol.predictPartyVictory("RRDDD"), "Radiant")

    def test_longer_case_2(self):
        self.assertEqual(self.sol.predictPartyVictory("DDRRR"), "Dire")

    def test_balanced_complex(self):
        self.assertEqual(self.sol.predictPartyVictory("RDRRDD"), "Radiant")

    def test_large_block(self):
        senate = "R" * 50 + "D" * 50
        self.assertEqual(self.sol.predictPartyVictory(senate), "Radiant")


if __name__ == "__main__":
    unittest.main()