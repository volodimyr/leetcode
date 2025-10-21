package kthsmallestelementinabst

import "testing"

func TestKthSmallest(t *testing.T) {
	tests := []struct {
		name string
		root *TreeNode
		k    int
		want int
	}{
		{
			name: "Example 1: k=1, smallest element",
			root: &TreeNode{
				Val: 3,
				Left: &TreeNode{
					Val:   1,
					Right: &TreeNode{Val: 2},
				},
				Right: &TreeNode{Val: 4},
			},
			k:    1,
			want: 1,
		},
		{
			name: "Example 2: k=3, middle element",
			root: &TreeNode{
				Val: 5,
				Left: &TreeNode{
					Val: 3,
					Left: &TreeNode{
						Val:  2,
						Left: &TreeNode{Val: 1},
					},
					Right: &TreeNode{Val: 4},
				},
				Right: &TreeNode{Val: 6},
			},
			k:    3,
			want: 3,
		},
		{
			name: "Single node tree",
			root: &TreeNode{Val: 1},
			k:    1,
			want: 1,
		},
		{
			name: "Two nodes, k=1",
			root: &TreeNode{
				Val:  2,
				Left: &TreeNode{Val: 1},
			},
			k:    1,
			want: 1,
		},
		{
			name: "Two nodes, k=2",
			root: &TreeNode{
				Val:  2,
				Left: &TreeNode{Val: 1},
			},
			k:    2,
			want: 2,
		},
		{
			name: "Right-skewed tree, k=1",
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
			k:    1,
			want: 1,
		},
		{
			name: "Right-skewed tree, k=4",
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
			k:    4,
			want: 4,
		},
		{
			name: "Left-skewed tree, k=1",
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
			k:    1,
			want: 1,
		},
		{
			name: "Left-skewed tree, k=3",
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
			k:    3,
			want: 3,
		},
		{
			name: "Balanced tree, k=last element",
			root: &TreeNode{
				Val: 4,
				Left: &TreeNode{
					Val:   2,
					Left:  &TreeNode{Val: 1},
					Right: &TreeNode{Val: 3},
				},
				Right: &TreeNode{
					Val:   6,
					Left:  &TreeNode{Val: 5},
					Right: &TreeNode{Val: 7},
				},
			},
			k:    7,
			want: 7,
		},
		{
			name: "Balanced tree, k=middle element",
			root: &TreeNode{
				Val: 4,
				Left: &TreeNode{
					Val:   2,
					Left:  &TreeNode{Val: 1},
					Right: &TreeNode{Val: 3},
				},
				Right: &TreeNode{
					Val:   6,
					Left:  &TreeNode{Val: 5},
					Right: &TreeNode{Val: 7},
				},
			},
			k:    4,
			want: 4,
		},
		{
			name: "Large values",
			root: &TreeNode{
				Val:   10000,
				Left:  &TreeNode{Val: 5000},
				Right: &TreeNode{Val: 10004},
			},
			k:    2,
			want: 10000,
		},
		{
			name: "Values with 0",
			root: &TreeNode{
				Val:   1,
				Left:  &TreeNode{Val: 0},
				Right: &TreeNode{Val: 2},
			},
			k:    1,
			want: 0,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := kthSmallest(tt.root, tt.k)
			if got != tt.want {
				t.Errorf("kthSmallest() = %v, want %v", got, tt.want)
			}
		})
	}
}
