package binarytreepaths

import (
	"reflect"
	"testing"
)

// quick tree builder
func node(val int, left, right *TreeNode) *TreeNode {
	return &TreeNode{Val: val, Left: left, Right: right}
}

func TestBinaryTreePaths(t *testing.T) {
	tests := []struct {
		name string
		root *TreeNode
		want []string
	}{
		{
			name: "example1",
			/*
				       1
				      / \
				     2   3
				      \
				       5
				Paths:
				1->2->5
				1->3
			*/
			root: node(1,
				node(2, nil, node(5, nil, nil)),
				node(3, nil, nil),
			),
			want: []string{"1->2->5", "1->3"},
		},
		{
			name: "single node",
			/*
				   1
				Paths:
				1
			*/
			root: node(1, nil, nil),
			want: []string{"1"},
		},
		{
			name: "left-skewed tree",
			/*
					 1
				   	|
				   2
				  |
				 3
				Paths:
				1->2->3
			*/
			root: node(1,
				node(2,
					node(3, nil, nil),
					nil,
				),
				nil,
			),
			want: []string{"1->2->3"},
		},
		{
			name: "right-skewed tree",
			/*
				1
				 \
				  2
				   \
				    3
				Paths:
				1->2->3
			*/
			root: node(1,
				nil,
				node(2,
					nil,
					node(3, nil, nil),
				),
			),
			want: []string{"1->2->3"},
		},
		{
			name: "balanced tree",
			/*
				     1
				    / \
				   2   3
				Paths:
				1->2
				1->3
			*/
			root: node(1,
				node(2, nil, nil),
				node(3, nil, nil),
			),
			want: []string{"1->2", "1->3"},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := binaryTreePaths(tt.root)
			if !reflect.DeepEqual(got, tt.want) {
				t.Fatalf("binaryTreePaths() = %v, want %v", got, tt.want)
			}
		})
	}
}
