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
