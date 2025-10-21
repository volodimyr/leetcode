// 144.  Binary tree preorder traversal
// Topics: 'Stack', 'Tree', 'Binary Tree', 'Depth-First Search'

// Given the root of a binary tree, return the preorder traversal of its nodes' values.

// Example 1:

// Input: root = [1,null,2,3]

// Output: [1,2,3]

// Explanation:

// Example 2:

// Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

// Output: [1,2,4,5,6,7,3,8,9]

// Explanation:

// Example 3:

// Input: root = []

// Output: []

// Example 4:

// Input: root = [1]

// Output: [1]

// Constraints:

//     The number of nodes in the tree is in the range [0, 100].
//     -100 <= Node.val <= 100

package binarytreepreordertraversal

func preorderTraversal(root *TreeNode) []int {
	arr := []int{}
	traversal(root, &arr)
	return arr
}

func traversal(root *TreeNode, arr *[]int) {
	if root == nil {
		return
	}
	*arr = append(*arr, root.Val)
	traversal(root.Left, arr)
	traversal(root.Right, arr)
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}
