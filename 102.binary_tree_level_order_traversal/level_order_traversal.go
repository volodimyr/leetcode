// 102. Binary tree level order traversal
// Topics: 'Breadth-First Search', 'Tree', 'Binary Tree'
// Level: 'Medium'

// Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

// Example 1:

// Input: root = [3,9,20,null,null,15,7]
// Output: [[3],[9,20],[15,7]]

// Example 2:

// Input: root = [1]
// Output: [[1]]

// Example 3:

// Input: root = []
// Output: []

// Constraints:

//     The number of nodes in the tree is in the range [0, 2000].
//     -1000 <= Node.val <= 1000

package binarytreelevelordertraversal

func levelOrder(root *TreeNode) [][]int {
	var lvl int
	arr := [][]int{}
	if root == nil {
		return arr
	}
	q := []*TreeNode{root}

	for len(q) != 0 {
		arr = append(arr, make([]int, len(q)))
		for i := range len(q) {
			tn := q[0]
			q = q[1:]
			arr[lvl][i] = tn.Val
			if tn.Left != nil {
				q = append(q, tn.Left)
			}
			if tn.Right != nil {
				q = append(q, tn.Right)
			}
		}
		lvl++
	}
	return arr
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}
