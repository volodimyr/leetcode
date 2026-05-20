# 348. Design Tic-Tac-Toe
# Topics: 'Array', 'Hash Table', 'Design', 'Matrix'
# Level: 'Medium'

# Design a Tic-tac-toe game that is played between two players on an n x n grid.

# A move is guaranteed to be valid and is placed on an empty block.
# Once a winning condition is reached, no more moves are allowed.
# A player who succeeds in placing n of their marks in a horizontal, vertical,
# or diagonal row wins the game.

# Implement the TicTacToe class:
#     TicTacToe(int n) Initializes the object the size of the board n.
#     int move(int row, int col, int player) Indicates that the player with id
#     player plays at the cell (row, col) of the board. The move is guaranteed
#     to be a valid move. Return the winner of the game if there is one, else 0.

# Example 1:

# Input:
# ["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
# [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]

# Output:
# [null, 0, 0, 0, 0, 0, 0, 1]

# Explanation:
# TicTacToe ticTacToe = new TicTacToe(3);
# ticTacToe.move(0, 0, 1); // return 0 (no one wins)
# ticTacToe.move(0, 2, 2); // return 0 (no one wins)
# ticTacToe.move(2, 2, 1); // return 0 (no one wins)
# ticTacToe.move(1, 1, 2); // return 0 (no one wins)
# ticTacToe.move(2, 0, 1); // return 0 (no one wins)
# ticTacToe.move(1, 0, 2); // return 0 (no one wins)
# ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)

# Constraints:
#     2 <= n <= 100
#     player is 1 or 2.
#     0 <= row, col < n
#     (row, col) are unique for each different call to move.
#     At most n^2 calls will be made to move.


class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        horizontal = 0
        for c in range(self.n):
            if self.board[row][c] != player:
                break
            horizontal += 1
        if horizontal == self.n:
            return player

        vertical = 0
        for r in range(self.n):
            if self.board[r][col] != player:
                break
            vertical += 1
        if vertical == self.n:
            return player

        diagonal = 1
        r, c = row, col
        while True:
            r -= 1
            c -= 1
            if min(r, c) < 0:
                break
            if self.board[r][c] != player:
                break
            diagonal += 1

        r, c = row, col
        while True:
            r += 1
            c += 1
            if max(r, c) >= self.n:
                break
            if self.board[r][c] != player:
                break
            diagonal += 1

        if diagonal == self.n:
            return player

        diagonal = 1
        r, c = row, col
        while True:
            r -= 1
            c += 1
            if r < 0 or c >= self.n:
                break
            if self.board[r][c] != player:
                break
            diagonal += 1

        r, c = row, col
        while True:
            r += 1
            c -= 1
            if c < 0 or r >= self.n:
                break
            if self.board[r][c] != player:
                break
            diagonal += 1

        return player if diagonal == self.n else 0
