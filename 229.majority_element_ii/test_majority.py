from majority import Solution


def test_example1():
    """Test case from example 1"""
    solution = Solution()
    nums = [3, 2, 3]
    result = solution.majorityElement(nums)
    assert result == [3], f"Expected [3], got {result}"
    print("[PASS] test_example1 passed")


def test_example2():
    """Test case from example 2"""
    solution = Solution()
    nums = [1]
    result = solution.majorityElement(nums)
    assert result == [1], f"Expected [1], got {result}"
    print("[PASS] test_example2 passed")


def test_example3():
    """Test case from example 3"""
    solution = Solution()
    nums = [1, 2]
    result = solution.majorityElement(nums)
    assert set(result) == {1, 2}, f"Expected [1, 2], got {result}"
    print("[PASS] test_example3 passed")


def test_two_majority_elements():
    """Test with two elements appearing more than n/3 times"""
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 2, 3]
    result = solution.majorityElement(nums)
    assert set(result) == {1, 2}, f"Expected [1, 2], got {result}"
    print("[PASS] test_two_majority_elements passed")


def test_single_majority_element():
    """Test with one element appearing more than n/3 times"""
    solution = Solution()
    nums = [1, 1, 1, 2, 3, 4, 5]
    result = solution.majorityElement(nums)
    assert result == [1], f"Expected [1], got {result}"
    print("[PASS] test_single_majority_element passed")


def test_all_same_elements():
    """Test with all elements the same"""
    solution = Solution()
    nums = [5, 5, 5, 5, 5]
    result = solution.majorityElement(nums)
    assert result == [5], f"Expected [5], got {result}"
    print("[PASS] test_all_same_elements passed")


def test_no_majority_element():
    """Test where no element appears more than n/3 times"""
    solution = Solution()
    nums = [1, 2, 3, 4, 5, 6]
    result = solution.majorityElement(nums)
    assert result == [], f"Expected [], got {result}"
    print("[PASS] test_no_majority_element passed")


def test_negative_numbers():
    """Test with negative numbers"""
    solution = Solution()
    nums = [-1, -1, -1, 0, 0, 0, 1]
    result = solution.majorityElement(nums)
    assert set(result) == {-1, 0}, f"Expected [-1, 0], got {result}"
    print("[PASS] test_negative_numbers passed")


def test_large_numbers():
    """Test with numbers at constraint boundaries"""
    solution = Solution()
    nums = [1000000000, 1000000000, 1000000000, -1000000000]
    result = solution.majorityElement(nums)
    assert result == [1000000000], f"Expected [1000000000], got {result}"
    print("[PASS] test_large_numbers passed")


def test_exactly_threshold():
    """Test element appearing exactly at n/3 (should not be included)"""
    solution = Solution()
    nums = [1, 1, 2, 2, 3, 3]  # n=6, n//3=2, each appears exactly 2 times
    result = solution.majorityElement(nums)
    assert result == [], f"Expected [], got {result}"
    print("[PASS] test_exactly_threshold passed")


def test_just_above_threshold():
    """Test element appearing just above n/3 threshold"""
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]  # n=6, n//3=2, 1 appears 3 times (>2)
    result = solution.majorityElement(nums)
    assert result == [1], f"Expected [1], got {result}"
    print("[PASS] test_just_above_threshold passed")


def test_three_elements_equal():
    """Test with three elements each appearing once (n=3, n//3=1)"""
    solution = Solution()
    nums = [1, 2, 3]
    result = solution.majorityElement(nums)
    assert result == [], f"Expected [], got {result}"
    print("[PASS] test_three_elements_equal passed")


def test_duplicates_scattered():
    """Test with majority elements scattered throughout array"""
    solution = Solution()
    nums = [1, 3, 1, 3, 1, 3, 2, 4, 5]
    result = solution.majorityElement(nums)
    assert result == [], f"Expected [], got {result}"
    print("[PASS] test_duplicates_scattered passed")


def test_long_array():
    """Test with a longer array"""
    solution = Solution()
    nums = [1] * 40 + [2] * 35 + [3] * 25  # n=100, threshold=33
    result = solution.majorityElement(nums)
    assert set(result) == {1, 2}, f"Expected [1, 2], got {result}"
    print("[PASS] test_long_array passed")


def run_all_tests():
    """Run all test cases"""
    tests = [
        test_example1,
        test_example2,
        test_example3,
        test_two_majority_elements,
        test_single_majority_element,
        test_all_same_elements,
        test_no_majority_element,
        test_negative_numbers,
        test_large_numbers,
        test_exactly_threshold,
        test_just_above_threshold,
        test_three_elements_equal,
        test_duplicates_scattered,
        test_long_array,
    ]
    
    print("Running tests...\n")
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"[FAIL] {test.__name__} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"[FAIL] {test.__name__} error: {e}")
            failed += 1
    
    print(f"\n{'='*50}")
    print(f"Results: {passed} passed, {failed} failed out of {len(tests)} tests")
    print(f"{'='*50}")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)