from merge import ListNode
from merge import Solution

# Helper functions
def create_linked_list(arr):
    """Create a linked list from an array"""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_array(head):
    """Convert a linked list to an array"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
def test_example_1():
    """Example 1: Remove middle nodes and insert list2"""
    sol = Solution()
    list1 = create_linked_list([10, 1, 13, 6, 9, 5])
    list2 = create_linked_list([1000000, 1000001, 1000002])
    result = sol.mergeInBetween(list1, 3, 4, list2)
    expected = [10, 1, 13, 1000000, 1000001, 1000002, 5]
    assert linked_list_to_array(result) == expected, f"Expected {expected}, got {linked_list_to_array(result)}"
    print("[PASS] Test 1 passed: Example 1")

def test_example_2():
    """Example 2: Remove larger range"""
    sol = Solution()
    list1 = create_linked_list([0, 1, 2, 3, 4, 5, 6])
    list2 = create_linked_list([1000000, 1000001, 1000002, 1000003, 1000004])
    result = sol.mergeInBetween(list1, 2, 5, list2)
    expected = [0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6]
    assert linked_list_to_array(result) == expected, f"Expected {expected}, got {linked_list_to_array(result)}"
    print("[PASS] Test 2 passed: Example 2")

def test_remove_single_node():
    """Remove a single node (a == b)"""
    sol = Solution()
    list1 = create_linked_list([1, 2, 3, 4, 5])
    list2 = create_linked_list([10, 20])
    result = sol.mergeInBetween(list1, 2, 2, list2)
    expected = [1, 2, 10, 20, 4, 5]
    assert linked_list_to_array(result) == expected, f"Expected {expected}, got {linked_list_to_array(result)}"
    print("[PASS] Test 3 passed: Remove single node")

def test_remove_at_start():
    """Remove nodes starting from index 1"""
    sol = Solution()
    list1 = create_linked_list([1, 2, 3, 4, 5])
    list2 = create_linked_list([100, 200])
    result = sol.mergeInBetween(list1, 1, 2, list2)
    expected = [1, 100, 200, 4, 5]
    assert linked_list_to_array(result) == expected, f"Expected {expected}, got {linked_list_to_array(result)}"
    print("[PASS] Test 4 passed: Remove at start")

def test_remove_till_end():
    """Remove nodes till near the end"""
    sol = Solution()
    list1 = create_linked_list([1, 2, 3, 4, 5, 6])
    list2 = create_linked_list([100])
    result = sol.mergeInBetween(list1, 2, 4, list2)
    expected = [1, 2, 100, 6]
    assert linked_list_to_array(result) == expected, f"Expected {expected}, got {linked_list_to_array(result)}"
    print("[PASS] Test 5 passed: Remove till near end")

def test_single_node_list2():
    """list2 has only one node"""
    sol = Solution()
    list1 = create_linked_list([1, 2, 3, 4, 5])
    list2 = create_linked_list([99])
    result = sol.mergeInBetween(list1, 1, 3, list2)
    expected = [1, 99, 5]
    assert linked_list_to_array(result) == expected, f"Expected {expected}, got {linked_list_to_array(result)}"
    print("[PASS] Test 6 passed: Single node list2")

def test_long_list2():
    """list2 is longer than the removed section"""
    sol = Solution()
    list1 = create_linked_list([1, 2, 3, 4])
    list2 = create_linked_list([10, 20, 30, 40, 50])
    result = sol.mergeInBetween(list1, 1, 1, list2)
    expected = [1, 10, 20, 30, 40, 50, 3, 4]
    assert linked_list_to_array(result) == expected, f"Expected {expected}, got {linked_list_to_array(result)}"
    print("[PASS] Test 7 passed: Long list2")

def test_minimum_list1():
    """Minimum size list1 (3 nodes)"""
    sol = Solution()
    list1 = create_linked_list([1, 2, 3])
    list2 = create_linked_list([100])
    result = sol.mergeInBetween(list1, 1, 1, list2)
    expected = [1, 100, 3]
    assert linked_list_to_array(result) == expected, f"Expected {expected}, got {linked_list_to_array(result)}"
    print("[PASS] Test 8 passed: Minimum list1")

def test_large_values():
    """Test with large values"""
    sol = Solution()
    list1 = create_linked_list([0, 1, 2, 3, 4])
    list2 = create_linked_list([1000000, 9999999])
    result = sol.mergeInBetween(list1, 2, 3, list2)
    expected = [0, 1, 1000000, 9999999, 4]
    assert linked_list_to_array(result) == expected, f"Expected {expected}, got {linked_list_to_array(result)}"
    print("[PASS] Test 9 passed: Large values")

def test_consecutive_range():
    """Remove consecutive nodes in middle"""
    sol = Solution()
    list1 = create_linked_list([5, 10, 15, 20, 25, 30])
    list2 = create_linked_list([100, 200, 300])
    result = sol.mergeInBetween(list1, 2, 3, list2)
    expected = [5, 10, 100, 200, 300, 25, 30]
    assert linked_list_to_array(result) == expected, f"Expected {expected}, got {linked_list_to_array(result)}"
    print("[PASS] Test 10 passed: Consecutive range")

# Run all tests
if __name__ == "__main__":
    print("Running tests...\n")
    test_example_1()
    test_example_2()
    test_remove_single_node()
    test_remove_at_start()
    test_remove_till_end()
    test_single_node_list2()
    test_long_list2()
    test_minimum_list1()
    test_large_values()
    test_consecutive_range()
    print("\n[PASS] All tests passed!")