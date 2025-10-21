// 145. Binary Tree Postorder Traversal
// Topics: 'Stack', 'Tree', 'Binary Tree', 'Depth-First Search'

// Given the root of a binary tree, return the postorder traversal of its nodes' values.

// Example 1:

// Input: root = [1,null,2,3]

// Output: [3,2,1]

// Explanation:

// Example 2:

// Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

// Output: [4,6,7,5,2,9,8,3,1]

// Explanation:

// Example 3:

// Input: root = []

// Output: []

// Example 4:

// Input: root = [1]

// Output: [1]

// Constraints:

//     The number of the nodes in the tree is in the range [0, 100].
//     -100 <= Node.val <= 100

package binarytreepreordertraversal

func postorderTraversal(root *TreeNode) []int {
	arr := []int{}
	traversal(root, &arr)
	return arr
}

func traversal(root *TreeNode, arr *[]int) {
	if root == nil {
		return
	}

	traversal(root.Left, arr)
	traversal(root.Right, arr)
	*arr = append(*arr, root.Val)
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}
