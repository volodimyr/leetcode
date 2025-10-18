package reorderlist

import (
	"testing"
)

func TestReorderList(t *testing.T) {
	tests := []struct {
		name     string
		input    []int
		expected string
	}{
		{
			name:     "example 1 - even length",
			input:    []int{1, 2, 3, 4},
			expected: "1 -> 4 -> 2 -> 3 -> ",
		},
		{
			name:     "example 2 - odd length",
			input:    []int{1, 2, 3, 4, 5},
			expected: "1 -> 5 -> 2 -> 4 -> 3 -> ",
		},
		{
			name:     "single node",
			input:    []int{1},
			expected: "1 -> ",
		},
		{
			name:     "two nodes",
			input:    []int{1, 2},
			expected: "1 -> 2 -> ",
		},
		{
			name:     "three nodes",
			input:    []int{1, 2, 3},
			expected: "1 -> 3 -> 2 -> ",
		},
		{
			name:     "six nodes",
			input:    []int{1, 2, 3, 4, 5, 6},
			expected: "1 -> 6 -> 2 -> 5 -> 3 -> 4 -> ",
		},
		{
			name:     "seven nodes",
			input:    []int{1, 2, 3, 4, 5, 6, 7},
			expected: "1 -> 7 -> 2 -> 6 -> 3 -> 5 -> 4 -> ",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			head := createList(tt.input)
			reorderList(head)
			result := head.String()

			if result != tt.expected {
				t.Errorf("got %q, want %q", result, tt.expected)
			}
		})
	}
}

func TestReorderListNoCycle(t *testing.T) {
	tests := []struct {
		name  string
		input []int
	}{
		{
			name:  "even length no cycle",
			input: []int{1, 2, 3, 4},
		},
		{
			name:  "odd length no cycle",
			input: []int{1, 2, 3, 4, 5},
		},
		{
			name:  "large list no cycle",
			input: []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			head := createList(tt.input)
			reorderList(head)

			if hasCycle(head) {
				t.Errorf("list has a cycle after reordering")
			}
		})
	}
}

func createList(vals []int) *ListNode {
	if len(vals) == 0 {
		return nil
	}

	head := &ListNode{Val: vals[0]}
	curr := head

	for i := 1; i < len(vals); i++ {
		curr.Next = &ListNode{Val: vals[i]}
		curr = curr.Next
	}

	return head
}

func hasCycle(head *ListNode) bool {
	if head == nil {
		return false
	}

	slow := head
	fast := head

	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next

		if slow == fast {
			return true
		}
	}

	return false
}
