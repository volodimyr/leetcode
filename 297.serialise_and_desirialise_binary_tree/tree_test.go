package serialiseanddesirialisebinarytree

import (
	"testing"
)

func TestDeserialize(t *testing.T) {
	c := Constructor()

	tests := []struct {
		name string
		data string
	}{
		{
			name: "empty tree",
			data: "nil",
		},
		{
			name: "single node",
			data: "1,nil,nil",
		},
		{
			name: "complete binary tree",
			data: "1,2,3,nil,nil,nil,nil",
		},
		{
			name: "left skewed tree",
			data: "1,2,nil,3,nil,nil,nil",
		},
		{
			name: "right skewed tree",
			data: "1,nil,2,nil,3,nil,nil",
		},
		{
			name: "example 1 from problem",
			data: "1,2,3,nil,nil,4,5,nil,nil,nil,nil",
		},
		{
			name: "tree with negative values",
			data: "-1,-2,-3,nil,nil,nil,nil",
		},
		{
			name: "tree with mixed positive and negative",
			data: "0,-1000,1000,nil,nil,nil,nil",
		},
		{
			name: "complex tree with nulls",
			data: "5,3,7,nil,4,6,nil,nil,nil,nil,nil",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := c.deserialize(tt.data)
			serialized := c.serialize(result)
			if serialized != tt.data {
				t.Errorf("deserialize() then serialize() = %v, want %v", serialized, tt.data)
			}
		})
	}
}

func TestSerializeDeserialize(t *testing.T) {
	c := Constructor()

	tests := []struct {
		name string
		root *TreeNode
	}{
		{
			name: "empty tree",
			root: nil,
		},
		{
			name: "single node",
			root: &TreeNode{Val: 1},
		},
		{
			name: "complete binary tree",
			root: &TreeNode{
				Val:   1,
				Left:  &TreeNode{Val: 2},
				Right: &TreeNode{Val: 3},
			},
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
		},
		{
			name: "example 1 from problem",
			root: &TreeNode{
				Val:  1,
				Left: &TreeNode{Val: 2},
				Right: &TreeNode{
					Val:   3,
					Left:  &TreeNode{Val: 4},
					Right: &TreeNode{Val: 5},
				},
			},
		},
		{
			name: "tree with negative values",
			root: &TreeNode{
				Val:   -1,
				Left:  &TreeNode{Val: -2},
				Right: &TreeNode{Val: -3},
			},
		},
		{
			name: "tree with mixed positive and negative",
			root: &TreeNode{
				Val:   0,
				Left:  &TreeNode{Val: -1000},
				Right: &TreeNode{Val: 1000},
			},
		},
		{
			name: "complex tree with nulls",
			root: &TreeNode{
				Val: 5,
				Left: &TreeNode{
					Val:   3,
					Right: &TreeNode{Val: 4},
				},
				Right: &TreeNode{
					Val:  7,
					Left: &TreeNode{Val: 6},
				},
			},
		},
		{
			name: "large tree",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val:   4,
						Left:  &TreeNode{Val: 8},
						Right: &TreeNode{Val: 9},
					},
					Right: &TreeNode{
						Val:   5,
						Left:  &TreeNode{Val: 10},
						Right: &TreeNode{Val: 11},
					},
				},
				Right: &TreeNode{
					Val: 3,
					Left: &TreeNode{
						Val:   6,
						Left:  &TreeNode{Val: 12},
						Right: &TreeNode{Val: 13},
					},
					Right: &TreeNode{
						Val:   7,
						Left:  &TreeNode{Val: 14},
						Right: &TreeNode{Val: 15},
					},
				},
			},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			serialized := c.serialize(tt.root)
			deserialized := c.deserialize(serialized)
			reSerialized := c.serialize(deserialized)
			if serialized != reSerialized {
				t.Errorf("serialize-deserialize-serialize mismatch: got %v, want %v", reSerialized, serialized)
			}
		})
	}
}

func TestDeserializeEdgeCases(t *testing.T) {
	c := Constructor()

	tests := []struct {
		name     string
		data     string
		expected string
	}{
		{
			name:     "empty string handled",
			data:     "",
			expected: "nil",
		},
		{
			name:     "boundary value positive",
			data:     "1000,nil,nil",
			expected: "1000,nil,nil",
		},
		{
			name:     "boundary value negative",
			data:     "-1000,nil,nil",
			expected: "-1000,nil,nil",
		},
		{
			name:     "zero value",
			data:     "0,nil,nil",
			expected: "0,nil,nil",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := c.deserialize(tt.data)
			serialized := c.serialize(result)
			if serialized != tt.expected {
				t.Errorf("deserialize(%v) = %v, want %v", tt.data, serialized, tt.expected)
			}
		})
	}
}

func TestSerialize(t *testing.T) {
	c := Constructor()

	tests := []struct {
		name     string
		root     *TreeNode
		expected string
	}{
		{
			name:     "empty tree",
			root:     nil,
			expected: "nil",
		},
		{
			name:     "single node",
			root:     &TreeNode{Val: 1},
			expected: "1,nil,nil",
		},
		{
			name: "complete binary tree",
			root: &TreeNode{
				Val:   1,
				Left:  &TreeNode{Val: 2},
				Right: &TreeNode{Val: 3},
			},
			expected: "1,2,3,nil,nil,nil,nil",
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
			expected: "1,2,nil,3,nil,nil,nil",
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
			expected: "1,nil,2,nil,3,nil,nil",
		},
		{
			name: "example 1 from problem",
			root: &TreeNode{
				Val:  1,
				Left: &TreeNode{Val: 2},
				Right: &TreeNode{
					Val:   3,
					Left:  &TreeNode{Val: 4},
					Right: &TreeNode{Val: 5},
				},
			},
			expected: "1,2,3,nil,nil,4,5,nil,nil,nil,nil",
		},
		{
			name: "tree with negative values",
			root: &TreeNode{
				Val:   -1,
				Left:  &TreeNode{Val: -2},
				Right: &TreeNode{Val: -3},
			},
			expected: "-1,-2,-3,nil,nil,nil,nil",
		},
		{
			name: "tree with mixed positive and negative",
			root: &TreeNode{
				Val:   0,
				Left:  &TreeNode{Val: -1000},
				Right: &TreeNode{Val: 1000},
			},
			expected: "0,-1000,1000,nil,nil,nil,nil",
		},
		{
			name: "complex tree with nulls",
			root: &TreeNode{
				Val: 5,
				Left: &TreeNode{
					Val:   3,
					Right: &TreeNode{Val: 4},
				},
				Right: &TreeNode{
					Val:  7,
					Left: &TreeNode{Val: 6},
				},
			},
			expected: "5,3,7,nil,4,6,nil,nil,nil,nil,nil",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := c.serialize(tt.root)
			if result != tt.expected {
				t.Errorf("serialize() = %v, want %v", result, tt.expected)
			}
		})
	}
}
