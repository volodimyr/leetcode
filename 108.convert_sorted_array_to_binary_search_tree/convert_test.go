package convertsortedarraytobinarysearchtree

import (
	"testing"
)

func TestSortedArrayToBST(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want func(*TreeNode) bool
	}{
		{
			name: "example 1",
			nums: []int{-10, -3, 0, 5, 9},
			want: func(root *TreeNode) bool {
				if root == nil {
					return false
				}
				return isValidBST(root, nil, nil) && isBalanced(root)
			},
		},
		{
			name: "example 2",
			nums: []int{1, 3},
			want: func(root *TreeNode) bool {
				if root == nil {
					return false
				}
				return isValidBST(root, nil, nil) && isBalanced(root)
			},
		},
		{
			name: "single element",
			nums: []int{1},
			want: func(root *TreeNode) bool {
				return root != nil && root.Val == 1 && root.Left == nil && root.Right == nil
			},
		},
		{
			name: "three elements",
			nums: []int{1, 2, 3},
			want: func(root *TreeNode) bool {
				if root == nil {
					return false
				}
				return isValidBST(root, nil, nil) && isBalanced(root)
			},
		},
		{
			name: "negative numbers",
			nums: []int{-5, -3, -1, 0, 1, 3, 5},
			want: func(root *TreeNode) bool {
				if root == nil {
					return false
				}
				return isValidBST(root, nil, nil) && isBalanced(root)
			},
		},
		{
			name: "two elements",
			nums: []int{1, 2},
			want: func(root *TreeNode) bool {
				if root == nil {
					return false
				}
				return isValidBST(root, nil, nil) && isBalanced(root)
			},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := sortedArrayToBST(tt.nums)
			if !tt.want(got) {
				t.Errorf("sortedArrayToBST() failed validation")
			}
		})
	}
}

func isValidBST(node *TreeNode, min, max *int) bool {
	if node == nil {
		return true
	}
	if min != nil && node.Val <= *min {
		return false
	}
	if max != nil && node.Val >= *max {
		return false
	}
	return isValidBST(node.Left, min, &node.Val) && isValidBST(node.Right, &node.Val, max)
}

func isBalanced(node *TreeNode) bool {
	_, balanced := checkHeight(node)
	return balanced
}

func checkHeight(node *TreeNode) (int, bool) {
	if node == nil {
		return 0, true
	}
	leftHeight, leftBalanced := checkHeight(node.Left)
	if !leftBalanced {
		return 0, false
	}
	rightHeight, rightBalanced := checkHeight(node.Right)
	if !rightBalanced {
		return 0, false
	}
	diff := leftHeight - rightHeight
	if diff < 0 {
		diff = -diff
	}
	if diff > 1 {
		return 0, false
	}
	maxHeight := leftHeight
	if rightHeight > maxHeight {
		maxHeight = rightHeight
	}
	return maxHeight + 1, true
}
