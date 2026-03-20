from typing import Optional
from merge import ListNode, Solution

class TestMergeNodes:
    # Helper function to create a linked list from a list of values
    def list_to_linkedlist(self, values: list) -> Optional[ListNode]:
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Helper function to convert a linked list to a list of values
    def linkedlist_to_list(self, head: Optional[ListNode]) -> list:
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values

    def test_example_1(self):
        """
        Input: head = [0,3,1,0,4,5,2,0]
        Output: [4,11]
        Explanation: (3+1) = 4, (4+5+2) = 11.
        """
        sol = Solution()
        input_list = [0, 3, 1, 0, 4, 5, 2, 0]
        head = self.list_to_linkedlist(input_list)
        
        result_head = sol.mergeNodes(head)
        result_list = self.linkedlist_to_list(result_head)
        
        assert result_list == [4, 11]

    def test_example_2(self):
        """
        Input: head = [0,1,0,3,0,2,2,0]
        Output: [1,3,4]
        Explanation: (1) = 1, (3) = 3, (2+2) = 4.
        """
        sol = Solution()
        input_list = [0, 1, 0, 3, 0, 2, 2, 0]
        head = self.list_to_linkedlist(input_list)
        
        result_head = sol.mergeNodes(head)
        result_list = self.linkedlist_to_list(result_head)
        
        assert result_list == [1, 3, 4]

    def test_single_element_group(self):
        """
        Input: head = [0,5,0]
        Output: [5]
        Explanation: (5) = 5.
        """
        sol = Solution()
        input_list = [0, 5, 0]
        head = self.list_to_linkedlist(input_list)
        
        result_head = sol.mergeNodes(head)
        result_list = self.linkedlist_to_list(result_head)
        
        assert result_list == [5]

    def test_multiple_groups(self):
        """
        Input: head = [0,2,3,0,1,1,0,5,0]
        Output: [5,2,5]
        Explanation: (2+3) = 5, (1+1) = 2, (5) = 5.
        """
        sol = Solution()
        input_list = [0, 2, 3, 0, 1, 1, 0, 5, 0]
        head = self.list_to_linkedlist(input_list)
        
        result_head = sol.mergeNodes(head)
        result_list = self.linkedlist_to_list(result_head)
        
        assert result_list == [5, 2, 5]

# Run the tests (in a real environment, you'd use a testing framework like unittest or pytest)
# For demonstration purposes, we'll manually instantiate and run them.
if __name__ == '__main__':
    tester = TestMergeNodes()
    try:
        tester.test_example_1()
        print("Test 1 Passed: Example 1")
        tester.test_example_2()
        print("Test 2 Passed: Example 2")
        tester.test_single_element_group()
        print("Test 3 Passed: Single Group")
        tester.test_multiple_groups()
        print("Test 4 Passed: Multiple Groups")
        print("\nAll tests passed successfully! [OK]")
    except AssertionError as e:
        print(f"\nTest Failed: {e}")