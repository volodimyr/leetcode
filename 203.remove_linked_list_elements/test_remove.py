import unittest
from typing import Optional, List
from remove import ListNode, Solution

class TestRemoveElements(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
    
    def list_to_linked_list(self, arr: List[int]) -> Optional[ListNode]:
        """Helper: Convert list to linked list"""
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    def linked_list_to_list(self, head: Optional[ListNode]) -> List[int]:
        """Helper: Convert linked list to list"""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    # Example test cases
    def test_example1(self):
        head = self.list_to_linked_list([1,2,6,3,4,5,6])
        result = self.s.removeElements(head, 6)
        self.assertEqual(self.linked_list_to_list(result), [1,2,3,4,5])
    
    def test_example2(self):
        head = self.list_to_linked_list([])
        result = self.s.removeElements(head, 1)
        self.assertEqual(self.linked_list_to_list(result), [])
    
    def test_example3(self):
        head = self.list_to_linked_list([7,7,7,7])
        result = self.s.removeElements(head, 7)
        self.assertEqual(self.linked_list_to_list(result), [])
    
    # Edge cases - empty list
    def test_empty_list(self):
        result = self.s.removeElements(None, 5)
        self.assertIsNone(result)
    
    # Single element cases
    def test_single_element_remove(self):
        head = self.list_to_linked_list([1])
        result = self.s.removeElements(head, 1)
        self.assertEqual(self.linked_list_to_list(result), [])
    
    def test_single_element_keep(self):
        head = self.list_to_linked_list([1])
        result = self.s.removeElements(head, 2)
        self.assertEqual(self.linked_list_to_list(result), [1])
    
    # Remove from head
    def test_remove_head_only(self):
        head = self.list_to_linked_list([1,2,3,4,5])
        result = self.s.removeElements(head, 1)
        self.assertEqual(self.linked_list_to_list(result), [2,3,4,5])
    
    def test_remove_multiple_from_head(self):
        head = self.list_to_linked_list([1,1,1,2,3])
        result = self.s.removeElements(head, 1)
        self.assertEqual(self.linked_list_to_list(result), [2,3])
    
    # Remove from tail
    def test_remove_tail_only(self):
        head = self.list_to_linked_list([1,2,3,4,5])
        result = self.s.removeElements(head, 5)
        self.assertEqual(self.linked_list_to_list(result), [1,2,3,4])
    
    def test_remove_multiple_from_tail(self):
        head = self.list_to_linked_list([1,2,3,3,3])
        result = self.s.removeElements(head, 3)
        self.assertEqual(self.linked_list_to_list(result), [1,2])
    
    # Remove from middle
    def test_remove_middle_only(self):
        head = self.list_to_linked_list([1,2,3,4,5])
        result = self.s.removeElements(head, 3)
        self.assertEqual(self.linked_list_to_list(result), [1,2,4,5])
    
    def test_remove_multiple_from_middle(self):
        head = self.list_to_linked_list([1,2,3,3,3,4,5])
        result = self.s.removeElements(head, 3)
        self.assertEqual(self.linked_list_to_list(result), [1,2,4,5])
    
    # Remove scattered elements
    def test_remove_scattered(self):
        head = self.list_to_linked_list([1,2,1,3,1,4,1])
        result = self.s.removeElements(head, 1)
        self.assertEqual(self.linked_list_to_list(result), [2,3,4])
    
    def test_remove_alternating(self):
        head = self.list_to_linked_list([1,2,1,2,1,2])
        result = self.s.removeElements(head, 1)
        self.assertEqual(self.linked_list_to_list(result), [2,2,2])
    
    # No elements to remove
    def test_no_match(self):
        head = self.list_to_linked_list([1,2,3,4,5])
        result = self.s.removeElements(head, 6)
        self.assertEqual(self.linked_list_to_list(result), [1,2,3,4,5])
    
    def test_no_match_single(self):
        head = self.list_to_linked_list([5])
        result = self.s.removeElements(head, 3)
        self.assertEqual(self.linked_list_to_list(result), [5])
    
    # Consecutive duplicates
    def test_consecutive_duplicates_at_start(self):
        head = self.list_to_linked_list([5,5,5,1,2,3])
        result = self.s.removeElements(head, 5)
        self.assertEqual(self.linked_list_to_list(result), [1,2,3])
    
    def test_consecutive_duplicates_at_end(self):
        head = self.list_to_linked_list([1,2,3,5,5,5])
        result = self.s.removeElements(head, 5)
        self.assertEqual(self.linked_list_to_list(result), [1,2,3])
    
    def test_consecutive_duplicates_in_middle(self):
        head = self.list_to_linked_list([1,2,5,5,5,3,4])
        result = self.s.removeElements(head, 5)
        self.assertEqual(self.linked_list_to_list(result), [1,2,3,4])
    
    # Two element lists
    def test_two_elements_remove_first(self):
        head = self.list_to_linked_list([1,2])
        result = self.s.removeElements(head, 1)
        self.assertEqual(self.linked_list_to_list(result), [2])
    
    def test_two_elements_remove_second(self):
        head = self.list_to_linked_list([1,2])
        result = self.s.removeElements(head, 2)
        self.assertEqual(self.linked_list_to_list(result), [1])
    
    def test_two_elements_remove_both(self):
        head = self.list_to_linked_list([1,1])
        result = self.s.removeElements(head, 1)
        self.assertEqual(self.linked_list_to_list(result), [])
    
    def test_two_elements_remove_none(self):
        head = self.list_to_linked_list([1,2])
        result = self.s.removeElements(head, 3)
        self.assertEqual(self.linked_list_to_list(result), [1,2])
    
    # Boundary values
    def test_val_at_min(self):
        head = self.list_to_linked_list([1,2,3,1,4])
        result = self.s.removeElements(head, 1)
        self.assertEqual(self.linked_list_to_list(result), [2,3,4])
    
    def test_val_at_max(self):
        head = self.list_to_linked_list([50,1,50,2,50])
        result = self.s.removeElements(head, 50)
        self.assertEqual(self.linked_list_to_list(result), [1,2])
    
    # Long list
    def test_long_list(self):
        # Create list [1,2,1,2,1,2,...] of length 100
        arr = [1 if i % 2 == 0 else 2 for i in range(100)]
        head = self.list_to_linked_list(arr)
        result = self.s.removeElements(head, 1)
        expected = [2] * 50
        self.assertEqual(self.linked_list_to_list(result), expected)
    
    def test_long_list_remove_all(self):
        head = self.list_to_linked_list([5] * 100)
        result = self.s.removeElements(head, 5)
        self.assertEqual(self.linked_list_to_list(result), [])

if __name__ == "__main__":
    unittest.main()