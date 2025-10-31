package constructquadtree

import (
	"testing"
)

func TestConstruct(t *testing.T) {
	tests := []struct {
		name string
		grid [][]int
		want *Node
	}{
		{
			name: "Example 1: 2x2 mixed grid",
			grid: [][]int{
				{0, 1},
				{1, 0},
			},
			want: &Node{
				IsLeaf: false,
				Val:    true,
				TopLeft: &Node{
					IsLeaf: true,
					Val:    false,
				},
				TopRight: &Node{
					IsLeaf: true,
					Val:    true,
				},
				BottomLeft: &Node{
					IsLeaf: true,
					Val:    true,
				},
				BottomRight: &Node{
					IsLeaf: true,
					Val:    false,
				},
			},
		},
		{
			name: "All ones 2x2",
			grid: [][]int{
				{1, 1},
				{1, 1},
			},
			want: &Node{
				IsLeaf: true,
				Val:    true,
			},
		},
		{
			name: "All zeros 2x2",
			grid: [][]int{
				{0, 0},
				{0, 0},
			},
			want: &Node{
				IsLeaf: true,
				Val:    false,
			},
		},
		{
			name: "Single cell - 1",
			grid: [][]int{
				{1},
			},
			want: &Node{
				IsLeaf: true,
				Val:    true,
			},
		},
		{
			name: "Single cell - 0",
			grid: [][]int{
				{0},
			},
			want: &Node{
				IsLeaf: true,
				Val:    false,
			},
		},
		{
			name: "4x4 all ones",
			grid: [][]int{
				{1, 1, 1, 1},
				{1, 1, 1, 1},
				{1, 1, 1, 1},
				{1, 1, 1, 1},
			},
			want: &Node{
				IsLeaf: true,
				Val:    true,
			},
		},
		{
			name: "4x4 mixed - top half ones, bottom half zeros",
			grid: [][]int{
				{1, 1, 1, 1},
				{1, 1, 1, 1},
				{0, 0, 0, 0},
				{0, 0, 0, 0},
			},
			want: &Node{
				IsLeaf: false,
				Val:    true,
				TopLeft: &Node{
					IsLeaf: true,
					Val:    true,
				},
				TopRight: &Node{
					IsLeaf: true,
					Val:    true,
				},
				BottomLeft: &Node{
					IsLeaf: true,
					Val:    false,
				},
				BottomRight: &Node{
					IsLeaf: true,
					Val:    false,
				},
			},
		},
		{
			name: "4x4 checkerboard pattern in quadrants",
			grid: [][]int{
				{1, 1, 0, 0},
				{1, 1, 0, 0},
				{0, 0, 1, 1},
				{0, 0, 1, 1},
			},
			want: &Node{
				IsLeaf: false,
				Val:    true,
				TopLeft: &Node{
					IsLeaf: true,
					Val:    true,
				},
				TopRight: &Node{
					IsLeaf: true,
					Val:    false,
				},
				BottomLeft: &Node{
					IsLeaf: true,
					Val:    false,
				},
				BottomRight: &Node{
					IsLeaf: true,
					Val:    true,
				},
			},
		},
		{
			name: "Example 2: 8x8 complex grid",
			grid: [][]int{
				{1, 1, 1, 1, 0, 0, 0, 0},
				{1, 1, 1, 1, 0, 0, 0, 0},
				{1, 1, 1, 1, 1, 1, 1, 1},
				{1, 1, 1, 1, 1, 1, 1, 1},
				{1, 1, 1, 1, 0, 0, 0, 0},
				{1, 1, 1, 1, 0, 0, 0, 0},
				{1, 1, 1, 1, 0, 0, 0, 0},
				{1, 1, 1, 1, 0, 0, 0, 0},
			},
			want: &Node{
				IsLeaf: false,
				Val:    true,
				TopLeft: &Node{
					IsLeaf: true,
					Val:    true,
				},
				TopRight: &Node{
					IsLeaf: false,
					Val:    true,
					TopLeft: &Node{
						IsLeaf: true,
						Val:    false,
					},
					TopRight: &Node{
						IsLeaf: true,
						Val:    false,
					},
					BottomLeft: &Node{
						IsLeaf: true,
						Val:    true,
					},
					BottomRight: &Node{
						IsLeaf: true,
						Val:    true,
					},
				},
				BottomLeft: &Node{
					IsLeaf: true,
					Val:    true,
				},
				BottomRight: &Node{
					IsLeaf: true,
					Val:    false,
				},
			},
		},
		{
			name: "4x4 all different values (checkerboard)",
			grid: [][]int{
				{0, 1, 0, 1},
				{1, 0, 1, 0},
				{0, 1, 0, 1},
				{1, 0, 1, 0},
			},
			want: &Node{
				IsLeaf: false,
				Val:    true,
				TopLeft: &Node{
					IsLeaf: false,
					Val:    true,
					TopLeft: &Node{
						IsLeaf: true,
						Val:    false,
					},
					TopRight: &Node{
						IsLeaf: true,
						Val:    true,
					},
					BottomLeft: &Node{
						IsLeaf: true,
						Val:    true,
					},
					BottomRight: &Node{
						IsLeaf: true,
						Val:    false,
					},
				},
				TopRight: &Node{
					IsLeaf: false,
					Val:    true,
					TopLeft: &Node{
						IsLeaf: true,
						Val:    false,
					},
					TopRight: &Node{
						IsLeaf: true,
						Val:    true,
					},
					BottomLeft: &Node{
						IsLeaf: true,
						Val:    true,
					},
					BottomRight: &Node{
						IsLeaf: true,
						Val:    false,
					},
				},
				BottomLeft: &Node{
					IsLeaf: false,
					Val:    true,
					TopLeft: &Node{
						IsLeaf: true,
						Val:    false,
					},
					TopRight: &Node{
						IsLeaf: true,
						Val:    true,
					},
					BottomLeft: &Node{
						IsLeaf: true,
						Val:    true,
					},
					BottomRight: &Node{
						IsLeaf: true,
						Val:    false,
					},
				},
				BottomRight: &Node{
					IsLeaf: false,
					Val:    true,
					TopLeft: &Node{
						IsLeaf: true,
						Val:    false,
					},
					TopRight: &Node{
						IsLeaf: true,
						Val:    true,
					},
					BottomLeft: &Node{
						IsLeaf: true,
						Val:    true,
					},
					BottomRight: &Node{
						IsLeaf: true,
						Val:    false,
					},
				},
			},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := construct(tt.grid)
			if !equalNodes(got, tt.want) {
				t.Errorf("construct() = %v, want %v", serializeNode(got), serializeNode(tt.want))
			}
		})
	}
}

