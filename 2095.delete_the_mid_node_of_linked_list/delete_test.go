package deletethemidnodeoflinkedlist

import (
	"testing"
)

func TestDeleteMiddle(t *testing.T) {
	tests := []struct {
		name     string
		input    []int
		expected []int
	}{
		{
			name:     "seven nodes",
			input:    []int{1, 3, 4, 7, 1, 2, 6},
			expected: []int{1, 3, 4, 1, 2, 6},
		},
		{
			name:     "four nodes",
			input:    []int{1, 2, 3, 4},
			expected: []int{1, 2, 4},
		},
		{
			name:     "two nodes",
			input:    []int{2, 1},
			expected: []int{2},
		},
		{
			name:     "single node",
			input:    []int{1},
			expected: []int{},
		},
		{
			name:     "three nodes",
			input:    []int{1, 2, 3},
			expected: []int{1, 3},
		},
		{
			name:     "five nodes",
			input:    []int{1, 2, 3, 4, 5},
			expected: []int{1, 2, 4, 5},
		},
		{
			name:     "six nodes",
			input:    []int{1, 2, 3, 4, 5, 6},
			expected: []int{1, 2, 3, 5, 6},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			head := buildList(tt.input)
			result := deleteMiddle(head)
			actual := listToSlice(result)

			if !equal(actual, tt.expected) {
				t.Errorf("got %v, want %v", actual, tt.expected)
			}
		})
	}
}

func buildList(vals []int) *ListNode {
	if len(vals) == 0 {
		return nil
	}
	head := &ListNode{Val: vals[0]}
	current := head
	for i := 1; i < len(vals); i++ {
		current.Next = &ListNode{Val: vals[i]}
		current = current.Next
	}
	return head
}

func listToSlice(head *ListNode) []int {
	result := []int{}
	for head != nil {
		result = append(result, head.Val)
		head = head.Next
	}
	return result
}

func equal(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}
