// 25. Reverse Nodes in k-Group
// Topics: 'Linked List', 'Recursion'
// Level: 'Hard'

// Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

// k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

// You may not alter the values in the list's nodes, only nodes themselves may be changed.

// Example 1:

// Input: head = [1,2,3,4,5], k = 2
// Output: [2,1,4,3,5]

// Example 2:

// Input: head = [1,2,3,4,5], k = 3
// Output: [3,2,1,4,5]

// Constraints:

//     The number of nodes in the list is n.
//     1 <= k <= n <= 5000
//     0 <= Node.val <= 1000

// Follow-up: Can you solve the problem in O(1) extra memory space?

package reversenodeinkgroup

type ListNode struct {
	Next *ListNode
	Val  int
}

func reverseKGroup(head *ListNode, k int) *ListNode {
	dummy := &ListNode{}
	cur := head
	dcur := dummy
	for cur != nil {
		dcur.Next, dcur, cur = reverse(cur, k)
	}
	return dummy.Next
}

func reverse(head *ListNode, k int) (*ListNode, *ListNode, *ListNode) {
	check := head
	i := k
	for check != nil && i > 1 {
		check = check.Next
		i--
	}
	if check == nil {
		return head, nil, nil
	}
	var prev *ListNode
	cur := head
	for k > 0 && cur != nil {
		next := cur.Next
		cur.Next = prev
		prev = cur
		cur = next
		k--
	}
	return prev, head, cur
}
