// 104. Maximum depth of binary tree
// Topics: 'Tree', 'Binary Tree', 'Depth-First Search', 'Breadth-First Search'

// Given the root of a binary tree, return its maximum depth.

// A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

// Example 1:

// Input: root = [3,9,20,null,null,15,7]
// Output: 3

// Example 2:

// Input: root = [1,null,2]
// Output: 2

// Constraints:

//     The number of nodes in the tree is in the range [0, 104].
//     -100 <= Node.val <= 100

package maximumdepthofbinarytree

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	left := maxDepth(root.Left)
	right := maxDepth(root.Right)
	if left > right {
		return left + 1
	}
	return right + 1
}

type TreeNode struct {
	Val   int
	Right *TreeNode
	Left  *TreeNode
}
