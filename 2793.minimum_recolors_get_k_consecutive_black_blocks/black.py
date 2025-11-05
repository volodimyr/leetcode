# 2793. Minimum Recolors to Get K Consecutive Black Blocks
#  Topics: 'Array', 'Sliding Window'

# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

# You are also given an integer k, which is the desired number of consecutive black blocks.

# In one operation, you can recolor a white block such that it becomes a black block.

# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

 

# Example 1:

# Input: blocks = "WBBWWBBWBW", k = 7
# Output: 3
# Explanation:
# One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
# so that blocks = "BBBBBBBWBW". 
# It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
# Therefore, we return 3.

# Example 2:

# Input: blocks = "WBWBBBW", k = 2
# Output: 0
# Explanation:
# No changes need to be made, since 2 consecutive black blocks already exist.
# Therefore, we return 0.

 

# Constraints:

#     n == blocks.length
#     1 <= n <= 100
#     blocks[i] is either 'W' or 'B'.
#     1 <= k <= n

# O(k) memory, O(n) time
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w = 0
        list = []
        window_size = k
        for char in blocks:
            if char == 'W':
                w+=1
            list.append(char)
            window_size-=1
            if window_size == 0:
                break
        if w == 0:
            return 0
        min_replace = w

        for i in range(k, len(blocks), 1):
            if blocks[i] == 'W':
                w+=1
            list.append(blocks[i])
            if list[0] == 'W':
                w-=1
            min_replace = min(min_replace, w)
            if min_replace == 0:
                return 0
            del list[0]
        return min_replace

# O(1) memory, O(n) time
# class Solution:
    # def minimumRecolors(self, blocks: str, k: int) -> int:
    #     w = sum(1 for i in range(k) if blocks[i] == 'W')
    #     min_replace = w
        
    #     for i in range(k, len(blocks)):
    #         if blocks[i] == 'W':
    #             w += 1
    #         if blocks[i - k] == 'W':
    #             w -= 1
    #         min_replace = min(min_replace, w)
    #         if min_replace == 0:
    #             return 0
        
    #     return min_replace
