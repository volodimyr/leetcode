// 110. Balanced binary tree
// Topics: 'Tree', 'Binary Tree', 'Depth-First Search'

// Given a binary tree, determine if it is

// Example 1:

// Input: root = [3,9,20,null,null,15,7]
// Output: true

// Example 2:

// Input: root = [1,2,2,3,3,null,null,4,4]
// Output: false

// Example 3:

// Input: root = []
// Output: true

// Constraints:

//     The number of nodes in the tree is in the range [0, 5000].
//     -104 <= Node.val <= 104

package balancedbinarytree

type TreeNode struct {
	Right *TreeNode
	Left  *TreeNode
	Val   int
}

func isBalanced(root *TreeNode) bool {
	return height(root) != -1
}

func height(root *TreeNode) int {
	if root == nil {
		return 0
	}
	left := height(root.Left)
	if left == -1 {
		return left
	}
	right := height(root.Right)
	if right == -1 {
		return right
	}
	if abs(left-right) > 1 {
		return -1
	}
	return max(left, right) + 1
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
