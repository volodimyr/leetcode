package binarytreelevelordertraversal

import (
	"reflect"
	"testing"
)

func TestLevelOrder(t *testing.T) {
	tests := []struct {
		name string
		root *TreeNode
		want [][]int
	}{
		{
			name: "example 1: tree with three levels",
			root: &TreeNode{
				Val:  3,
				Left: &TreeNode{Val: 9},
				Right: &TreeNode{
					Val:   20,
					Left:  &TreeNode{Val: 15},
					Right: &TreeNode{Val: 7},
				},
			},
			want: [][]int{{3}, {9, 20}, {15, 7}},
		},
		{
			name: "example 2: single node",
			root: &TreeNode{Val: 1},
			want: [][]int{{1}},
		},
		{
			name: "example 3: empty tree",
			root: nil,
			want: [][]int{},
		},
		{
			name: "left skewed tree",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:  2,
					Left: &TreeNode{Val: 3},
				},
			},
			want: [][]int{{1}, {2}, {3}},
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
			want: [][]int{{1}, {2}, {3}},
		},
		{
			name: "complete binary tree",
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
			want: [][]int{{1}, {2, 3}, {4, 5, 6, 7}},
		},
		{
			name: "tree with negative values",
			root: &TreeNode{
				Val:   -1,
				Left:  &TreeNode{Val: -2},
				Right: &TreeNode{Val: -3},
			},
			want: [][]int{{-1}, {-2, -3}},
		},
		{
			name: "tree with mixed positive and negative values",
			root: &TreeNode{
				Val:   0,
				Left:  &TreeNode{Val: -1000},
				Right: &TreeNode{Val: 1000},
			},
			want: [][]int{{0}, {-1000, 1000}},
		},
		{
			name: "unbalanced tree with only left children at second level",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:  2,
					Left: &TreeNode{Val: 4},
				},
				Right: &TreeNode{
					Val:  3,
					Left: &TreeNode{Val: 5},
				},
			},
			want: [][]int{{1}, {2, 3}, {4, 5}},
		},
		{
			name: "two level tree with one child each",
			root: &TreeNode{
				Val:  10,
				Left: &TreeNode{Val: 20},
			},
			want: [][]int{{10}, {20}},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := levelOrder(tt.root)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("levelOrder() = %v, want %v", got, tt.want)
			}
		})
	}
}
