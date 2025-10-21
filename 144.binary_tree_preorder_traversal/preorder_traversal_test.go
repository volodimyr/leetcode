package binarytreepreordertraversal

import (
	"reflect"
	"testing"
)

func TestPreorderTraversal(t *testing.T) {
	tests := []struct {
		name string
		root *TreeNode
		want []int
	}{
		{
			name: "Example 1: Right-skewed with left child",
			root: &TreeNode{
				Val: 1,
				Right: &TreeNode{
					Val:  2,
					Left: &TreeNode{Val: 3},
				},
			},
			want: []int{1, 2, 3},
		},
		{
			name: "Example 2: Complex tree",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val: 4,
					},
					Right: &TreeNode{
						Val:   5,
						Left:  &TreeNode{Val: 6},
						Right: &TreeNode{Val: 7},
					},
				},
				Right: &TreeNode{
					Val: 3,
					Right: &TreeNode{
						Val:  8,
						Left: &TreeNode{Val: 9},
					},
				},
			},
			want: []int{1, 2, 4, 5, 6, 7, 3, 8, 9},
		},
		{
			name: "Example 3: Empty tree",
			root: nil,
			want: []int{},
		},
		{
			name: "Example 4: Single node",
			root: &TreeNode{Val: 1},
			want: []int{1},
		},
		{
			name: "Two nodes - left child only",
			root: &TreeNode{
				Val:  1,
				Left: &TreeNode{Val: 2},
			},
			want: []int{1, 2},
		},
		{
			name: "Two nodes - right child only",
			root: &TreeNode{
				Val:   1,
				Right: &TreeNode{Val: 2},
			},
			want: []int{1, 2},
		},
		{
			name: "Three nodes - complete binary tree",
			root: &TreeNode{
				Val:   1,
				Left:  &TreeNode{Val: 2},
				Right: &TreeNode{Val: 3},
			},
			want: []int{1, 2, 3},
		},
		{
			name: "Left-skewed tree",
			root: &TreeNode{
				Val: 4,
				Left: &TreeNode{
					Val: 3,
					Left: &TreeNode{
						Val:  2,
						Left: &TreeNode{Val: 1},
					},
				},
			},
			want: []int{4, 3, 2, 1},
		},
		{
			name: "Right-skewed tree",
			root: &TreeNode{
				Val: 1,
				Right: &TreeNode{
					Val: 2,
					Right: &TreeNode{
						Val:   3,
						Right: &TreeNode{Val: 4},
					},
				},
			},
			want: []int{1, 2, 3, 4},
		},
		{
			name: "Balanced binary tree",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:   2,
					Left:  &TreeNode{Val: 4},
					Right: &TreeNode{Val: 5},
				},
				Right: &TreeNode{
					Val:   3,
					Left:  &TreeNode{Val: 6},
					Right: &TreeNode{Val: 7},
				},
			},
			want: []int{1, 2, 4, 5, 3, 6, 7},
		},
		{
			name: "Tree with negative values",
			root: &TreeNode{
				Val:   0,
				Left:  &TreeNode{Val: -50},
				Right: &TreeNode{Val: 50},
			},
			want: []int{0, -50, 50},
		},
		{
			name: "Tree with boundary values",
			root: &TreeNode{
				Val: 0,
				Left: &TreeNode{
					Val:   -100,
					Left:  &TreeNode{Val: -99},
					Right: &TreeNode{Val: -98},
				},
				Right: &TreeNode{
					Val:   100,
					Left:  &TreeNode{Val: 99},
					Right: &TreeNode{Val: 98},
				},
			},
			want: []int{0, -100, -99, -98, 100, 99, 98},
		},
		{
			name: "Unbalanced tree - heavy left",
			root: &TreeNode{
				Val: 5,
				Left: &TreeNode{
					Val: 3,
					Left: &TreeNode{
						Val:   1,
						Left:  &TreeNode{Val: 0},
						Right: &TreeNode{Val: 2},
					},
					Right: &TreeNode{Val: 4},
				},
				Right: &TreeNode{Val: 6},
			},
			want: []int{5, 3, 1, 0, 2, 4, 6},
		},
		{
			name: "Unbalanced tree - heavy right",
			root: &TreeNode{
				Val:  1,
				Left: &TreeNode{Val: 0},
				Right: &TreeNode{
					Val:  3,
					Left: &TreeNode{Val: 2},
					Right: &TreeNode{
						Val:   5,
						Left:  &TreeNode{Val: 4},
						Right: &TreeNode{Val: 6},
					},
				},
			},
			want: []int{1, 0, 3, 2, 5, 4, 6},
		},
		{
			name: "Deep left subtree only",
			root: &TreeNode{
				Val: 10,
				Left: &TreeNode{
					Val: 5,
					Left: &TreeNode{
						Val: 3,
						Left: &TreeNode{
							Val:  1,
							Left: &TreeNode{Val: 0},
						},
					},
				},
			},
			want: []int{10, 5, 3, 1, 0},
		},
		{
			name: "Zigzag pattern",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Right: &TreeNode{
						Val: 3,
						Left: &TreeNode{
							Val:   4,
							Right: &TreeNode{Val: 5},
						},
					},
				},
			},
			want: []int{1, 2, 3, 4, 5},
		},
		{
			name: "Maximum nodes (100 nodes would be too large, using smaller)",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:   2,
					Left:  &TreeNode{Val: 3},
					Right: &TreeNode{Val: 4},
				},
				Right: &TreeNode{
					Val:   5,
					Left:  &TreeNode{Val: 6},
					Right: &TreeNode{Val: 7},
				},
			},
			want: []int{1, 2, 3, 4, 5, 6, 7},
		},
		{
			name: "All same values",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:   1,
					Left:  &TreeNode{Val: 1},
					Right: &TreeNode{Val: 1},
				},
				Right: &TreeNode{
					Val:   1,
					Left:  &TreeNode{Val: 1},
					Right: &TreeNode{Val: 1},
				},
			},
			want: []int{1, 1, 1, 1, 1, 1, 1},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := preorderTraversal(tt.root)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("preorderTraversal() = %v, want %v", got, tt.want)
			}
		})
	}
}
