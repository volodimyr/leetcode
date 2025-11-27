from collections import Counter
from typing import List
from permutation import Solution

def run_test(nums: List[int], expected_perms: List[List[int]]):
    """
    Runs a single test case and asserts correctness.
    Compares the result set (tuples) against the expected set (tuples).
    """
    result = Solution().permuteUnique(nums)
    
    # Convert lists of lists to sets of tuples for order-independent comparison
    result_set = set(tuple(p) for p in result)
    expected_set = set(tuple(p) for p in expected_perms)

    assert result_set == expected_set, \
        f"\nInput: {nums}\nExpected Set: {expected_set}\nReceived Set: {result_set}\n"
    print(f"Test Passed for Input: {nums}")
    print(f"Result Count: {len(result_set)}")
    
# --- Tests ---
print("--- Running Permutation Tests ---")

# Example 1 (The classic case with duplicates)
# Input: [1, 1, 2]
# Expected: 3 permutations: (1, 1, 2), (1, 2, 1), (2, 1, 1)
run_test(
    nums=[1, 1, 2],
    expected_perms=[[1, 1, 2], [1, 2, 1], [2, 1, 1]]
)

# Example 2 (No duplicates - standard permutation)
# Input: [1, 2, 3]
# Expected: 6 permutations (3!)
run_test(
    nums=[1, 2, 3],
    expected_perms=[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
)

# Edge Case 1: All duplicates
# Input: [2, 2, 2]
# Expected: 1 permutation: (2, 2, 2)
run_test(
    nums=[2, 2, 2],
    expected_perms=[[2, 2, 2]]
)

# Edge Case 2: Empty input (Constraint check: length >= 1, but good practice)
# NOTE: Constraints say 1 <= nums.length, but testing the boundary before is safe.
# run_test(nums=[], expected_perms=[[]]) # Based on problem constraints, this won't happen.

# Edge Case 3: Single element
# Input: [5]
# Expected: 1 permutation: (5)
run_test(
    nums=[5],
    expected_perms=[[5]]
)

# Complex Case: Mixed duplicates
# Input: [1, 1, 2, 2]
# Expected: 6 permutations: 4! / (2! * 2!) = 24 / 4 = 6
# (1, 1, 2, 2), (1, 2, 1, 2), (1, 2, 2, 1), 
# (2, 1, 1, 2), (2, 1, 2, 1), (2, 2, 1, 1)
run_test(
    nums=[1, 1, 2, 2],
    expected_perms=[
        [1, 1, 2, 2], [1, 2, 1, 2], [1, 2, 2, 1], 
        [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1]
    ]
)

# Constraint Check: Negative numbers
# Input: [-1, 0, 1]
# Expected: 6 permutations
run_test(
    nums=[-1, 0, 1],
    expected_perms=[
        [-1, 0, 1], [-1, 1, 0], [0, -1, 1], 
        [0, 1, -1], [1, -1, 0], [1, 0, -1]
    ]
)

# Constraint Check: Negative duplicates
# Input: [-1, -1, 0]
# Expected: 3 permutations
run_test(
    nums=[-1, -1, 0],
    expected_perms=[[-1, -1, 0], [-1, 0, -1], [0, -1, -1]]
)