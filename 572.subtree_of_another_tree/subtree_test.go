package subtreeofanothertree

import "testing"

func TestIsSubtree(t *testing.T) {
	tests := []struct {
		name    string
		root    *TreeNode
		subRoot *TreeNode
		want    bool
	}{
		{
			name: "example 1 - subtree exists",
			root: &TreeNode{
				Val: 3,
				Left: &TreeNode{
					Val:   4,
					Left:  &TreeNode{Val: 1},
					Right: &TreeNode{Val: 2},
				},
				Right: &TreeNode{Val: 5},
			},
			subRoot: &TreeNode{
				Val:   4,
				Left:  &TreeNode{Val: 1},
				Right: &TreeNode{Val: 2},
			},
			want: true,
		},
		{
			name: "example 2 - subtree does not exist",
			root: &TreeNode{
				Val: 3,
				Left: &TreeNode{
					Val: 4,
					Left: &TreeNode{
						Val:  1,
						Left: &TreeNode{Val: 0},
					},
					Right: &TreeNode{Val: 2},
				},
				Right: &TreeNode{Val: 5},
			},
			subRoot: &TreeNode{
				Val:   4,
				Left:  &TreeNode{Val: 1},
				Right: &TreeNode{Val: 2},
			},
			want: false,
		},
		{
			name: "root and subRoot are identical",
			root: &TreeNode{
				Val:   1,
				Left:  &TreeNode{Val: 2},
				Right: &TreeNode{Val: 3},
			},
			subRoot: &TreeNode{
				Val:   1,
				Left:  &TreeNode{Val: 2},
				Right: &TreeNode{Val: 3},
			},
			want: true,
		},
		{
			name:    "single node match",
			root:    &TreeNode{Val: 1},
			subRoot: &TreeNode{Val: 1},
			want:    true,
		},
		{
			name:    "single node no match",
			root:    &TreeNode{Val: 1},
			subRoot: &TreeNode{Val: 2},
			want:    false,
		},
		{
			name: "subRoot is a leaf in root",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:  2,
					Left: &TreeNode{Val: 4},
				},
				Right: &TreeNode{Val: 3},
			},
			subRoot: &TreeNode{Val: 4},
			want:    true,
		},
		{
			name: "partial match - different structure",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:   2,
					Right: &TreeNode{Val: 3},
				},
			},
			subRoot: &TreeNode{
				Val:  2,
				Left: &TreeNode{Val: 3},
			},
			want: false,
		},
		{
			name: "subRoot larger than any subtree",
			root: &TreeNode{
				Val:   1,
				Left:  &TreeNode{Val: 2},
				Right: &TreeNode{Val: 3},
			},
			subRoot: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:  2,
					Left: &TreeNode{Val: 4},
				},
				Right: &TreeNode{Val: 3},
			},
			want: false,
		},
		{
			name: "multiple nodes with same value",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:  2,
					Left: &TreeNode{Val: 4},
				},
				Right: &TreeNode{
					Val:   2,
					Left:  &TreeNode{Val: 4},
					Right: &TreeNode{Val: 5},
				},
			},
			subRoot: &TreeNode{
				Val:  2,
				Left: &TreeNode{Val: 4},
			},
			want: true,
		},
		{
			name: "deep tree with subtree at bottom",
			root: &TreeNode{
				Val: 10,
				Left: &TreeNode{
					Val: 5,
					Left: &TreeNode{
						Val:   3,
						Left:  &TreeNode{Val: 1},
						Right: &TreeNode{Val: 4},
					},
				},
			},
			subRoot: &TreeNode{
				Val:   3,
				Left:  &TreeNode{Val: 1},
				Right: &TreeNode{Val: 4},
			},
			want: true,
		},
		{
			name: "same values but different structure",
			root: &TreeNode{
				Val:  1,
				Left: &TreeNode{Val: 2},
			},
			subRoot: &TreeNode{
				Val:   1,
				Right: &TreeNode{Val: 2},
			},
			want: false,
		},
		{
			name: "negative values",
			root: &TreeNode{
				Val:   -10,
				Left:  &TreeNode{Val: -20},
				Right: &TreeNode{Val: -5},
			},
			subRoot: &TreeNode{
				Val: -20,
			},
			want: true,
		},
		{
			name: "complex tree with no match",
			root: &TreeNode{
				Val: 12,
				Left: &TreeNode{
					Val:   7,
					Left:  &TreeNode{Val: 3},
					Right: &TreeNode{Val: 9},
				},
				Right: &TreeNode{
					Val:   15,
					Right: &TreeNode{Val: 20},
				},
			},
			subRoot: &TreeNode{
				Val:  7,
				Left: &TreeNode{Val: 3},
				Right: &TreeNode{
					Val:  9,
					Left: &TreeNode{Val: 8},
				},
			},
			want: false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := isSubtree(tt.root, tt.subRoot)
			if got != tt.want {
				t.Errorf("isSubtree() = %v, want %v", got, tt.want)
			}
		})
	}
}
