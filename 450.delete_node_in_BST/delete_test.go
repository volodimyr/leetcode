package deletenodeinbst

import (
	"testing"
)

func TestDeleteNode(t *testing.T) {
	tests := []struct {
		name     string
		root     *TreeNode
		key      int
		expected []int // inorder traversal of expected result
	}{
		{
			name:     "delete node with two children",
			root:     buildTree([]interface{}{5, 3, 6, 2, 4, nil, 7}),
			key:      3,
			expected: []int{2, 4, 5, 6, 7}, // one valid result
		},
		{
			name:     "delete node that doesn't exist",
			root:     buildTree([]interface{}{5, 3, 6, 2, 4, nil, 7}),
			key:      0,
			expected: []int{2, 3, 4, 5, 6, 7},
		},
		{
			name:     "empty tree",
			root:     nil,
			key:      0,
			expected: []int{},
		},
		{
			name:     "delete root with no children",
			root:     buildTree([]interface{}{5}),
			key:      5,
			expected: []int{},
		},
		{
			name:     "delete root with only left child",
			root:     buildTree([]interface{}{5, 3, nil}),
			key:      5,
			expected: []int{3},
		},
		{
			name:     "delete root with only right child",
			root:     buildTree([]interface{}{5, nil, 6}),
			key:      5,
			expected: []int{6},
		},
		{
			name:     "delete root with two children",
			root:     buildTree([]interface{}{5, 3, 6, 2, 4, nil, 7}),
			key:      5,
			expected: []int{2, 3, 4, 6, 7},
		},
		{
			name:     "delete leaf node",
			root:     buildTree([]interface{}{5, 3, 6, 2, 4, nil, 7}),
			key:      2,
			expected: []int{3, 4, 5, 6, 7},
		},
		{
			name:     "delete node with only right child",
			root:     buildTree([]interface{}{5, 3, 6, nil, 4, nil, 7}),
			key:      3,
			expected: []int{4, 5, 6, 7},
		},
		{
			name:     "delete node with only left child",
			root:     buildTree([]interface{}{5, 3, 6, 2, nil, nil, 7}),
			key:      3,
			expected: []int{2, 5, 6, 7},
		},
		{
			name:     "single node tree, delete existing",
			root:     buildTree([]interface{}{1}),
			key:      1,
			expected: []int{},
		},
		{
			name:     "delete from larger tree",
			root:     buildTree([]interface{}{8, 5, 12, 4, 7, 10, 14, nil, nil, 6, nil, 9, 11}),
			key:      5,
			expected: []int{4, 6, 7, 8, 9, 10, 11, 12, 14},
		},
		{
			name:     "negative values",
			root:     buildTree([]interface{}{0, -5, 5, -10, -3, 3, 10}),
			key:      -5,
			expected: []int{-10, -3, 0, 3, 5, 10},
		},
		{
			name:     "delete rightmost node",
			root:     buildTree([]interface{}{5, 3, 6, 2, 4, nil, 7}),
			key:      7,
			expected: []int{2, 3, 4, 5, 6},
		},
		{
			name:     "delete leftmost node",
			root:     buildTree([]interface{}{5, 3, 6, 2, 4, nil, 7}),
			key:      2,
			expected: []int{3, 4, 5, 6, 7},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := deleteNode(tt.root, tt.key)
			actual := inorderTraversal(result)

			if !equalSlices(actual, tt.expected) {
				t.Errorf("deleteNode() = %v, expected %v", actual, tt.expected)
			}

			// Verify BST property is maintained
			if result != nil && !isBST(result, nil, nil) {
				t.Errorf("Result tree is not a valid BST")
			}
		})
	}
}

// Helper function to build a tree from level-order array
func buildTree(values []interface{}) *TreeNode {
	if len(values) == 0 || values[0] == nil {
		return nil
	}

	root := &TreeNode{Val: values[0].(int)}
	queue := []*TreeNode{root}
	i := 1

	for len(queue) > 0 && i < len(values) {
		node := queue[0]
		queue = queue[1:]

		if i < len(values) && values[i] != nil {
			node.Left = &TreeNode{Val: values[i].(int)}
			queue = append(queue, node.Left)
		}
		i++

		if i < len(values) && values[i] != nil {
			node.Right = &TreeNode{Val: values[i].(int)}
			queue = append(queue, node.Right)
		}
		i++
	}

	return root
}

// Helper function for inorder traversal
func inorderTraversal(root *TreeNode) []int {
	result := []int{}
	var traverse func(*TreeNode)
	traverse = func(node *TreeNode) {
		if node == nil {
			return
		}
		traverse(node.Left)
		result = append(result, node.Val)
		traverse(node.Right)
	}
	traverse(root)
	return result
}

// Helper function to compare slices
func equalSlices(a, b []int) bool {
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

// Helper function to verify BST property
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
