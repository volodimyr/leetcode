// 230. Kth smallest element in a BST
// Topics: 'Tree', 'Binary Search Tree', 'Binary Tree', 'Depth-First Search'
// Level: 'Medium'

// Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

// Example 1:

// Input: root = [3,1,4,null,2], k = 1
// Output: 1

// Example 2:

// Input: root = [5,3,6,2,4,null,null,1], k = 3
// Output: 3

// Constraints:

//     The number of nodes in the tree is n.
//     1 <= k <= n <= 104
//     0 <= Node.val <= 104

package kthsmallestelementinabst

func kthSmallest(root *TreeNode, k int) int {
	sm := -1
	find(root, &k, &sm)
	return sm
}

func find(root *TreeNode, k *int, sm *int) {
	if root == nil || *k == 0 {
		return
	}
	find(root.Left, k, sm)
	if *k > 0 {
		*sm = root.Val
		*k--
	}
	find(root.Right, k, sm)
}

type TreeNode struct {
	Val   int
	Right *TreeNode
	Left  *TreeNode
}
