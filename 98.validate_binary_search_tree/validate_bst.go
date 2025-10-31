// 98. Validate Binary Search Tree
// Topics: 'Binary Search Tree', 'Tree', 'Binary Tree', 'Depth-First Search'
// Level: 'Medium'

// Given the root of a binary tree, determine if it is a valid binary search tree (BST).

// A valid BST is defined as follows:

//     The left

//     of a node contains only nodes with keys strictly less than the node's key.
//     The right subtree of a node contains only nodes with keys strictly greater than the node's key.
//     Both the left and right subtrees must also be binary search trees.

// Example 1:

// Input: root = [2,1,3]
// Output: true

// Example 2:

// Input: root = [5,1,4,null,null,3,6]
// Output: false
// Explanation: The root node's value is 5 but its right child's value is 4.

// Constraints:

//     The number of nodes in the tree is in the range [1, 104].
//     -231 <= Node.val <= 231 - 1

package validatebinarysearchtree

func isValidBST(root *TreeNode) bool {
	return valid(root, nil, nil)
}

func valid(root *TreeNode, min, max *int) bool {
	if root == nil {
		return true
	}
	if min != nil && root.Val <= *min {
		return false
	}
	if max != nil && root.Val >= *max {
		return false
	}

	return valid(root.Left, min, &root.Val) && valid(root.Right, &root.Val, max)
}

type TreeNode struct {
	Right *TreeNode
	Left  *TreeNode
	Val   int
}
