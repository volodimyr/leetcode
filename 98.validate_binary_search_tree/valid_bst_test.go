package validatebinarysearchtree

import "testing"

func TestIsValidBST(t *testing.T) {
	tests := []struct {
		name string
		root *TreeNode
		want bool
	}{
		{
			name: "example 1: [2,1,3]",
			//     2
			//    / \
			//   1   3
			root: &TreeNode{
				Val:   2,
				Left:  &TreeNode{Val: 1},
				Right: &TreeNode{Val: 3},
			},
			want: true,
		},
		{
			name: "example 2: [5,1,4,null,null,3,6]",
			//       5
			//      / \
			//     1   4
			//        / \
			//       3   6
			root: &TreeNode{
				Val:  5,
				Left: &TreeNode{Val: 1},
				Right: &TreeNode{
					Val:   4,
					Left:  &TreeNode{Val: 3},
					Right: &TreeNode{Val: 6},
				},
			},
			want: false,
		},
		{
			name: "single node",
			//   1
			root: &TreeNode{Val: 1},
			want: true,
		},
		{
			name: "nil root",
			root: nil,
			want: true,
		},
		{
			name: "left child equal to parent",
			//   2
			//  /
			// 2
			root: &TreeNode{
				Val:  2,
				Left: &TreeNode{Val: 2},
			},
			want: false,
		},
		{
			name: "right child equal to parent",
			//   2
			//    \
			//     2
			root: &TreeNode{
				Val:   2,
				Right: &TreeNode{Val: 2},
			},
			want: false,
		},
		{
			name: "valid larger tree",
			//       10
			//      /  \
			//     5    15
			//    / \   / \
			//   3   7 13  20
			root: &TreeNode{
				Val: 10,
				Left: &TreeNode{
					Val:   5,
					Left:  &TreeNode{Val: 3},
					Right: &TreeNode{Val: 7},
				},
				Right: &TreeNode{
					Val:   15,
					Left:  &TreeNode{Val: 13},
					Right: &TreeNode{Val: 20},
				},
			},
			want: true,
		},
		{
			name: "left subtree value greater than ancestor",
			// 15 > 10 but 15 is in left subtree
			//       10
			//      /  \
			//     5    20
			//    / \
			//   3   8
			//        \
			//         15
			root: &TreeNode{
				Val: 10,
				Left: &TreeNode{
					Val:  5,
					Left: &TreeNode{Val: 3},
					Right: &TreeNode{
						Val:   8,
						Right: &TreeNode{Val: 15},
					},
				},
				Right: &TreeNode{Val: 20},
			},
			want: false,
		},
		{
			name: "right subtree value less than ancestor",
			// 6 < 10 but 6 is in right subtree
			//       10
			//      /  \
			//     5    15
			//         /  \
			//        6    20
			//            /
			//           18
			root: &TreeNode{
				Val:  10,
				Left: &TreeNode{Val: 5},
				Right: &TreeNode{
					Val:  15,
					Left: &TreeNode{Val: 6},
					Right: &TreeNode{
						Val:  20,
						Left: &TreeNode{Val: 18},
					},
				},
			},
			want: false,
		},
		{
			name: "only left children",
			//     5
			//    /
			//   3
			//  /
			// 1
			root: &TreeNode{
				Val: 5,
				Left: &TreeNode{
					Val: 3,
					Left: &TreeNode{
						Val: 1,
					},
				},
			},
			want: true,
		},
		{
			name: "only right children",
			//   1
			//    \
			//     3
			//      \
			//       5
			root: &TreeNode{
				Val: 1,
				Right: &TreeNode{
					Val: 3,
					Right: &TreeNode{
						Val: 5,
					},
				},
			},
			want: true,
		},
		{
			name: "negative values valid",
			//      0
			//     / \
			//   -5   5
			root: &TreeNode{
				Val:   0,
				Left:  &TreeNode{Val: -5},
				Right: &TreeNode{Val: 5},
			},
			want: true,
		},
		{
			name: "negative values invalid",
			// -15 > -20 but -15 is in right subtree of root -10
			//       -10
			//       /  \
			//     -20   0
			//          /
			//        -15
			root: &TreeNode{
				Val:  -10,
				Left: &TreeNode{Val: -20},
				Right: &TreeNode{
					Val:  0,
					Left: &TreeNode{Val: -15},
				},
			},
			want: false,
		},
		{
			name: "min and max int values",
			//           0
			//          / \
			//  -2147483648  2147483647
			root: &TreeNode{
				Val:   0,
				Left:  &TreeNode{Val: -2147483648},
				Right: &TreeNode{Val: 2147483647},
			},
			want: true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := isValidBST(tt.root)
			if got != tt.want {
				t.Errorf("isValidBST() = %v, want %v", got, tt.want)
			}
		})
	}
}
