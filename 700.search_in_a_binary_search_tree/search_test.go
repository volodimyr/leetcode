package searchinabinarysearchtree

import (
	"reflect"
	"testing"
)

// helper to build a tree
func makeTree(val int, left, right *TreeNode) *TreeNode {
	return &TreeNode{Val: val, Left: left, Right: right}
}

func TestSearchBST(t *testing.T) {
	/*
	      4
	     / \
	    2   7
	   / \
	  1   3
	*/
	root := makeTree(4,
		makeTree(2,
			makeTree(1, nil, nil),
			makeTree(3, nil, nil),
		),
		makeTree(7, nil, nil),
	)

	tests := []struct {
		name     string
		root     *TreeNode
		val      int
		expected *TreeNode
	}{
		{
			name:     "finds existing value in left subtree",
			root:     root,
			val:      2,
			expected: makeTree(2, makeTree(1, nil, nil), makeTree(3, nil, nil)),
		},
		{
			name:     "finds existing value in right subtree",
			root:     root,
			val:      7,
			expected: makeTree(7, nil, nil),
		},
		{
			name:     "finds root value",
			root:     root,
			val:      4,
			expected: root, // can directly compare pointers
		},
		{
			name:     "returns nil if value does not exist",
			root:     root,
			val:      5,
			expected: nil,
		},
		{
			name:     "handles nil root",
			root:     nil,
			val:      1,
			expected: nil,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := searchBST(tt.root, tt.val)
			if tt.expected == nil && got != nil {
				t.Errorf("expected nil, got %+v", got)
			}
			if tt.expected != nil && got == nil {
				t.Errorf("expected non-nil, got nil")
			}
			if tt.expected != nil && got != nil {
				if got.Val != tt.expected.Val {
					t.Errorf("expected value %d, got %d", tt.expected.Val, got.Val)
				}
				// For non-root test cases, compare structure equality too
				if !reflect.DeepEqual(got, tt.expected) && tt.val != 4 {
					t.Errorf("expected subtree %+v, got %+v", tt.expected, got)
				}
			}
		})
	}
}
