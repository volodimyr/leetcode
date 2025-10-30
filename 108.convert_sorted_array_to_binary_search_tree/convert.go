// 108. Conver sorted array to binary search tree
// Topics: 'Array', 'Divide and Conquer', 'Tree', 'Binary Tree', 'Binary Searh Tree'

// Given an integer array nums where the elements are sorted in ascending order, convert it to a

// binary search tree.

// Example 1:

// Input: nums = [-10,-3,0,5,9]
// Output: [0,-3,9,-10,null,5]
// Explanation: [0,-10,5,null,-3,null,9] is also accepted:

// Example 2:

// Input: nums = [1,3]
// Output: [3,1]
// Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

// Constraints:

//     1 <= nums.length <= 104
//     -104 <= nums[i] <= 104
//     nums is sorted in a strictly increasing order.

package convertsortedarraytobinarysearchtree

import "fmt"

func sortedArrayToBST(nums []int) *TreeNode {
	if len(nums) < 1 {
		return nil
	}
	mid := len(nums) / 2
	root := &TreeNode{Val: nums[mid]}
	root.Left = sortedArrayToBST(nums[:mid])
	root.Right = sortedArrayToBST(nums[mid+1:])
	return root
}

type TreeNode struct {
	Val   int
	Right *TreeNode
	Left  *TreeNode
}

func traversal(root *TreeNode) {
	if root == nil {
		return
	}
	traversal(root.Left)
	fmt.Println("val = ", root.Val)
	traversal(root.Right)
}
