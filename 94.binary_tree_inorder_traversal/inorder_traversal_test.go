package binarytreeinordertraversal

import (
	"reflect"
	"testing"
)

func TestInorderTraversal(t *testing.T) {
	tests := []struct {
		name string
		root *TreeNode
		want []int
	}{
		{
			name: "Example 1: [1,null,2,3]",
			root: &TreeNode{
				Val: 1,
				Right: &TreeNode{
					Val:  2,
					Left: &TreeNode{Val: 3},
				},
			},
			want: []int{1, 3, 2},
		},
		{
			name: "Example 2: [1,2,3,4,5,null,8,null,null,6,7,9]",
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
				Right: &TreeNode{
					Val: 3,
					Right: &TreeNode{
						Val:  8,
						Left: &TreeNode{Val: 9},
					},
				},
			},
			want: []int{4, 2, 6, 5, 7, 1, 3, 9, 8},
		},
		{
			name: "Example 3: empty tree",
			root: nil,
			want: nil,
		},
		{
			name: "Example 4: single node",
			root: &TreeNode{Val: 1},
			want: []int{1},
		},
		{
			name: "left skewed tree",
			root: &TreeNode{
				Val: 3,
				Left: &TreeNode{
					Val:  2,
					Left: &TreeNode{Val: 1},
				},
			},
			want: []int{1, 2, 3},
		},
		{
			name: "right skewed tree",
			root: &TreeNode{
				Val: 1,
				Right: &TreeNode{
					Val:   2,
					Right: &TreeNode{Val: 3},
				},
			},
			want: []int{1, 2, 3},
		},
		{
			name: "complete binary tree",
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
			want: []int{1, 2, 3, 4, 5, 6, 7},
		},
		{
			name: "tree with negative values",
			root: &TreeNode{
				Val:   0,
				Left:  &TreeNode{Val: -100},
				Right: &TreeNode{Val: 100},
			},
			want: []int{-100, 0, 100},
		},
		{
			name: "tree with duplicate values",
			root: &TreeNode{
				Val: 2,
				Left: &TreeNode{
					Val:  2,
					Left: &TreeNode{Val: 2},
				},
				Right: &TreeNode{Val: 2},
			},
			want: []int{2, 2, 2, 2},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := inorderTraversal(tt.root)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("inorderTraversal() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestInorderTraversalEdgeCases(t *testing.T) {
	t.Run("only left child", func(t *testing.T) {
		root := &TreeNode{
			Val:  1,
			Left: &TreeNode{Val: 2},
		}
		want := []int{2, 1}
		got := inorderTraversal(root)
		if !reflect.DeepEqual(got, want) {
			t.Errorf("inorderTraversal() = %v, want %v", got, want)
		}
	})

	t.Run("only right child", func(t *testing.T) {
		root := &TreeNode{
			Val:   1,
			Right: &TreeNode{Val: 2},
		}
		want := []int{1, 2}
		got := inorderTraversal(root)
		if !reflect.DeepEqual(got, want) {
			t.Errorf("inorderTraversal() = %v, want %v", got, want)
		}
	})

	t.Run("maximum depth with minimum values", func(t *testing.T) {
		root := &TreeNode{
			Val: -100,
			Left: &TreeNode{
				Val:  -100,
				Left: &TreeNode{Val: -100},
			},
		}
		want := []int{-100, -100, -100}
		got := inorderTraversal(root)
		if !reflect.DeepEqual(got, want) {
			t.Errorf("inorderTraversal() = %v, want %v", got, want)
		}
	})
}
