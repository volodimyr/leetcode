package lowestcommonancestorofabinarysearchtree

import "testing"

func TestLowestCommonAncestor(t *testing.T) {
	tests := []struct {
		name     string
		root     *TreeNode
		p        *TreeNode
		q        *TreeNode
		expected int
	}{
		{
			name: "Example 1: LCA of 2 and 8 is 6",
			//       6
			//      / \
			//     2   8
			//    / \ / \
			//   0  4 7  9
			//     / \
			//    3   5
			root: &TreeNode{
				Val: 6,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val: 0,
					},
					Right: &TreeNode{
						Val: 4,
						Left: &TreeNode{
							Val: 3,
						},
						Right: &TreeNode{
							Val: 5,
						},
					},
				},
				Right: &TreeNode{
					Val: 8,
					Left: &TreeNode{
						Val: 7,
					},
					Right: &TreeNode{
						Val: 9,
					},
				},
			},
			p:        &TreeNode{Val: 2},
			q:        &TreeNode{Val: 8},
			expected: 6,
		},
		{
			name: "Example 2: LCA of 2 and 4 is 2",
			//       6
			//      / \
			//     2   8
			//    / \ / \
			//   0  4 7  9
			//     / \
			//    3   5
			root: &TreeNode{
				Val: 6,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val: 0,
					},
					Right: &TreeNode{
						Val: 4,
						Left: &TreeNode{
							Val: 3,
						},
						Right: &TreeNode{
							Val: 5,
						},
					},
				},
				Right: &TreeNode{
					Val: 8,
					Left: &TreeNode{
						Val: 7,
					},
					Right: &TreeNode{
						Val: 9,
					},
				},
			},
			p:        &TreeNode{Val: 2},
			q:        &TreeNode{Val: 4},
			expected: 2,
		},
		{
			name: "Example 3: LCA of 2 and 1 is 2",
			//   2
			//  /
			// 1
			root: &TreeNode{
				Val: 2,
				Left: &TreeNode{
					Val: 1,
				},
			},
			p:        &TreeNode{Val: 2},
			q:        &TreeNode{Val: 1},
			expected: 2,
		},
		{
			name: "LCA of 0 and 5 is 2",
			//       6
			//      / \
			//     2   8
			//    / \ / \
			//   0  4 7  9
			//     / \
			//    3   5
			root: &TreeNode{
				Val: 6,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val: 0,
					},
					Right: &TreeNode{
						Val: 4,
						Left: &TreeNode{
							Val: 3,
						},
						Right: &TreeNode{
							Val: 5,
						},
					},
				},
				Right: &TreeNode{
					Val: 8,
					Left: &TreeNode{
						Val: 7,
					},
					Right: &TreeNode{
						Val: 9,
					},
				},
			},
			p:        &TreeNode{Val: 0},
			q:        &TreeNode{Val: 5},
			expected: 2,
		},
		{
			name: "LCA of 7 and 9 is 8",
			//       6
			//      / \
			//     2   8
			//    / \ / \
			//   0  4 7  9
			//     / \
			//    3   5
			root: &TreeNode{
				Val: 6,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val: 0,
					},
					Right: &TreeNode{
						Val: 4,
						Left: &TreeNode{
							Val: 3,
						},
						Right: &TreeNode{
							Val: 5,
						},
					},
				},
				Right: &TreeNode{
					Val: 8,
					Left: &TreeNode{
						Val: 7,
					},
					Right: &TreeNode{
						Val: 9,
					},
				},
			},
			p:        &TreeNode{Val: 7},
			q:        &TreeNode{Val: 9},
			expected: 8,
		},
		{
			name: "Small tree with two nodes",
			//  10
			//  /
			// 5
			root: &TreeNode{
				Val: 10,
				Left: &TreeNode{
					Val: 5,
				},
			},
			p:        &TreeNode{Val: 10},
			q:        &TreeNode{Val: 5},
			expected: 10,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := lowestCommonAncestor(tt.root, tt.p, tt.q)
			if result.Val != tt.expected {
				t.Errorf("expected %d, got %d", tt.expected, result.Val)
			}
		})
	}
}
