package linkedlistcycle

import "testing"

func TestHasCycle_NilHead(t *testing.T) {
	if hasCycle(nil) {
		t.Error("Expected false for nil head, got true")
	}
}

func TestHasCycle_SingleNodeNoCycle(t *testing.T) {
	head := &ListNode{Val: 1}
	if hasCycle(head) {
		t.Error("Expected false for single node without cycle, got true")
	}
}

func TestHasCycle_TwoNodesNoCycle(t *testing.T) {
	head := &ListNode{Val: 1}
	head.Next = &ListNode{Val: 2}
	if hasCycle(head) {
		t.Error("Expected false for two nodes without cycle, got true")
	}
}

func TestHasCycle_SingleNodeWithCycle(t *testing.T) {
	head := &ListNode{Val: 1}
	head.Next = head
	if !hasCycle(head) {
		t.Error("Expected true for single node with cycle, got false")
	}
}

func TestHasCycle_TwoNodesWithCycle(t *testing.T) {
	head := &ListNode{Val: 1}
	second := &ListNode{Val: 2}
	head.Next = second
	second.Next = head
	if !hasCycle(head) {
		t.Error("Expected true for two nodes with cycle at position 0, got false")
	}
}

func TestHasCycle_Example1(t *testing.T) {
	head := &ListNode{Val: 3}
	second := &ListNode{Val: 2}
	third := &ListNode{Val: 0}
	fourth := &ListNode{Val: -4}

	head.Next = second
	second.Next = third
	third.Next = fourth
	fourth.Next = second

	if !hasCycle(head) {
		t.Error("Expected true for cycle at position 1, got false")
	}
}

func TestHasCycle_Example2(t *testing.T) {
	head := &ListNode{Val: 1}
	second := &ListNode{Val: 2}
	head.Next = second
	second.Next = head

	if !hasCycle(head) {
		t.Error("Expected true for cycle at position 0, got false")
	}
}

func TestHasCycle_Example3(t *testing.T) {
	head := &ListNode{Val: 1}

	if hasCycle(head) {
		t.Error("Expected false for single node without cycle, got true")
	}
}

func TestHasCycle_LongListNoCycle(t *testing.T) {
	head := &ListNode{Val: 1}
	current := head
	for i := 2; i <= 10; i++ {
		current.Next = &ListNode{Val: i}
		current = current.Next
	}

	if hasCycle(head) {
		t.Error("Expected false for long list without cycle, got true")
	}
}

func TestHasCycle_LongListWithCycleAtEnd(t *testing.T) {
	head := &ListNode{Val: 1}
	current := head
	nodes := []*ListNode{head}

	for i := 2; i <= 10; i++ {
		current.Next = &ListNode{Val: i}
		current = current.Next
		nodes = append(nodes, current)
	}
	current.Next = nodes[len(nodes)-3]

	if !hasCycle(head) {
		t.Error("Expected true for long list with cycle at end, got false")
	}
}

func TestHasCycle_LongListWithCycleAtMiddle(t *testing.T) {
	head := &ListNode{Val: 1}
	current := head
	nodes := []*ListNode{head}

	for i := 2; i <= 10; i++ {
		current.Next = &ListNode{Val: i}
		current = current.Next
		nodes = append(nodes, current)
	}
	current.Next = nodes[4]

	if !hasCycle(head) {
		t.Error("Expected true for long list with cycle at middle, got false")
	}
}

func TestHasCycle_ThreeNodesNoCycle(t *testing.T) {
	head := &ListNode{Val: 1}
	head.Next = &ListNode{Val: 2}
	head.Next.Next = &ListNode{Val: 3}

	if hasCycle(head) {
		t.Error("Expected false for three nodes without cycle, got true")
	}
}

func TestHasCycle_ThreeNodesWithCycle(t *testing.T) {
	head := &ListNode{Val: 1}
	second := &ListNode{Val: 2}
	third := &ListNode{Val: 3}

	head.Next = second
	second.Next = third
	third.Next = second

	if !hasCycle(head) {
		t.Error("Expected true for three nodes with cycle, got false")
	}
}

func TestHasCycle_NegativeValues(t *testing.T) {
	head := &ListNode{Val: -105}
	second := &ListNode{Val: -50}
	third := &ListNode{Val: 0}
	fourth := &ListNode{Val: 105}

	head.Next = second
	second.Next = third
	third.Next = fourth
	fourth.Next = second

	if !hasCycle(head) {
		t.Error("Expected true for list with negative values and cycle, got false")
	}
}
