// 700. Search in a binary search tree
// Topics: 'Binary Search Tree', 'Tree', 'Binary Tree'

// You are given the root of a binary search tree (BST) and an integer val.

// Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

// Example 1:

// Input: root = [4,2,7,1,3], val = 2
// Output: [2,1,3]

// Example 2:

// Input: root = [4,2,7,1,3], val = 5
// Output: []

// Constraints:

//     The number of nodes in the tree is in the range [1, 5000].
//     1 <= Node.val <= 107
//     root is a binary search tree.
//     1 <= val <= 107

package searchinabinarysearchtree

type TreeNode struct {
	Val   int
	Right *TreeNode
	Left  *TreeNode
}

func searchBST(root *TreeNode, val int) *TreeNode {
	// cur := root
	// for cur != nil {
	//     if cur.Val == val {
	//         return cur
	//     }
	//     if cur.Val > val {
	//         cur = cur.Left
	//     }else {
	//         cur = cur.Right
	//     }
	// }
	if root == nil {
		return root
	}
	if root.Val == val {
		return root
	}
	if root.Val > val {
		return searchBST(root.Left, val)
	}

	return searchBST(root.Right, val)
}
