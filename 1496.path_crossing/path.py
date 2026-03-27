# 1496. Path Crossing
# Topics: 'Hash Table', 'String'

# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

 

# Example 1:

# Input: path = "NES"
# Output: false 
# Explanation: Notice that the path doesn't cross any point more than once.

# Example 2:

# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.

 

# Constraints:

#     1 <= path.length <= 104
#     path[i] is either 'N', 'S', 'E', or 'W'.

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        N = len(path)
        if N == 1:
            return False

        ps = set()
        i, j = 0, 0
        ps.add((i, j))
        for dr in path:
            if dr == 'N':
                i += 1
            elif dr == 'S':
                i -= 1
            elif dr == 'W':
                j += 1
            else:
                j -= 1
            if (i, j) in ps:
                return True
            else:
                ps.add((i,j))

        return False