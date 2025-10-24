// 105. Construct binary tree from preorder and inorder traversal
// Topics: 'Array', 'Hash Table', 'Divide and Conquer', 'Tree', 'Binary Tree'
// Level: 'Medium'

// Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

// Example 1:

// Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
// Output: [3,9,20,null,null,15,7]

// Example 2:

// Input: preorder = [-1], inorder = [-1]
// Output: [-1]

// Constraints:

//     1 <= preorder.length <= 3000
//     inorder.length == preorder.length
//     -3000 <= preorder[i], inorder[i] <= 3000
//     preorder and inorder consist of unique values.
//     Each value of inorder also appears in preorder.
//     preorder is guaranteed to be the preorder traversal of the tree.
//     inorder is guaranteed to be the inorder traversal of the tree.

package construct

func buildTree(preorder []int, inorder []int) *TreeNode {

	/*
		      3
		   /     \
		  9      20
		 / \    /  \
		2  11 15   7
	*/
	//	preorder := []int{3, 9, 2, 11, 20, 15, 7}
	// inorder := []int{2, 9, 11, 3, 15, 20, 7}

	m := make(map[int]int, len(inorder))
	for i, n := range inorder {
		m[n] = i
	}
	return build(m, preorder, inorder)
}

func build(m map[int]int, preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 {
		return nil
	}
	root := &TreeNode{Val: preorder[0]}
	split := m[root.Val]
	if split != 0 {
		root.Left = buildTree(preorder[1:split+1], inorder[:split])
	}
	if len(preorder) > split {
		root.Right = buildTree(preorder[split+1:], inorder[split+1:])
	}
	return root
}

func traverse(root *TreeNode, arr *[]int) {
	if root == nil {
		return
	}
	traverse(root.Left, arr)
	*arr = append(*arr, root.Val)
	traverse(root.Right, arr)
}

type TreeNode struct {
	Left  *TreeNode
	Right *TreeNode
	Val   int
}
