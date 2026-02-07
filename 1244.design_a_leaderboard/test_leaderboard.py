import unittest
from leaderboard import Leaderboard


class TestLeaderboard(unittest.TestCase):

    def setUp(self):
        self.lb = Leaderboard()

    def test_add_score_new_players(self):
        self.lb.addScore(1, 50)
        self.lb.addScore(2, 30)
        self.lb.addScore(3, 20)

        self.assertEqual(self.lb.top(3), 100)

    def test_add_score_existing_player(self):
        self.lb.addScore(1, 50)
        self.lb.addScore(1, 25)

        self.assertEqual(self.lb.top(1), 75)

    def test_top_k_basic(self):
        self.lb.addScore(1, 50)
        self.lb.addScore(2, 30)
        self.lb.addScore(3, 20)

        self.assertEqual(self.lb.top(1), 50)
        self.assertEqual(self.lb.top(2), 80)

    def test_top_after_multiple_calls(self):
        self.lb.addScore(1, 50)
        self.lb.addScore(2, 30)

        self.assertEqual(self.lb.top(1), 50)
        self.assertEqual(self.lb.top(2), 80)

        # ensure repeated calls don't break lazy sorting
        self.assertEqual(self.lb.top(1), 50)

    def test_reset_player(self):
        self.lb.addScore(1, 50)
        self.lb.addScore(2, 30)

        self.lb.reset(1)

        self.assertEqual(self.lb.top(2), 30)

    def test_reset_then_add_again(self):
        self.lb.addScore(1, 50)
        self.lb.reset(1)
        self.lb.addScore(1, 40)

        self.assertEqual(self.lb.top(1), 40)

    def test_sorted_flag_invalidated(self):
        self.lb.addScore(1, 10)
        self.lb.addScore(2, 20)
        self.lb.top(2)

        # internal state should be sorted now
        self.assertTrue(self.lb.sorted)

        self.lb.addScore(1, 50)
        self.assertFalse(self.lb.sorted)


if __name__ == "__main__":
    unittest.main()
