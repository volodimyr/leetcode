package deleteleaveswithagivenvalue

import (
	"reflect"
	"testing"
)

func TestRemoveLeafNodes(t *testing.T) {
	tests := []struct {
		name   string
		root   *TreeNode
		target int
		want   *TreeNode
	}{
		{
			name: "example 1",
			//     1              1
			//    / \              \
			//   2   3     =>       3
			//  /   / \              \
			// 2   2   4              4
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:  2,
					Left: &TreeNode{Val: 2},
				},
				Right: &TreeNode{
					Val:   3,
					Left:  &TreeNode{Val: 2},
					Right: &TreeNode{Val: 4},
				},
			},
			target: 2,
			want: &TreeNode{
				Val:  1,
				Left: nil,
				Right: &TreeNode{
					Val:   3,
					Left:  nil,
					Right: &TreeNode{Val: 4},
				},
			},
		},
		{
			name: "example 2",
			//     1          1
			//    / \        /
			//   3   3  =>  3
			//  / \          \
			// 3   2          2
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:   3,
					Left:  &TreeNode{Val: 3},
					Right: &TreeNode{Val: 2},
				},
				Right: &TreeNode{Val: 3},
			},
			target: 3,
			want: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:   3,
					Left:  nil,
					Right: &TreeNode{Val: 2},
				},
				Right: nil,
			},
		},
		{
			name: "example 3",
			//   1          1
			//  /
			// 2      =>
			// |
			// 2
			// |
			// 2
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val:  2,
						Left: &TreeNode{Val: 2},
					},
				},
			},
			target: 2,
			want:   &TreeNode{Val: 1},
		},
		{
			name: "single node matching target",
			// 5  =>  (null)
			root:   &TreeNode{Val: 5},
			target: 5,
			want:   nil,
		},
		{
			name: "single node not matching target",
			// 5  =>  5
			root:   &TreeNode{Val: 5},
			target: 3,
			want:   &TreeNode{Val: 5},
		},
		{
			name: "no nodes match target",
			//   1        1
			//  / \  =>  / \
			// 2   3    2   3
			root: &TreeNode{
				Val:   1,
				Left:  &TreeNode{Val: 2},
				Right: &TreeNode{Val: 3},
			},
			target: 5,
			want: &TreeNode{
				Val:   1,
				Left:  &TreeNode{Val: 2},
				Right: &TreeNode{Val: 3},
			},
		},
		{
			name: "all leaf nodes match target",
			//     1            1
			//    / \          / \
			//   2   4   =>   2   4
			//  / \ / \
			// 3  3 3  3
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:   2,
					Left:  &TreeNode{Val: 3},
					Right: &TreeNode{Val: 3},
				},
				Right: &TreeNode{
					Val:   4,
					Left:  &TreeNode{Val: 3},
					Right: &TreeNode{Val: 3},
				},
			},
			target: 3,
			want: &TreeNode{
				Val:   1,
				Left:  &TreeNode{Val: 2},
				Right: &TreeNode{Val: 4},
			},
		},
		{
			name: "cascading deletion left side",
			//    10           10
			//   /  \           \
			//  5   20   =>     20
			//  |
			//  5
			//  |
			//  5
			root: &TreeNode{
				Val: 10,
				Left: &TreeNode{
					Val: 5,
					Left: &TreeNode{
						Val:  5,
						Left: &TreeNode{Val: 5},
					},
				},
				Right: &TreeNode{Val: 20},
			},
			target: 5,
			want: &TreeNode{
				Val:   10,
				Left:  nil,
				Right: &TreeNode{Val: 20},
			},
		},
		{
			name: "cascading deletion right side",
			//   10          10
			//  /  \        /
			// 20   5  =>  20
			//      |
			//      5
			//      |
			//      5
			root: &TreeNode{
				Val:  10,
				Left: &TreeNode{Val: 20},
				Right: &TreeNode{
					Val: 5,
					Right: &TreeNode{
						Val:   5,
						Right: &TreeNode{Val: 5},
					},
				},
			},
			target: 5,
			want: &TreeNode{
				Val:   10,
				Left:  &TreeNode{Val: 20},
				Right: nil,
			},
		},
		{
			name: "target in middle nodes only",
			//   1          1
			//  / \        / \
			// 2   5  =>  2   5
			/// \        / \
			//3   4      3   4
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:   2,
					Left:  &TreeNode{Val: 3},
					Right: &TreeNode{Val: 4},
				},
				Right: &TreeNode{Val: 5},
			},
			target: 2,
			want: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:   2,
					Left:  &TreeNode{Val: 3},
					Right: &TreeNode{Val: 4},
				},
				Right: &TreeNode{Val: 5},
			},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := removeLeafNodes(tt.root, tt.target)
			if !treesEqual(got, tt.want) {
				t.Errorf("removeLeafNodes() = %v, want %v", treeToSlice(got), treeToSlice(tt.want))
			}
		})
	}
}

func treesEqual(t1, t2 *TreeNode) bool {
	if t1 == nil && t2 == nil {
		return true
	}
	if t1 == nil || t2 == nil {
		return false
	}
	if t1.Val != t2.Val {
		return false
	}
	return treesEqual(t1.Left, t2.Left) && treesEqual(t1.Right, t2.Right)
}

func treeToSlice(root *TreeNode) []interface{} {
	if root == nil {
		return []interface{}{}
	}
	result := []interface{}{}
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		if node == nil {
			result = append(result, nil)
		} else {
			result = append(result, node.Val)
			queue = append(queue, node.Left)
			queue = append(queue, node.Right)
		}
	}
	for len(result) > 0 && result[len(result)-1] == nil {
		result = result[:len(result)-1]
	}
	return result
}

func TestTraversal(t *testing.T) {
	tests := []struct {
		name   string
		root   *TreeNode
		target int
		want   *TreeNode
	}{
		{
			name:   "nil root",
			root:   nil,
			target: 1,
			want:   nil,
		},
		{
			name: "leaf node matches target",
			// 5  =>  (null)
			root:   &TreeNode{Val: 5},
			target: 5,
			want:   nil,
		},
		{
			name: "leaf node does not match target",
			// 5  =>  5
			root:   &TreeNode{Val: 5},
			target: 3,
			want:   &TreeNode{Val: 5},
		},
		{
			name: "parent becomes leaf after child deletion",
			// 2      (null)
			// |  =>
			// 2
			root: &TreeNode{
				Val:  2,
				Left: &TreeNode{Val: 2},
			},
			target: 2,
			want:   nil,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := removeLeafNodes(tt.root, tt.target)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("traversal() = %v, want %v", got, tt.want)
			}
		})
	}
}
