// 143. Reorder list
// Topics: 'Linked List', 'Stack', 'Recursion', 'Two Pointers'
//

// You are given the head of a singly linked-list. The list can be represented as:

// L0 → L1 → … → Ln - 1 → Ln

// Reorder the list to be on the following form:

// L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

// You may not modify the values in the list's nodes. Only nodes themselves may be changed.

// Example 1:

// Input: head = [1,2,3,4]
// Output: [1,4,2,3]

// Example 2:

// Input: head = [1,2,3,4,5]
// Output: [1,5,2,4,3]

// Constraints:

//     The number of nodes in the list is in the range [1, 5 * 104].
//     1 <= Node.val <= 1000

package reorderlist

import "fmt"

func reorderList(head *ListNode) {
	slow := head
	fast := head
	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next
	}

	secondHalf := slow.Next
	slow.Next = nil
	// reverse secondhalf
	var prev *ListNode
	curr := secondHalf
	for curr != nil {
		next := curr.Next
		curr.Next = prev
		prev = curr
		curr = next
	}
	secondHalf = prev

	merge(head, secondHalf, true)
}

func merge(list1, list2 *ListNode, takeFirst bool) *ListNode {
	if list1 == nil {
		return list2
	}
	if list2 == nil {
		return list1
	}
	if takeFirst {
		list1.Next = merge(list1.Next, list2, false)
		return list1
	} else {
		list2.Next = merge(list1, list2.Next, true)
		return list2
	}
}

func reverse(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	if head.Next == nil {
		return head
	}
	nhead := reverse(head.Next)
	head.Next.Next = head
	head.Next = nil
	return nhead
}

type ListNode struct {
	Next *ListNode
	Val  int
}

func (l *ListNode) String() string {
	var str string
	curr := l
	for curr != nil {
		str += fmt.Sprintf("%d -> ", curr.Val)
		curr = curr.Next
	}

	return str
}
