package invertbinarytree

import (
	"reflect"
	"testing"
)

// Helper function to perform level-order traversal for comparison
func levelOrder(root *TreeNode) []interface{} {
	if root == nil {
		return []interface{}{}
	}
	result := []interface{}{}
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		if node == nil {
			result = append(result, nil)
		} else {
			result = append(result, node.Val)
			queue = append(queue, node.Left, node.Right)
		}
	}
	// Trim trailing nils
	for len(result) > 0 && result[len(result)-1] == nil {
		result = result[:len(result)-1]
	}
	return result
}

func TestInvertTree(t *testing.T) {
	tests := []struct {
		name string
		root *TreeNode
		want []interface{}
	}{
		{
			name: "Example 1: Full tree",
			root: &TreeNode{
				Val: 4,
				Left: &TreeNode{
					Val:   2,
					Left:  &TreeNode{Val: 1},
					Right: &TreeNode{Val: 3},
				},
				Right: &TreeNode{
					Val:   7,
					Left:  &TreeNode{Val: 6},
					Right: &TreeNode{Val: 9},
				},
			},
			want: []interface{}{4, 7, 2, 9, 6, 3, 1},
		},
		{
			name: "Example 2: Small tree",
			root: &TreeNode{
				Val:   2,
				Left:  &TreeNode{Val: 1},
				Right: &TreeNode{Val: 3},
			},
			want: []interface{}{2, 3, 1},
		},
		{
			name: "Example 3: Empty tree",
			root: nil,
			want: []interface{}{},
		},
		{
			name: "Single node",
			root: &TreeNode{Val: 1},
			want: []interface{}{1},
		},
		{
			name: "Only left child",
			root: &TreeNode{
				Val:  1,
				Left: &TreeNode{Val: 2},
			},
			want: []interface{}{1, nil, 2},
		},
		{
			name: "Only right child",
			root: &TreeNode{
				Val:   1,
				Right: &TreeNode{Val: 2},
			},
			want: []interface{}{1, 2},
		},
		{
			name: "Left-skewed tree",
			root: &TreeNode{
				Val: 3,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val:  1,
						Left: &TreeNode{Val: 0},
					},
				},
			},
			want: []interface{}{3, nil, 2, nil, 1, nil, 0},
		},
		{
			name: "Right-skewed tree",
			root: &TreeNode{
				Val: 1,
				Right: &TreeNode{
					Val: 2,
					Right: &TreeNode{
						Val:   3,
						Right: &TreeNode{Val: 4},
					},
				},
			},
			want: []interface{}{1, 2, nil, 3, nil, 4},
		},
		{
			name: "Unbalanced tree",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:   2,
					Left:  &TreeNode{Val: 3},
					Right: &TreeNode{Val: 4},
				},
				Right: &TreeNode{Val: 5},
			},
			want: []interface{}{1, 5, 2, nil, nil, 4, 3},
		},
		{
			name: "Negative values",
			root: &TreeNode{
				Val:   0,
				Left:  &TreeNode{Val: -50},
				Right: &TreeNode{Val: 50},
			},
			want: []interface{}{0, 50, -50},
		},
		{
			name: "Large tree with multiple levels",
			root: &TreeNode{
				Val: 10,
				Left: &TreeNode{
					Val: 5,
					Left: &TreeNode{
						Val:   2,
						Left:  &TreeNode{Val: 1},
						Right: &TreeNode{Val: 3},
					},
					Right: &TreeNode{
						Val:   7,
						Left:  &TreeNode{Val: 6},
						Right: &TreeNode{Val: 8},
					},
				},
				Right: &TreeNode{
					Val: 15,
					Left: &TreeNode{
						Val:   12,
						Left:  &TreeNode{Val: 11},
						Right: &TreeNode{Val: 13},
					},
					Right: &TreeNode{
						Val:   20,
						Left:  &TreeNode{Val: 18},
						Right: &TreeNode{Val: 25},
					},
				},
			},
			want: []interface{}{10, 15, 5, 20, 12, 7, 2, 25, 18, 13, 11, 8, 6, 3, 1},
		},
		{
			name: "Boundary values",
			root: &TreeNode{
				Val:   0,
				Left:  &TreeNode{Val: -100},
				Right: &TreeNode{Val: 100},
			},
			want: []interface{}{0, 100, -100},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := invertTree(tt.root)
			gotOrder := levelOrder(got)
			if !reflect.DeepEqual(gotOrder, tt.want) {
				t.Errorf("invertTree() = %v, want %v", gotOrder, tt.want)
			}
		})
	}
}

// Additional test to verify original tree structure preservation
func TestInvertTreeTwice(t *testing.T) {
	original := &TreeNode{
		Val: 4,
		Left: &TreeNode{
			Val:   2,
			Left:  &TreeNode{Val: 1},
			Right: &TreeNode{Val: 3},
		},
		Right: &TreeNode{
			Val:   7,
			Left:  &TreeNode{Val: 6},
			Right: &TreeNode{Val: 9},
		},
	}

	originalOrder := levelOrder(original)

	// Invert twice should restore original
	inverted := invertTree(original)
	restored := invertTree(inverted)
	restoredOrder := levelOrder(restored)

	if !reflect.DeepEqual(originalOrder, restoredOrder) {
		t.Errorf("Double inversion failed: original = %v, restored = %v", originalOrder, restoredOrder)
	}
}
