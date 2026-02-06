# 1197. Minimum Knight Moves
# Topics: 'Array', 'Breadth-First Search', 'Graph', 'Queue', 'Matrix', 'Dynamic Programming', 'Depth-First Search'
# Level: 'Medium'

# In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

# A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

# Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

# Example 1:

# Input: x = 2, y = 1

# Output: 1

# Explanation: [0, 0] → [2, 1]

# Example 2:

# Input: x = 5, y = 5

# Output: 4

# Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]

# Constraints:

#     -300 <= x, y <= 300
#     0 <= |x| + |y| <= 300

from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # optimization
        x, y = abs(x), abs(y)
        visit = set()
        q = deque()
        q.append((0,0,0))
        visit.add((0,0))


        while q:
            x1, y1, moves = q.popleft()
            if x1 == x and y1 == y:
                return moves

            for dr, dc in ((-1,-2),(-1,2),(-2,-1),(-2,1),(1,-2),(1,2),(2,-1),(2,1)):
                nr, nc = x1+dr, y1+dc
                # optimization
                if nr < -2 or nc < -2:
                    continue
                if (nr,nc) in visit:
                    continue
                visit.add((nr,nc))
                q.append((nr,nc,moves+1))

        return -1