// 257. Binary tree path
// Topics: 'Tree', 'Binary Tree', 'Depth-First Search', 'Backtracking', 'String'

// Given the root of a binary tree, return all root-to-leaf paths in any order.

// A leaf is a node with no children.

// Example 1:

// Input: root = [1,2,3,null,5]
// Output: ["1->2->5","1->3"]

// Example 2:

// Input: root = [1]
// Output: ["1"]

// Constraints:

//     The number of nodes in the tree is in the range [1, 100].
//     -100 <= Node.val <= 100

package binarytreepaths

import (
	"strconv"
	"strings"
)

func draw(arr []int) string {
	var path strings.Builder
	for i, node := range arr {
		path.WriteString(strconv.Itoa(node))
		if i != len(arr)-1 {
			path.WriteString("->")
		}
	}
	return path.String()
}

func binaryTreePaths(root *TreeNode) []string {
	arr := []int{}
	paths := []string{}
	track(root, &arr, &paths)
	return paths
}

func track(root *TreeNode, arr *[]int, paths *[]string) {
	if root == nil {
		return
	}
	*arr = append(*arr, root.Val)

	if root.Left == nil && root.Right == nil {
		*paths = append(*paths, draw(*arr))
	}
	track(root.Left, arr, paths)
	track(root.Right, arr, paths)
	*arr = (*arr)[:len(*arr)-1]
}

type TreeNode struct {
	Val   int
	Right *TreeNode
	Left  *TreeNode
}