func TestBuild(t *testing.T) {
	tests := []struct {
		name string
		grid [][]int
		i    int
		j    int
		size int
		want *Node
	}{
		{
			name: "Build from subgrid - top left 2x2 of 4x4",
			grid: [][]int{
				{1, 1, 0, 0},
				{1, 1, 0, 0},
				{0, 0, 1, 1},
				{0, 0, 1, 1},
			},
			i:    0,
			j:    0,
			size: 2,
			want: &Node{
				IsLeaf: true,
				Val:    true,
			},
		},
		{
			name: "Build from subgrid - bottom right 2x2 of 4x4",
			grid: [][]int{
				{1, 1, 0, 0},
				{1, 1, 0, 0},
				{0, 0, 1, 1},
				{0, 0, 1, 1},
			},
			i:    2,
			j:    2,
			size: 2,
			want: &Node{
				IsLeaf: true,
				Val:    true,
			},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := build(tt.grid, tt.i, tt.j, tt.size)
			if !equalNodes(got, tt.want) {
				t.Errorf("build() = %v, want %v", serializeNode(got), serializeNode(tt.want))
			}
		})
	}
}

func TestSamenumb(t *testing.T) {
	tests := []struct {
		name string
		grid [][]int
		row  int
		col  int
		size int
		want bool
	}{
		{
			name: "All ones in 2x2",
			grid: [][]int{
				{1, 1},
				{1, 1},
			},
			row:  0,
			col:  0,
			size: 2,
			want: true,
		},
		{
			name: "All zeros in 2x2",
			grid: [][]int{
				{0, 0},
				{0, 0},
			},
			row:  0,
			col:  0,
			size: 2,
			want: true,
		},
		{
			name: "Mixed values in 2x2",
			grid: [][]int{
				{0, 1},
				{1, 0},
			},
			row:  0,
			col:  0,
			size: 2,
			want: false,
		},
		{
			name: "Single cell - 1",
			grid: [][]int{
				{1},
			},
			row:  0,
			col:  0,
			size: 1,
			want: true,
		},
		{
			name: "Subgrid top-left 2x2 of 4x4 - all ones",
			grid: [][]int{
				{1, 1, 0, 0},
				{1, 1, 0, 0},
				{0, 0, 1, 1},
				{0, 0, 1, 1},
			},
			row:  0,
			col:  0,
			size: 2,
			want: true,
		},
		{
			name: "Subgrid top-right 2x2 of 4x4 - all zeros",
			grid: [][]int{
				{1, 1, 0, 0},
				{1, 1, 0, 0},
				{0, 0, 1, 1},
				{0, 0, 1, 1},
			},
			row:  0,
			col:  2,
			size: 2,
			want: true,
		},
		{
			name: "Full 4x4 grid - mixed",
			grid: [][]int{
				{1, 1, 0, 0},
				{1, 1, 0, 0},
				{0, 0, 1, 1},
				{0, 0, 1, 1},
			},
			row:  0,
			col:  0,
			size: 4,
			want: false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := samenumb(tt.grid, tt.row, tt.col, tt.size); got != tt.want {
				t.Errorf("samenumb() = %v, want %v", got, tt.want)
			}
		})
	}
}

// Helper function to compare two quad trees
func equalNodes(a, b *Node) bool {
	if a == nil && b == nil {
		return true
	}
	if a == nil || b == nil {
		return false
	}
	if a.IsLeaf != b.IsLeaf || a.Val != b.Val {
		return false
	}
	if a.IsLeaf {
		return true
	}
	return equalNodes(a.TopLeft, b.TopLeft) &&
		equalNodes(a.TopRight, b.TopRight) &&
		equalNodes(a.BottomLeft, b.BottomLeft) &&
		equalNodes(a.BottomRight, b.BottomRight)
}

// Helper function to serialize node for debugging
func serializeNode(n *Node) []interface{} {
	if n == nil {
		return []interface{}{nil}
	}
	result := []interface{}{[]int{boolToInt(n.IsLeaf), boolToInt(n.Val)}}
	if !n.IsLeaf {
		result = append(result, serializeNode(n.TopLeft)...)
		result = append(result, serializeNode(n.TopRight)...)
		result = append(result, serializeNode(n.BottomLeft)...)
		result = append(result, serializeNode(n.BottomRight)...)
	}
	return result
}

func boolToInt(b bool) int {
	if b {
		return 1
	}
	return 0
}
