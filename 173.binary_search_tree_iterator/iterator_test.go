package binarysearchtreeiterator

import (
	"testing"
)

func buildTree() *TreeNode {
	// Example BST:
	//        7
	//      /   \
	//     3     15
	//          /  \
	//         9    20
	return &TreeNode{
		Val:  7,
		Left: &TreeNode{Val: 3},
		Right: &TreeNode{
			Val:   15,
			Left:  &TreeNode{Val: 9},
			Right: &TreeNode{Val: 20},
		},
	}
}

func TestBSTIterator_InorderTraversal(t *testing.T) {
	tests := []struct {
		name     string
		root     *TreeNode
		expected []int
	}{
		{
			name:     "basic tree",
			root:     buildTree(),
			expected: []int{3, 7, 9, 15, 20},
		},
		{
			name:     "single node",
			root:     &TreeNode{Val: 42},
			expected: []int{42},
		},
		{
			name:     "empty tree",
			root:     nil,
			expected: []int{},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			it := Constructor(tt.root)
			var result []int

			for it.HasNext() {
				result = append(result, it.Next())
			}

			if len(result) != len(tt.expected) {
				t.Fatalf("expected %v elements, got %v", len(tt.expected), len(result))
			}
			for i := range tt.expected {
				if result[i] != tt.expected[i] {
					t.Errorf("expected inorder[%d] = %v, got %v", i, tt.expected[i], result[i])
				}
			}
		})
	}
}

func TestBSTIterator_HasNextFalseAfterEnd(t *testing.T) {
	root := &TreeNode{Val: 1}
	it := Constructor(root)

	if !it.HasNext() {
		t.Fatalf("expected HasNext() = true before consuming element")
	}

	_ = it.Next()
	it.cursor++

	if it.HasNext() {
		t.Fatalf("expected HasNext() = false after consuming last element")
	}
}
