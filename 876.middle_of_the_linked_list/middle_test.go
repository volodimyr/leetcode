package middleofthelinkedlist

import "testing"

func TestMiddleNode_SingleNode(t *testing.T) {
	head := &ListNode{Val: 1}
	result := middleNode(head)

	if result != head {
		t.Error("Expected single node to be returned as middle")
	}
	if result.Val != 1 {
		t.Errorf("Expected value 1, got %d", result.Val)
	}
}

func TestMiddleNode_TwoNodes(t *testing.T) {
	head := &ListNode{Val: 1}
	second := &ListNode{Val: 2}
	head.Next = second

	result := middleNode(head)

	if result != second {
		t.Error("Expected second node to be returned as middle")
	}
	if result.Val != 2 {
		t.Errorf("Expected value 2, got %d", result.Val)
	}
}

func TestMiddleNode_ThreeNodes(t *testing.T) {
	head := &ListNode{Val: 1}
	head.Next = &ListNode{Val: 2}
	head.Next.Next = &ListNode{Val: 3}

	result := middleNode(head)

	if result.Val != 2 {
		t.Errorf("Expected middle value 2, got %d", result.Val)
	}
}

func TestMiddleNode_FourNodes(t *testing.T) {
	head := &ListNode{Val: 1}
	head.Next = &ListNode{Val: 2}
	head.Next.Next = &ListNode{Val: 3}
	head.Next.Next.Next = &ListNode{Val: 4}

	result := middleNode(head)

	if result.Val != 3 {
		t.Errorf("Expected second middle value 3, got %d", result.Val)
	}
}

func TestMiddleNode_Example1(t *testing.T) {
	head := &ListNode{Val: 1}
	head.Next = &ListNode{Val: 2}
	head.Next.Next = &ListNode{Val: 3}
	head.Next.Next.Next = &ListNode{Val: 4}
	head.Next.Next.Next.Next = &ListNode{Val: 5}

	result := middleNode(head)

	if result.Val != 3 {
		t.Errorf("Expected middle value 3, got %d", result.Val)
	}

	values := []int{}
	for curr := result; curr != nil; curr = curr.Next {
		values = append(values, curr.Val)
	}
	expected := []int{3, 4, 5}
	if len(values) != len(expected) {
		t.Errorf("Expected remaining list length %d, got %d", len(expected), len(values))
	}
	for i := range expected {
		if values[i] != expected[i] {
			t.Errorf("At position %d: expected %d, got %d", i, expected[i], values[i])
		}
	}
}

func TestMiddleNode_Example2(t *testing.T) {
	head := &ListNode{Val: 1}
	head.Next = &ListNode{Val: 2}
	head.Next.Next = &ListNode{Val: 3}
	head.Next.Next.Next = &ListNode{Val: 4}
	head.Next.Next.Next.Next = &ListNode{Val: 5}
	head.Next.Next.Next.Next.Next = &ListNode{Val: 6}

	result := middleNode(head)

	if result.Val != 4 {
		t.Errorf("Expected second middle value 4, got %d", result.Val)
	}

	values := []int{}
	for curr := result; curr != nil; curr = curr.Next {
		values = append(values, curr.Val)
	}
	expected := []int{4, 5, 6}
	if len(values) != len(expected) {
		t.Errorf("Expected remaining list length %d, got %d", len(expected), len(values))
	}
	for i := range expected {
		if values[i] != expected[i] {
			t.Errorf("At position %d: expected %d, got %d", i, expected[i], values[i])
		}
	}
}

func TestMiddleNode_SevenNodes(t *testing.T) {
	head := &ListNode{Val: 1}
	curr := head
	for i := 2; i <= 7; i++ {
		curr.Next = &ListNode{Val: i}
		curr = curr.Next
	}

	result := middleNode(head)

	if result.Val != 4 {
		t.Errorf("Expected middle value 4, got %d", result.Val)
	}
}

func TestMiddleNode_EightNodes(t *testing.T) {
	head := &ListNode{Val: 1}
	curr := head
	for i := 2; i <= 8; i++ {
		curr.Next = &ListNode{Val: i}
		curr = curr.Next
	}

	result := middleNode(head)

	if result.Val != 5 {
		t.Errorf("Expected second middle value 5, got %d", result.Val)
	}
}

func TestMiddleNode_MaxConstraint(t *testing.T) {
	head := &ListNode{Val: 100}
	curr := head
	for i := 99; i >= 1; i-- {
		curr.Next = &ListNode{Val: i}
		curr = curr.Next
	}

	result := middleNode(head)

	if result == nil {
		t.Error("Expected non-nil result for 100 nodes")
	}
}

func TestMiddleNode_TenNodes(t *testing.T) {
	head := &ListNode{Val: 10}
	curr := head
	for i := 20; i <= 100; i += 10 {
		curr.Next = &ListNode{Val: i}
		curr = curr.Next
	}

	result := middleNode(head)

	if result.Val != 60 {
		t.Errorf("Expected second middle value 60, got %d", result.Val)
	}
}

func TestMiddleNode_NineNodes(t *testing.T) {
	head := &ListNode{Val: 1}
	curr := head
	for i := 2; i <= 9; i++ {
		curr.Next = &ListNode{Val: i * 10}
		curr = curr.Next
	}

	result := middleNode(head)

	if result.Val != 50 {
		t.Errorf("Expected middle value 50, got %d", result.Val)
	}
}
