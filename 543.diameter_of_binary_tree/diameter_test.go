package diameterofbinarytree

import "testing"

func TestDiameterOfBinaryTree(t *testing.T) {
	tests := []struct {
		name string
		root *TreeNode
		want int
	}{
		{
			name: "example 1",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:   2,
					Left:  &TreeNode{Val: 4},
					Right: &TreeNode{Val: 5},
				},
				Right: &TreeNode{Val: 3},
			},
			want: 3, // [4,2,1,3] or [5,2,1,3]
		},
		{
			name: "example 2",
			root: &TreeNode{
				Val:  1,
				Left: &TreeNode{Val: 2},
			},
			want: 1,
		},
		{
			name: "single node",
			root: &TreeNode{Val: 42},
			want: 0, // only one node, no edges
		},
		{
			name: "empty tree",
			root: nil,
			want: 0,
		},
		{
			name: "unbalanced tree",
			root: &TreeNode{
				Val:  1,
				Left: &TreeNode{Val: 2, Left: &TreeNode{Val: 3, Left: &TreeNode{Val: 4}}},
			},
			want: 3, // [4,3,2,1]
		},
		{
			name: "balanced tree depth 3",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:  2,
					Left: &TreeNode{Val: 4},
					Right: &TreeNode{
						Val:   5,
						Left:  &TreeNode{Val: 6},
						Right: &TreeNode{Val: 7},
					},
				},
				Right: &TreeNode{Val: 3},
			},
			want: 4, // [6,5,2,1,3]
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := diameterOfBinaryTree(tt.root)
			if got != tt.want {
				t.Errorf("diameterOfBinaryTree(%v) = %d, want %d", tt.name, got, tt.want)
			}
		})
	}
}
