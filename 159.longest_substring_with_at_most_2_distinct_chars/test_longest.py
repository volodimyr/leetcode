
from longest import Solution

def test_basic_examples():
    """Test the provided examples"""
    sol = Solution()
    
    # Example 1
    assert sol.lengthOfLongestSubstringTwoDistinct("eceba") == 3, "Failed: eceba should return 3"
    print("✓ Example 1: 'eceba' -> 3 (substring: 'ece')")
    
    # Example 2
    assert sol.lengthOfLongestSubstringTwoDistinct("ccaabbb") == 5, "Failed: ccaabbb should return 5"
    print("✓ Example 2: 'ccaabbb' -> 5 (substring: 'aabbb' or 'caaab')")


def test_edge_cases():
    """Test edge cases"""
    sol = Solution()
    
    # Empty string
    assert sol.lengthOfLongestSubstringTwoDistinct("") == 0, "Failed: empty string"
    print("✓ Edge case: Empty string -> 0")
    
    # Single character
    assert sol.lengthOfLongestSubstringTwoDistinct("a") == 1, "Failed: single char"
    print("✓ Edge case: 'a' -> 1")
    
    # Two characters (same)
    assert sol.lengthOfLongestSubstringTwoDistinct("aa") == 2, "Failed: two same chars"
    print("✓ Edge case: 'aa' -> 2")
    
    # Two characters (different)
    assert sol.lengthOfLongestSubstringTwoDistinct("ab") == 2, "Failed: two different chars"
    print("✓ Edge case: 'ab' -> 2")


def test_all_same_character():
    """Test strings with all same characters"""
    sol = Solution()
    
    assert sol.lengthOfLongestSubstringTwoDistinct("aaaa") == 4, "Failed: all same"
    print("✓ All same: 'aaaa' -> 4")
    
    assert sol.lengthOfLongestSubstringTwoDistinct("zzzzzzzz") == 8, "Failed: 8 z's"
    print("✓ All same: 'zzzzzzzz' -> 8")


def test_two_distinct_characters():
    """Test strings with exactly two distinct characters"""
    sol = Solution()
    
    assert sol.lengthOfLongestSubstringTwoDistinct("aabb") == 4, "Failed: aabb"
    print("✓ Two distinct: 'aabb' -> 4")
    
    assert sol.lengthOfLongestSubstringTwoDistinct("abababab") == 8, "Failed: alternating"
    print("✓ Two distinct: 'abababab' -> 8")
    
    assert sol.lengthOfLongestSubstringTwoDistinct("aaabbb") == 6, "Failed: aaabbb"
    print("✓ Two distinct: 'aaabbb' -> 6")


def test_large_inputs():
    """Test with larger inputs to verify performance"""
    sol = Solution()
    
    # Large string with 2 distinct characters
    s1 = "a" * 50000 + "b" * 50000
    assert sol.lengthOfLongestSubstringTwoDistinct(s1) == 100000, "Failed: large two distinct"
    print("✓ Large input: 100,000 chars with 2 distinct -> 100000")
    
    # Large string with many characters
    s2 = "abc" * 10000
    result = sol.lengthOfLongestSubstringTwoDistinct(s2)
    assert result == 2, "Failed: large repeating pattern"
    print(f"✓ Large input: 30,000 chars with pattern 'abc'*10000 -> {result}")
    
    # Worst case: all different characters
    s3 = "".join(chr(97 + i % 26) for i in range(1000))
    result = sol.lengthOfLongestSubstringTwoDistinct(s3)
    print(f"✓ Large input: 1,000 chars cycling through alphabet -> {result}")


def test_special_sequences():
    """Test special character sequences"""
    sol = Solution()
    
    # Repeating triplets
    assert sol.lengthOfLongestSubstringTwoDistinct("aaabbbccc") == 6, "Failed: repeating triplets"
    print("✓ Special: 'aaabbbccc' -> 6 ('aaabbb' or 'bbbccc')")
    
    # Single char interruption
    assert sol.lengthOfLongestSubstringTwoDistinct("aaaaacaaaaa") == 11, "Failed: interruption"
    print("✓ Special: 'aaaaacaaaaa' -> 11")
    
    # Palindrome-like
    assert sol.lengthOfLongestSubstringTwoDistinct("abba") == 4, "Failed: abba"
    print("✓ Special: 'abba' -> 4")


def run_all_tests():
    """Run all test suites"""
    print("=" * 60)
    print("TESTING: Longest Substring with At Most Two Distinct Characters")
    print("=" * 60)
    
    test_suites = [
        ("Basic Examples", test_basic_examples),
        ("Edge Cases", test_edge_cases),
        ("All Same Character", test_all_same_character),
        ("Two Distinct Characters", test_two_distinct_characters),
        ("Large Inputs", test_large_inputs),
        ("Special Sequences", test_special_sequences),
    ]
    
    passed = 0
    failed = 0
    
    for suite_name, test_func in test_suites:
        print(f"\n{suite_name}:")
        print("-" * 60)
        try:
            test_func()
            passed += 1
        except AssertionError as e:
            print(f"❌ {suite_name} FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"❌ {suite_name} ERROR: {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} test suites passed, {failed} failed")
    print("=" * 60)
    
    if failed == 0:
        print("🎉 ALL TESTS PASSED! 🎉")
    
    return failed == 0


if __name__ == "__main__":
    run_all_tests()