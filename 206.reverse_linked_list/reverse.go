// 206. Reverse Linked List
// Topics: 'Linked List', 'Recusrsion'

//Given the head of a singly linked list, reverse the list, and return the reversed list.

// Example 1:

// Input: head = [1,2,3,4,5]
// Output: [5,4,3,2,1]

// Example 2:

// Input: head = [1,2]
// Output: [2,1]

// Example 3:

// Input: head = []
// Output: []

// Constraints:

//     The number of nodes in the list is the range [0, 5000].
//     -5000 <= Node.val <= 5000

// Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

package reverselinkedlist

type ListNode struct {
	Val  int
	Next *ListNode
}

func (l *ListNode) GetValues() []int {
	var arr []int
	curr := l
	for curr != nil {
		arr = append(arr, curr.Val)
		curr = curr.Next
	}
	return arr
}

func reverseList(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	if head.Next == nil {
		return head
	}
	nHead := reverseList(head.Next)
	head.Next.Next = head
	head.Next = nil

	return nHead
}
