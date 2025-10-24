package pathsum

import "testing"

func node(v int, l, r *TreeNode) *TreeNode {
	return &TreeNode{Val: v, Left: l, Right: r}
}

func TestHasPathSum(t *testing.T) {
	tests := []struct {
		name      string
		root      *TreeNode
		targetSum int
		want      bool
	}{
		{
			name: "example1",
			/*
				        5
				       / \
				      4   8
				     /   / \
				    11  13  4
				   /  \      \
				  7    2      1

				Paths include:
				5->4->11->7  (27)
				5->4->11->2  (22) <- target
				5->8->13     (26)
				5->8->4->1   (18)
			*/
			root: node(5,
				node(4,
					node(11,
						node(7, nil, nil),
						node(2, nil, nil),
					),
					nil,
				),
				node(8,
					node(13, nil, nil),
					node(4,
						nil,
						node(1, nil, nil),
					),
				),
			),
			targetSum: 22,
			want:      true,
		},
		{
			name: "example2",
			/*
				    1
				   / \
				  2   3

				Paths:
				1->2 (3)
				1->3 (4)
			*/
			root: node(1,
				node(2, nil, nil),
				node(3, nil, nil),
			),
			targetSum: 5,
			want:      false,
		},
		{
			name: "empty tree",
			/*
				(empty)
			*/
			root:      nil,
			targetSum: 0,
			want:      false,
		},
		{
			name: "single node equals target",
			/*
			  7
			*/
			root:      node(7, nil, nil),
			targetSum: 7,
			want:      true,
		},
		{
			name: "single node not equal target",
			/*
			  7
			*/
			root:      node(7, nil, nil),
			targetSum: 5,
			want:      false,
		},
		{
			name: "multiple paths only one valid",
			/*
				    1
				   / \
				  2   3
				     /
				    4

				Paths:
				1->2 (3)
				1->3->4 (8) <- target
			*/
			root: node(1,
				node(2, nil, nil),
				node(3,
					node(4, nil, nil),
					nil,
				),
			),
			targetSum: 1 + 3 + 4,
			want:      true,
		},
		{
			name: "no valid paths",
			/*
				    1
				   / \
				  2   3

				No root-to-leaf path sums to 100.
			*/
			root: node(1,
				node(2, nil, nil),
				node(3, nil, nil),
			),
			targetSum: 100,
			want:      false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := hasPathSum(tt.root, tt.targetSum)
			if got != tt.want {
				t.Fatalf("hasPathSum() = %v, want %v", got, tt.want)
			}
		})
	}
}
