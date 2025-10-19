// 2. Add two numbers
// Topics: 'Math', 'Recursion', 'Linked List'
// Level: 'Medium'

// You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

// Example 1:

// Input: l1 = [2,4,3], l2 = [5,6,4]
// Output: [7,0,8]
// Explanation: 342 + 465 = 807.

// Example 2:

// Input: l1 = [0], l2 = [0]
// Output: [0]

// Example 3:

// Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
// Output: [8,9,9,9,0,0,0,1]

// Constraints:

//     The number of nodes in each linked list is in the range [1, 100].
//     0 <= Node.val <= 9
//     It is guaranteed that the list represents a number that does not have leading zeros.

package addtwonumbers

// memory O(n) extra
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	dummy := &ListNode{}
	current := dummy
	carry := 0

	for l1 != nil || l2 != nil || carry > 0 {
		sum := carry
		if l1 != nil {
			sum += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			sum += l2.Val
			l2 = l2.Next
		}
		carry = sum / 10
		current.Next = &ListNode{Val: sum % 10}
		current = current.Next
	}

	return dummy.Next
}

// memory O(1) extra
// func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
// 	cur1 := l1
// 	prev := cur1
// 	cur2 := l2
// 	var carry int
// 	for {
// 		sum := carry
// 		if cur1 == nil && cur2 == nil {
// 			if carry != 0 {
// 				prev.Next = &ListNode{Val: carry}
// 			}
// 			break
// 		}
// 		if cur1 != nil {
// 			sum += cur1.Val
// 		}
// 		if cur2 != nil {
// 			sum += cur2.Val
// 		}

// 		if cur1 != nil {
// 			cur1.Val = sum % 10
// 		} else {
// 			cur2.Val = sum % 10
// 			prev.Next = cur2
// 			prev = prev.Next
// 		}

// 		if cur1 != nil {
// 			prev = cur1
// 			cur1 = cur1.Next
// 		}
// 		if cur2 != nil {
// 			cur2 = cur2.Next
// 		}
// 		carry = sum / 10
// 	}

// 	return l1
// }

type ListNode struct {
	Val  int
	Next *ListNode
}
