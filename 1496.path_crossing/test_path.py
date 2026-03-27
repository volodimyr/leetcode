from path import Solution

s = Solution()

assert s.isPathCrossing("NES") == False
assert s.isPathCrossing("NESWW") == True
assert s.isPathCrossing("N") == False
assert s.isPathCrossing("NESW") == True   # returns to origin
assert s.isPathCrossing("NN") == False

print("all tests passed")
