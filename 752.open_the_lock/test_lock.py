import unittest
from lock import Solution  # adjust filename if needed


class TestOpenLock(unittest.TestCase):

    def test_example_1(self):
        dead = ["0201","0101","0102","1212","2002"]
        target = "0202"
        self.assertEqual(Solution().openLock(dead, target), 6)

    def test_example_2(self):
        dead = ["8888"]
        target = "0009"
        self.assertEqual(Solution().openLock(dead, target), 1)

    def test_example_3(self):
        dead = ["8887","8889","8878","8898","8788","8988","7888","9888"]
        target = "8888"
        self.assertEqual(Solution().openLock(dead, target), -1)

    def test_start_in_deadends(self):
        dead = ["0000"]
        target = "9999"
        self.assertEqual(Solution().openLock(dead, target), -1)

    def test_target_is_start(self):
        dead = []
        target = "0000"
        self.assertEqual(Solution().openLock(dead, target), 0)

    def test_no_deadends_small_target(self):
        dead = []
        target = "0001"
        self.assertEqual(Solution().openLock(dead, target), 1)

    def test_deadends_block_single_digit(self):
        dead = ["0001"]
        target = "0002"
        # BFS finds the shortest path in 4 moves
        self.assertEqual(Solution().openLock(dead, target), 4)

    def test_large_deadends_but_path_exists(self):
        dead = ["0001", "0002", "0003", "0004", "0005", "0006", "0007", "0008"]
        target = "0009"
        self.assertEqual(Solution().openLock(dead, target), 1)

    def test_blocked_middle_path(self):
        dead = ["1000", "0100", "0010", "0001"]
        target = "9999"
        # Optimal path: 0000→9000→9900→9990→9999 (4 moves)
        self.assertEqual(Solution().openLock(dead, target), 4)


if __name__ == "__main__":
    unittest.main()
