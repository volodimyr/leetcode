from collections import deque
from typing import List
from path import Solution

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1:
            return -1
        length = 1
        visit = set()
        q = deque()
        q.append((0,0))
        visit.add((0,0))

        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                if row == ROWS-1 and col == COLS-1:
                    return length
                directions = [
                # diagonals
                    [-1,-1], [-1, 1], [1, -1], [1, 1], 
                # straight
                    [0, 1], [0, -1], [1, 0], [-1, 0]
                ]
                for dr, dc in directions:
                    if min(row + dr, col+dc) < 0:
                        continue
                    if row + dr == ROWS or col + dc == COLS:
                        continue
                    if (row+dr, col+dc) in visit:
                        continue
                    if grid[row+dr][col+dc] == 1:
                        continue
                    visit.add((row+dr,col+dc))
                    q.append((row+dr, col+dc))
            length+=1
        return -1


def test_shortest_path():
    solution = Solution()
    
    # Test 1: Example 1 from problem - 2x2 grid
    grid1 = [[0,1],
             [1,0]]
    assert solution.shortestPathBinaryMatrix(grid1) == 2, "Test 1 Failed"
    print("✓ Test 1 passed: Example 1 - 2x2 grid")
    
    # Test 2: Example 2 from problem - 3x3 grid
    grid2 = [[0,0,0],
             [1,1,0],
             [1,1,0]]
    assert solution.shortestPathBinaryMatrix(grid2) == 4, "Test 2 Failed"
    print("✓ Test 2 passed: Example 2 - 3x3 grid with path")
    
    # Test 3: Example 3 from problem - no path (starting cell blocked)
    grid3 = [[1,0,0],
             [1,1,0],
             [1,1,0]]
    assert solution.shortestPathBinaryMatrix(grid3) == -1, "Test 3 Failed"
    print("✓ Test 3 passed: Example 3 - starting cell blocked")
    
    # Test 4: Direct diagonal path
    grid4 = [[0,0,0],
             [0,0,0],
             [0,0,0]]
    assert solution.shortestPathBinaryMatrix(grid4) == 3, "Test 4 Failed"
    print("✓ Test 4 passed: Direct diagonal path")
    
    # Test 5: Ending cell blocked
    grid5 = [[0,0,0],
             [0,0,0],
             [0,0,1]]
    assert solution.shortestPathBinaryMatrix(grid5) == -1, "Test 5 Failed"
    print("✓ Test 5 passed: Ending cell blocked")
    
    # Test 6: No path exists (wall in middle)
    grid6 = [[0,0,1],
             [1,1,1],
             [1,0,0]]
    assert solution.shortestPathBinaryMatrix(grid6) == -1, "Test 6 Failed"
    print("✓ Test 6 passed: No path exists")
    
    # Test 7: Single cell (edge case)
    grid7 = [[0]]
    assert solution.shortestPathBinaryMatrix(grid7) == 1, "Test 7 Failed"
    print("✓ Test 7 passed: Single cell grid")
    
    # Test 8: Single cell blocked
    grid8 = [[1]]
    assert solution.shortestPathBinaryMatrix(grid8) == -1, "Test 8 Failed"
    print("✓ Test 8 passed: Single cell blocked")
    
    # Test 9: Longer path needed
    grid9 = [[0,0,0,0],
             [1,1,1,0],
             [0,0,0,0],
             [0,1,1,0]]
    result9 = solution.shortestPathBinaryMatrix(grid9)
    assert result9 == 6, f"Test 9 Failed: Expected 5, got {result9}"
    print("✓ Test 9 passed: Longer path with obstacles")


    print("\n✅ All tests passed!")

if __name__ == "__main__":
    test_shortest_path()