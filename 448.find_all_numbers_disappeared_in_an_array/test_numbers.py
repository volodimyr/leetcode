from numbers import Solution

s = Solution()

assert s.findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5,6]
assert s.findDisappearedNumbers([1,1]) == [2]
assert s.findDisappearedNumbers([1,2,3]) == []          # none missing
assert s.findDisappearedNumbers([2,2,2]) == [1,3]       # all duplicates
assert s.findDisappearedNumbers([1]) == []              # single element, present

print("All tests passed")
