// 147. Insertion sort list
// Topics: 'Sorting'
// Level: 'Medium', 'Linked List'

// Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

// The steps of the insertion sort algorithm:

//     Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
//     At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
//     It repeats until no input elements remain.

// The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

// Example 1:

// Input: head = [4,2,1,3]
// Output: [1,2,3,4]

// Example 2:

// Input: head = [-1,5,3,4,0]
// Output: [-1,0,3,4,5]

package insertionsortlist

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func (ln *ListNode) String() string {
	var s string
	curr := ln
	for curr != nil {
		if s == "" {
			s = fmt.Sprintf("%d", curr.Val)
		} else {
			s += fmt.Sprintf("->%d", curr.Val)
		}
		curr = curr.Next
	}
	return s
}

// space is O(n), time is O(n^2)
// space should be optimised and use O(1) (in-place sorting)
// therefore no new node creation
func insertionSortListSpaceN(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	dummy := &ListNode{Next: &ListNode{Val: head.Val}}

	for curr := head.Next; curr != nil; curr = curr.Next {
		j := dummy.Next
		var prev *ListNode
		for j != nil && j.Val < curr.Val {
			prev = j
			j = j.Next
		}
		newNode := &ListNode{Val: curr.Val, Next: j}
		if prev == nil {
			dummy.Next = newNode
		} else {
			prev.Next = newNode
		}
	}
	return dummy.Next
}

func insertionSortList(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	dummy := &ListNode{Next: head}
	curr := head.Next
	head.Next = nil
	for curr != nil {
		next := curr.Next
		prev := dummy
		for prev.Next != nil && prev.Next.Val < curr.Val {
			prev = prev.Next
		}
		curr.Next, prev.Next = prev.Next, curr
		curr = next

	}
	return dummy.Next
}
