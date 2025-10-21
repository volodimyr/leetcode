package binarytreepreordertraversal

import (
	"reflect"
	"testing"
)

func TestPostorderTraversal(t *testing.T) {
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
			want: []int{3, 2, 1},
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
			want: []int{4, 6, 7, 5, 2, 9, 8, 3, 1},
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
			want: []int{2, 1},
		},
		{
			name: "Two nodes - right child only",
			root: &TreeNode{
				Val:   1,
				Right: &TreeNode{Val: 2},
			},
			want: []int{2, 1},
		},
		{
			name: "Three nodes - complete binary tree",
			root: &TreeNode{
				Val:   1,
				Left:  &TreeNode{Val: 2},
				Right: &TreeNode{Val: 3},
			},
			want: []int{2, 3, 1},
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
			want: []int{1, 2, 3, 4},
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
			want: []int{4, 3, 2, 1},
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
			want: []int{4, 5, 2, 6, 7, 3, 1},
		},
		{
			name: "Tree with negative values",
			root: &TreeNode{
				Val:   0,
				Left:  &TreeNode{Val: -50},
				Right: &TreeNode{Val: 50},
			},
			want: []int{-50, 50, 0},
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
			want: []int{-99, -98, -100, 99, 98, 100, 0},
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
			want: []int{0, 2, 1, 4, 3, 6, 5},
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
			want: []int{0, 2, 4, 6, 5, 3, 1},
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
			want: []int{0, 1, 3, 5, 10},
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
			want: []int{5, 4, 3, 2, 1},
		},
		{
			name: "Multiple levels balanced",
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
			want: []int{3, 4, 2, 6, 7, 5, 1},
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
		{
			name: "Only left children path",
			root: &TreeNode{
				Val: 5,
				Left: &TreeNode{
					Val: 4,
					Left: &TreeNode{
						Val:  3,
						Left: &TreeNode{Val: 2},
					},
				},
			},
			want: []int{2, 3, 4, 5},
		},
		{
			name: "Only right children path",
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
			want: []int{4, 3, 2, 1},
		},
		{
			name: "Mixed single children",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Right: &TreeNode{
						Val: 3,
					},
				},
				Right: &TreeNode{
					Val: 4,
					Left: &TreeNode{
						Val: 5,
					},
				},
			},
			want: []int{3, 2, 5, 4, 1},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := postorderTraversal(tt.root)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("postorderTraversal() = %v, want %v", got, tt.want)
			}
		})
	}
}
