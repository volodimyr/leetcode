package countgoodnodeinbinarytree

import "testing"

func TestGoodNodes(t *testing.T) {
	tests := []struct {
		name string
		root *TreeNode
		want int
	}{
		{
			name: "example 1",
			root: &TreeNode{
				Val:  3,
				Left: &TreeNode{Val: 1, Left: &TreeNode{Val: 3}},
				Right: &TreeNode{
					Val:   4,
					Left:  &TreeNode{Val: 1},
					Right: &TreeNode{Val: 5},
				},
			},
			want: 4,
		},
		{
			name: "example 2",
			root: &TreeNode{
				Val: 3,
				Left: &TreeNode{
					Val:   3,
					Left:  &TreeNode{Val: 4},
					Right: &TreeNode{Val: 2},
				},
			},
			want: 3,
		},
		{
			name: "example 3",
			root: &TreeNode{Val: 1},
			want: 1,
		},
		{
			name: "all increasing path",
			root: &TreeNode{
				Val: 1,
				Right: &TreeNode{
					Val:   2,
					Right: &TreeNode{Val: 3},
				},
			},
			want: 3,
		},
		{
			name: "all decreasing path",
			root: &TreeNode{
				Val: 3,
				Right: &TreeNode{
					Val:   2,
					Right: &TreeNode{Val: 1},
				},
			},
			want: 1,
		},
		{
			name: "negative values",
			root: &TreeNode{
				Val:   -1,
				Left:  &TreeNode{Val: -2},
				Right: &TreeNode{Val: -3},
			},
			want: 1,
		},
		{
			name: "negative to positive",
			root: &TreeNode{
				Val:   -1,
				Left:  &TreeNode{Val: 0},
				Right: &TreeNode{Val: 1},
			},
			want: 3,
		},
		{
			name: "duplicate values in path",
			root: &TreeNode{
				Val:  5,
				Left: &TreeNode{Val: 5, Left: &TreeNode{Val: 5}},
			},
			want: 3,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := goodNodes(tt.root)
			if got != tt.want {
				t.Errorf("goodNodes() = %v, want %v", got, tt.want)
			}
		})
	}
}
