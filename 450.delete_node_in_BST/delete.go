// 450. Delete node in BST
// Topics: 'Tree', 'Binary Search Tree', 'Binary Tree'
// Level: 'Medium'

// Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

// Basically, the deletion can be divided into two stages:

//     Search for a node to remove.
//     If the node is found, delete the node.

// Example 1:

// Input: root = [5,3,6,2,4,null,7], key = 3
// Output: [5,4,6,2,null,null,7]
// Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
// One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
// Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

// Example 2:

// Input: root = [5,3,6,2,4,null,7], key = 0
// Output: [5,3,6,2,4,null,7]
// Explanation: The tree does not contain a node with value = 0.

// Example 3:

// Input: root = [], key = 0
// Output: []

// Constraints:

//     The number of nodes in the tree is in the range [0, 104].
//     -105 <= Node.val <= 105
//     Each node has a unique value.
//     root is a valid binary search tree.
//     -105 <= key <= 105

// Follow up: Could you solve it with time complexity O(height of tree)?

package deletenodeinbst

type TreeNode struct {
	Val   int
	Right *TreeNode
	Left  *TreeNode
}

func deleteNode(root *TreeNode, key int) *TreeNode {
	if root == nil {
		return root
	}

	if root.Val > key {
		root.Left = deleteNode(root.Left, key)
	} else if root.Val < key {
		root.Right = deleteNode(root.Right, key)
	} else {
		if root.Left == nil {
			return root.Right
		}
		if root.Right == nil {
			return root.Left
		}
		root.Val = successor(root.Right, root)
	}

	return root

}

func successor(node *TreeNode, parent *TreeNode) int {
	if node.Left == nil {
		val := node.Val

		if parent.Right == node {
			parent.Right = node.Right
		} else {
			parent.Left = node.Right
		}
		return val
	}
	return successor(node.Left, node)
}

// func deleteNode(root *TreeNode, key int) *TreeNode {
// 	if root == nil {
// 		return root
// 	}
// 	var parent *TreeNode
// 	cur := root
// 	for cur != nil && cur.Val != key {
// 		parent = cur
// 		if cur.Val > key {
// 			cur = cur.Left
// 		} else {
// 			cur = cur.Right
// 		}
// 	}
// 	if cur == nil {
// 		return root
// 	}

// 	successor := successor(cur)
// 	if parent == nil {
// 		return successor
// 	}

// 	if parent.Left == cur {
// 		parent.Left = successor
// 	} else {
// 		parent.Right = successor
// 	}

// 	return root
// }

// func successor(root *TreeNode) *TreeNode {
// 	if root.Right == nil {
// 		return root.Left
// 	}
// 	if root.Left == nil {
// 		return root.Right
// 	}
// 	parent := root
// 	successor := root.Right
// 	for successor.Left != nil {
// 		parent = successor
// 		successor = successor.Left
// 	}
// 	if parent == root {
// 		successor.Left = root.Left
// 		return successor
// 	}
// 	parent.Left = successor.Right
// 	successor.Left = root.Left
// 	successor.Right = root.Right

// 	return successor
// }
