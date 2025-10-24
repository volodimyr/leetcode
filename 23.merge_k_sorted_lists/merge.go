// 23. Merge k Sorted Lists
// Topics: 'Linked List', 'Divide and Conquer', 'Heap (Priority Queue)', 'Merge Sort'
// Level: 'Hard'

// You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

// Merge all the linked-lists into one sorted linked-list and return it.

// Example 1:

// Input: lists = [[1,4,5],[1,3,4],[2,6]]
// Output: [1,1,2,3,4,4,5,6]
// Explanation: The linked-lists are:
// [
//   1->4->5,
//   1->3->4,
//   2->6
// ]
// merging them into one sorted linked list:
// 1->1->2->3->4->4->5->6

// Example 2:

// Input: lists = []
// Output: []

// Example 3:

// Input: lists = [[]]
// Output: []

// Constraints:

//     k == lists.length
//     0 <= k <= 104
//     0 <= lists[i].length <= 500
//     -104 <= lists[i][j] <= 104
//     lists[i] is sorted in ascending order.
//     The sum of lists[i].length will not exceed 104.

package mergeksortedlists

func mergeKLists(lists []*ListNode) *ListNode {
	if len(lists) < 1 {
		return nil
	}
	if len(lists) == 1 {
		return lists[0]
	}

	return mergeRange(lists, 0, len(lists)-1)
}

func mergeRange(lists []*ListNode, L, R int) *ListNode {
	if L == R {
		return lists[L]
	}
	mid := (L + R) / 2
	left := mergeRange(lists, L, mid)
	right := mergeRange(lists, mid+1, R)
	return merge(left, right)
}

func merge(list1, list2 *ListNode) *ListNode {
	dummy := &ListNode{}

	cur := dummy
	cur1 := list1
	cur2 := list2
	for cur1 != nil && cur2 != nil {
		if cur1.Val < cur2.Val {
			cur.Next = cur1
			cur1 = cur1.Next
		} else {
			cur.Next = cur2
			cur2 = cur2.Next
		}
		cur = cur.Next
	}

	if cur1 != nil {
		cur.Next = cur1
	} else if cur2 != nil {
		cur.Next = cur2
	}
	return dummy.Next
}

type ListNode struct {
	Next *ListNode
	Val  int
}
