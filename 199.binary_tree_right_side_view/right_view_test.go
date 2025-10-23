package binarytreerightsideview

import "testing"

func TestRightSideView(t *testing.T) {
	tests := []struct {
		name string
		root *TreeNode
		want []int
	}{
		{
			name: "empty tree",
			root: nil,
			want: []int{},
		},
		{
			name: "single node",
			root: &TreeNode{Val: 1},
			want: []int{1},
		},
		{
			name: "example 1",
			// [1,2,3,null,5,null,4]
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Right: &TreeNode{
						Val: 5,
					},
				},
				Right: &TreeNode{
					Val: 3,
					Right: &TreeNode{
						Val: 4,
					},
				},
			},
			want: []int{1, 3, 4},
		},
		{
			name: "example 2",
			// [1,2,3,4,null,null,null,5]
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val:  4,
						Left: &TreeNode{Val: 5},
					},
				},
				Right: &TreeNode{Val: 3},
			},
			want: []int{1, 3, 4, 5},
		},
		{
			name: "example 3",
			// [1,null,3]
			root: &TreeNode{
				Val: 1,
				Right: &TreeNode{
					Val: 3,
				},
			},
			want: []int{1, 3},
		},
		{
			name: "left skewed tree",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val: 3,
					},
				},
			},
			want: []int{1, 2, 3},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := rightSideView(tt.root)
			if len(got) != len(tt.want) {
				t.Fatalf("expected %v, got %v", tt.want, got)
			}
			for i := range got {
				if got[i] != tt.want[i] {
					t.Errorf("%s: expected %v, got %v", tt.name, tt.want, got)
					break
				}
			}
		})
	}
}
