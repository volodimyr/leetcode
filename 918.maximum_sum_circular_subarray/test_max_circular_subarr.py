from max_circular_subarr import Solution

def test_maxSubarraySumCircular():
    solution = Solution()
    
    # Example 1: Simple case, max is single element
    assert solution.maxSubarraySumCircular([1, -2, 3, -2]) == 3
    
    # Example 2: Wrapping case - classic circular advantage
    assert solution.maxSubarraySumCircular([5, -3, 5]) == 10
    
    # Example 3: All negative numbers
    assert solution.maxSubarraySumCircular([-3, -2, -3]) == -2
    
    # Single element
    assert solution.maxSubarraySumCircular([5]) == 5
    assert solution.maxSubarraySumCircular([-5]) == -5
    
    # Two elements
    assert solution.maxSubarraySumCircular([1, 2]) == 3
    assert solution.maxSubarraySumCircular([-1, -2]) == -1
    
    # All positive numbers - should take entire array
    assert solution.maxSubarraySumCircular([1, 2, 3, 4]) == 10
    
    # Wrapping gives better result than non-wrapping
    assert solution.maxSubarraySumCircular([8, -1, -1, -1, 8]) == 16  # Take both 8s
    
    # Non-wrapping is better
    assert solution.maxSubarraySumCircular([1, -2, 3, -2, 5]) == 7  # [3, -2, 5]
    
    # Mix of positive and negative
    assert solution.maxSubarraySumCircular([3, -1, 2, -1]) == 4  # Entire array
    assert solution.maxSubarraySumCircular([3, -2, 2, -3]) == 3  # Either single 3 or [2, -3, 3]
    
    # Large positive at ends, negative in middle
    assert solution.maxSubarraySumCircular([5, -3, 5, -3, 5]) == 12  # Wrap around
    
    # Edge case: zeros
    assert solution.maxSubarraySumCircular([0, 0, 0]) == 0
    assert solution.maxSubarraySumCircular([-1, 0, -1]) == 0
    
    # Large array pattern
    assert solution.maxSubarraySumCircular([1, -1, 1, -1, 1]) == 2  # Wrapping
    
    print("All tests passed!")

if __name__ == "__main__":
    test_maxSubarraySumCircular()