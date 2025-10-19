package linkedlistcycleii

import "testing"

func TestDetectCycle(t *testing.T) {
	tests := []struct {
		name     string
		values   []int
		pos      int
		expected int // index of cycle start, -1 if no cycle
	}{
		{
			name:     "cycle at index 1",
			values:   []int{3, 2, 0, -4},
			pos:      1,
			expected: 1,
		},
		{
			name:     "cycle at index 0",
			values:   []int{1, 2},
			pos:      0,
			expected: 0,
		},
		{
			name:     "no cycle",
			values:   []int{1},
			pos:      -1,
			expected: -1,
		},
		{
			name:     "empty list",
			values:   []int{},
			pos:      -1,
			expected: -1,
		},
		{
			name:     "single node with cycle",
			values:   []int{1},
			pos:      0,
			expected: 0,
		},
		{
			name:     "two nodes no cycle",
			values:   []int{1, 2},
			pos:      -1,
			expected: -1,
		},
		{
			name:     "cycle in middle",
			values:   []int{1, 2, 3, 4, 5},
			pos:      2,
			expected: 2,
		},
		{
			name:     "cycle at end",
			values:   []int{1, 2, 3, 4, 5},
			pos:      4,
			expected: 4,
		},
		{
			name:     "large list with cycle",
			values:   []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
			pos:      5,
			expected: 5,
		},
		{
			name:     "large list no cycle",
			values:   []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
			pos:      -1,
			expected: -1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			head, cycleNode := createLinkedListWithCycle(tt.values, tt.pos)
			result := detectCycle(head)

			if tt.expected == -1 {
				if result != nil {
					t.Errorf("expected no cycle (nil), got node with value %d", result.Val)
				}
			} else {
				if result == nil {
					t.Errorf("expected cycle at index %d, got nil", tt.expected)
				} else if result != cycleNode {
					t.Errorf("expected cycle node at index %d, got different node", tt.expected)
				}
			}
		})
	}
}

func TestDetectCycleNilHead(t *testing.T) {
	result := detectCycle(nil)
	if result != nil {
		t.Errorf("expected nil for nil head, got %v", result)
	}
}

func TestDetectCycleEdgeCases(t *testing.T) {
	t.Run("negative values with cycle", func(t *testing.T) {
		head, cycleNode := createLinkedListWithCycle([]int{-1, -2, -3, -4}, 2)
		result := detectCycle(head)
		if result != cycleNode {
			t.Errorf("expected cycle at index 2, got different result")
		}
	})

	t.Run("duplicate values with cycle", func(t *testing.T) {
		head, cycleNode := createLinkedListWithCycle([]int{1, 1, 1, 1}, 1)
		result := detectCycle(head)
		if result != cycleNode {
			t.Errorf("expected cycle at index 1, got different result")
		}
	})

	t.Run("very long cycle", func(t *testing.T) {
		values := make([]int, 1000)
		for i := range values {
			values[i] = i
		}
		head, cycleNode := createLinkedListWithCycle(values, 100)
		result := detectCycle(head)
		if result != cycleNode {
			t.Errorf("expected cycle at index 100, got different result")
		}
	})
}

// Helper function to create a linked list with a cycle
func createLinkedListWithCycle(values []int, pos int) (*ListNode, *ListNode) {
	if len(values) == 0 {
		return nil, nil
	}

	head := &ListNode{Val: values[0]}
	current := head
	var cycleNode *ListNode

	// Create nodes
	nodes := []*ListNode{head}
	for i := 1; i < len(values); i++ {
		newNode := &ListNode{Val: values[i]}
		current.Next = newNode
		current = newNode
		nodes = append(nodes, newNode)
	}

	// Create cycle if pos is valid
	if pos >= 0 && pos < len(nodes) {
		cycleNode = nodes[pos]
		current.Next = cycleNode
	}

	return head, cycleNode
}
