package insertintoabinarysearchtree

import (
	"testing"
)

func TestInsertIntoBST(t *testing.T) {
	tests := []struct {
		name     string
		root     *TreeNode
		val      int
		validate func(*TreeNode) bool
	}{
		{
			name: "insert into empty tree",
			root: nil,
			val:  5,
			validate: func(root *TreeNode) bool {
				return root != nil && root.Val == 5 && root.Left == nil && root.Right == nil
			},
		},
		{
			name: "insert into single node tree - left",
			root: &TreeNode{Val: 10},
			val:  5,
			validate: func(root *TreeNode) bool {
				return root.Val == 10 && root.Left != nil && root.Left.Val == 5
			},
		},
		{
			name: "insert into single node tree - right",
			root: &TreeNode{Val: 10},
			val:  15,
			validate: func(root *TreeNode) bool {
				return root.Val == 10 && root.Right != nil && root.Right.Val == 15
			},
		},
		{
			name: "example 1 - insert 5 into [4,2,7,1,3]",
			root: &TreeNode{
				Val: 4,
				Left: &TreeNode{
					Val:   2,
					Left:  &TreeNode{Val: 1},
					Right: &TreeNode{Val: 3},
				},
				Right: &TreeNode{Val: 7},
			},
			val: 5,
			validate: func(root *TreeNode) bool {
				return isBST(root, nil, nil) && contains(root, 5)
			},
		},
		{
			name: "example 2 - insert 25 into [40,20,60,10,30,50,70]",
			root: &TreeNode{
				Val: 40,
				Left: &TreeNode{
					Val:   20,
					Left:  &TreeNode{Val: 10},
					Right: &TreeNode{Val: 30},
				},
				Right: &TreeNode{
					Val:   60,
					Left:  &TreeNode{Val: 50},
					Right: &TreeNode{Val: 70},
				},
			},
			val: 25,
			validate: func(root *TreeNode) bool {
				return isBST(root, nil, nil) && contains(root, 25)
			},
		},
		{
			name: "insert minimum value",
			root: &TreeNode{
				Val:   50,
				Left:  &TreeNode{Val: 30},
				Right: &TreeNode{Val: 70},
			},
			val: 10,
			validate: func(root *TreeNode) bool {
				return isBST(root, nil, nil) && contains(root, 10)
			},
		},
		{
			name: "insert maximum value",
			root: &TreeNode{
				Val:   50,
				Left:  &TreeNode{Val: 30},
				Right: &TreeNode{Val: 70},
			},
			val: 100,
			validate: func(root *TreeNode) bool {
				return isBST(root, nil, nil) && contains(root, 100)
			},
		},
		{
			name: "insert into left-skewed tree",
			root: &TreeNode{
				Val: 10,
				Left: &TreeNode{
					Val: 5,
					Left: &TreeNode{
						Val: 2,
					},
				},
			},
			val: 3,
			validate: func(root *TreeNode) bool {
				return isBST(root, nil, nil) && contains(root, 3)
			},
		},
		{
			name: "insert into right-skewed tree",
			root: &TreeNode{
				Val: 10,
				Right: &TreeNode{
					Val: 20,
					Right: &TreeNode{
						Val: 30,
					},
				},
			},
			val: 25,
			validate: func(root *TreeNode) bool {
				return isBST(root, nil, nil) && contains(root, 25)
			},
		},
		{
			name: "insert negative value",
			root: &TreeNode{
				Val:   0,
				Left:  &TreeNode{Val: -5},
				Right: &TreeNode{Val: 5},
			},
			val: -3,
			validate: func(root *TreeNode) bool {
				return isBST(root, nil, nil) && contains(root, -3)
			},
		},
		{
			name: "insert large value",
			root: &TreeNode{Val: 0},
			val:  100000000,
			validate: func(root *TreeNode) bool {
				return isBST(root, nil, nil) && contains(root, 100000000)
			},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := insertIntoBST(tt.root, tt.val)

			if result == nil {
				t.Fatal("insertIntoBST returned nil")
			}

			if !tt.validate(result) {
				t.Errorf("validation failed for test case: %s", tt.name)
			}
		})
	}
}

// Helper function to check if a tree is a valid BST
func isBST(node *TreeNode, min, max *int) bool {
	if node == nil {
		return true
	}

	if min != nil && node.Val <= *min {
		return false
	}
	if max != nil && node.Val >= *max {
		return false
	}

	return isBST(node.Left, min, &node.Val) && isBST(node.Right, &node.Val, max)
}

// Helper function to check if a value exists in the tree
func contains(node *TreeNode, val int) bool {
	if node == nil {
		return false
	}
	if node.Val == val {
		return true
	}
	if val < node.Val {
		return contains(node.Left, val)
	}
	return contains(node.Right, val)
}

// Helper function to count nodes in the tree
func countNodes(node *TreeNode) int {
	if node == nil {
		return 0
	}
	return 1 + countNodes(node.Left) + countNodes(node.Right)
}

func TestInsertIntoBST_NodeCount(t *testing.T) {
	root := &TreeNode{
		Val: 4,
		Left: &TreeNode{
			Val:   2,
			Left:  &TreeNode{Val: 1},
			Right: &TreeNode{Val: 3},
		},
		Right: &TreeNode{Val: 7},
	}

	originalCount := countNodes(root)
	result := insertIntoBST(root, 5)
	newCount := countNodes(result)

	if newCount != originalCount+1 {
		t.Errorf("expected node count to increase by 1, got original: %d, new: %d", originalCount, newCount)
	}
}

func TestInsertIntoBST_PreservesOriginalNodes(t *testing.T) {
	root := &TreeNode{
		Val:   10,
		Left:  &TreeNode{Val: 5},
		Right: &TreeNode{Val: 15},
	}

	result := insertIntoBST(root, 7)

	// Check that original values are still present
	if !contains(result, 10) || !contains(result, 5) || !contains(result, 15) {
		t.Error("original nodes were not preserved after insertion")
	}

	// Check that new value was added
	if !contains(result, 7) {
		t.Error("new value was not inserted")
	}
}
