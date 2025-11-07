from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i in range(len(nums)):
            if q and q[0] <= i - k:
                q.popleft()
            if not q:
                q.append(i)
            elif nums[q[0]] <= nums[i]:
                q.clear()
                q.append(i)
            else:
                while q and nums[q[-1]] <= nums[i]:
                    q.pop()
                q.append(i)
            
            if i >= k - 1:
                res.append(nums[q[0]])
        return res


def test_maxSlidingWindow():
    solution = Solution()
    
    # Example 1: Standard case
    assert solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    
    # Example 2: Single element
    assert solution.maxSlidingWindow([1], 1) == [1]
    
    # Window size equals array length
    assert solution.maxSlidingWindow([1,3,2,5,4], 5) == [5]
    
    # Increasing sequence
    assert solution.maxSlidingWindow([1,2,3,4,5], 3) == [3,4,5]
    
    # Decreasing sequence
    assert solution.maxSlidingWindow([5,4,3,2,1], 3) == [5,4,3]
    
    # All same elements
    assert solution.maxSlidingWindow([4,4,4,4,4], 3) == [4,4,4]
    
    # Window size 1 (each element is max)
    assert solution.maxSlidingWindow([1,3,-1,-3,5], 1) == [1,3,-1,-3,5]
    
    # Negative numbers
    assert solution.maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4) == [7,7,7,7,7]
    
    # Max at the beginning
    assert solution.maxSlidingWindow([9,1,2,3,4], 3) == [9,3,4]
    
    # Max at the end
    assert solution.maxSlidingWindow([1,2,3,4,9], 3) == [3,4,9]
    
    # Two elements, window size 2
    assert solution.maxSlidingWindow([1,3], 2) == [3]
    
    # Alternating high and low
    assert solution.maxSlidingWindow([1,5,2,6,3,7], 3) == [5,6,6,7]
    
    # Large window
    assert solution.maxSlidingWindow([1,2,3,4,5,6,7,8,9], 5) == [5,6,7,8,9]
    
    # Contains zeros
    assert solution.maxSlidingWindow([0,0,0,1,0,0,0], 3) == [0,1,1,1,0]
    
    # Mix of positive and negative
    assert solution.maxSlidingWindow([-1,-2,3,-4,5], 2) == [-1,3,3,5]
    
    print("All tests passed!")


if __name__ == "__main__":
    test_maxSlidingWindow()