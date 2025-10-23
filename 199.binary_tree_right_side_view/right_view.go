// 199. Binary tree right side view
// Topics: 'Tree', 'Binary Tree', 'Depth-First Search', 'Breadth-First Search'
// Level: 'Medium'

// Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

// Example 1:

// Input: root = [1,2,3,null,5,null,4]

// Output: [1,3,4]

// Explanation:

// Example 2:

// Input: root = [1,2,3,4,null,null,null,5]

// Output: [1,3,4,5]

// Explanation:

// Example 3:

// Input: root = [1,null,3]

// Output: [1,3]

// Example 4:

// Input: root = []

// Output: []

// Constraints:

//     The number of nodes in the tree is in the range [0, 100].
//     -100 <= Node.val <= 100

package binarytreerightsideview

func rightSideView(root *TreeNode) []int {
	arr := []int{}
	if root == nil {
		return arr
	}
	q := []*TreeNode{root}

	for len(q) != 0 {
		qlen := len(q)
		mostRight := q[0]
		arr = append(arr, mostRight.Val)
		for _, node := range q {
			if node.Right != nil {
				q = append(q, node.Right)
			}
			if node.Left != nil {
				q = append(q, node.Left)
			}
		}
		q = q[qlen:]
	}
	return arr
}

type TreeNode struct {
	Val   int
	Right *TreeNode
	Left  *TreeNode
}
