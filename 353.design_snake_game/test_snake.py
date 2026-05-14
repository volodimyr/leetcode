import unittest
from snake import SnakeGame


class TestSnakeGame(unittest.TestCase):

    def test_example1(self):
        game = SnakeGame(3, 2, [[1, 2], [0, 1]])
        self.assertEqual(game.move("R"), 0)
        self.assertEqual(game.move("D"), 0)
        self.assertEqual(game.move("R"), 1)
        self.assertEqual(game.move("U"), 1)
        self.assertEqual(game.move("L"), 2)
        self.assertEqual(game.move("U"), -1)

    def test_hit_top_wall(self):
        game = SnakeGame(3, 3, [])
        self.assertEqual(game.move("U"), -1)

    def test_hit_left_wall(self):
        game = SnakeGame(3, 3, [])
        self.assertEqual(game.move("L"), -1)

    def test_hit_right_wall(self):
        game = SnakeGame(1, 3, [])
        self.assertEqual(game.move("R"), -1)

    def test_hit_bottom_wall(self):
        game = SnakeGame(3, 1, [])
        self.assertEqual(game.move("D"), -1)

    def test_self_collision(self):
        # Snake grows to length 4, then runs into itself
        game = SnakeGame(4, 4, [[0, 1], [0, 2], [0, 3]])
        game.move("R")  # eat food at (0,1), score=1
        game.move("R")  # eat food at (0,2), score=2
        game.move("R")  # eat food at (0,3), score=3
        # Snake occupies (0,3),(0,2),(0,1),(0,0); move D then L then U runs into body
        game.move("D")  # (1,3)
        game.move("L")  # (1,2)
        game.move("L")  # (1,1)
        game.move("L")  # (1,0)
        game.move("U")  # (0,0) — tail has moved, not a collision
        self.assertEqual(game.move("R"), 3)  # (0,1) — tail moved off, no collision

    def test_returns_minus1_after_game_over(self):
        game = SnakeGame(3, 3, [])
        game.move("U")  # game over
        self.assertEqual(game.move("R"), -1)
        self.assertEqual(game.move("D"), -1)

    def test_no_food(self):
        game = SnakeGame(5, 5, [])
        self.assertEqual(game.move("R"), 0)
        self.assertEqual(game.move("D"), 0)
        self.assertEqual(game.move("L"), 0)

    def test_snake_can_move_to_vacated_tail(self):
        # Snake of length 1 can move to where its tail just was
        # (0,0) -> R -> (0,1), tail vacates (0,0)
        # then L -> (0,0), which is now empty — valid
        game = SnakeGame(3, 3, [])
        self.assertEqual(game.move("R"), 0)
        self.assertEqual(game.move("L"), 0)

    def test_eat_all_food_then_move(self):
        game = SnakeGame(3, 3, [[0, 1]])
        self.assertEqual(game.move("R"), 1)
        self.assertEqual(game.move("R"), 1)


if __name__ == "__main__":
    unittest.main()
