from ribbons import Solution

def test_maxLength():
    solution = Solution()

    # Example 1
    assert solution.maxLength([9, 7, 5], 3) == 5

    # Example 2
    assert solution.maxLength([7, 5, 9], 4) == 4

    # Example 3 - impossible
    assert solution.maxLength([5, 7, 9], 22) == 0

    # Single ribbon single piece
    assert solution.maxLength([10], 1) == 10

    # Single ribbon multiple pieces
    assert solution.maxLength([10], 3) == 3

    # All ribbons same length
    assert solution.maxLength([5, 5, 5, 5], 4) == 5

    # k equals total segments
    assert solution.maxLength([4, 4, 4], 6) == 2

    # k is one - answer is max ribbon
    assert solution.maxLength([3, 7, 2], 1) == 7

    # Large k just possible
    assert solution.maxLength([10, 10, 10], 30) == 1

    # Large k impossible
    assert solution.maxLength([10, 10, 10], 31) == 0

    # Mixed lengths
    assert solution.maxLength([1, 2, 3, 4, 9], 5) == 3

    print("All tests passed!")

if __name__ == "__main__":
    test_maxLength()
