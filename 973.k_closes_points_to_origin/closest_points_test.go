package kclosespointstoorigin

import (
	"sort"
	"testing"
)

func TestKClosest(t *testing.T) {
	tests := []struct {
		name   string
		points [][]int
		k      int
		want   [][]int
	}{
		{
			name:   "example 1",
			points: [][]int{{1, 3}, {-2, 2}},
			k:      1,
			want:   [][]int{{-2, 2}},
		},
		{
			name:   "example 2",
			points: [][]int{{3, 3}, {5, -1}, {-2, 4}},
			k:      2,
			want:   [][]int{{3, 3}, {-2, 4}},
		},
		{
			name:   "single point",
			points: [][]int{{1, 1}},
			k:      1,
			want:   [][]int{{1, 1}},
		},
		{
			name:   "k equals length",
			points: [][]int{{1, 3}, {-2, 2}},
			k:      2,
			want:   [][]int{{1, 3}, {-2, 2}},
		},
		{
			name:   "origin included",
			points: [][]int{{0, 0}, {1, 1}, {2, 2}},
			k:      1,
			want:   [][]int{{0, 0}},
		},
		{
			name:   "origin included k=2",
			points: [][]int{{0, 0}, {1, 1}, {2, 2}},
			k:      2,
			want:   [][]int{{0, 0}, {1, 1}},
		},
		{
			name:   "all same distance",
			points: [][]int{{1, 0}, {0, 1}, {-1, 0}, {0, -1}},
			k:      2,
			want:   [][]int{{1, 0}, {0, 1}},
		},
		{
			name:   "negative coordinates",
			points: [][]int{{-5, -5}, {-3, -3}, {-1, -1}},
			k:      1,
			want:   [][]int{{-1, -1}},
		},
		{
			name:   "mixed coordinates ascending distance",
			points: [][]int{{1, 1}, {2, 2}, {3, 3}, {4, 4}},
			k:      2,
			want:   [][]int{{1, 1}, {2, 2}},
		},
		{
			name:   "mixed coordinates descending distance",
			points: [][]int{{4, 4}, {3, 3}, {2, 2}, {1, 1}},
			k:      2,
			want:   [][]int{{1, 1}, {2, 2}},
		},
		{
			name:   "larger k value",
			points: [][]int{{1, 1}, {2, 2}, {3, 3}, {4, 4}, {5, 5}},
			k:      3,
			want:   [][]int{{1, 1}, {2, 2}, {3, 3}},
		},
		{
			name:   "random order",
			points: [][]int{{3, 3}, {1, 1}, {4, 4}, {2, 2}},
			k:      2,
			want:   [][]int{{1, 1}, {2, 2}},
		},
		{
			name:   "pythagorean triples",
			points: [][]int{{3, 4}, {5, 12}, {8, 15}, {1, 0}},
			k:      2,
			want:   [][]int{{1, 0}, {3, 4}},
		},
		{
			name:   "many points k=1",
			points: [][]int{{10, 10}, {9, 9}, {8, 8}, {7, 7}, {6, 6}, {5, 5}, {4, 4}, {3, 3}, {2, 2}, {1, 1}},
			k:      1,
			want:   [][]int{{1, 1}},
		},
		{
			name:   "many points k=5",
			points: [][]int{{10, 10}, {9, 9}, {8, 8}, {7, 7}, {6, 6}, {5, 5}, {4, 4}, {3, 3}, {2, 2}, {1, 1}},
			k:      5,
			want:   [][]int{{1, 1}, {2, 2}, {3, 3}, {4, 4}, {5, 5}},
		},
		{
			name:   "heap replacement needed",
			points: [][]int{{5, 5}, {4, 4}, {3, 3}, {1, 1}},
			k:      2,
			want:   [][]int{{1, 1}, {3, 3}},
		},
		{
			name:   "large then small values",
			points: [][]int{{100, 100}, {50, 50}, {10, 10}, {1, 1}},
			k:      2,
			want:   [][]int{{1, 1}, {10, 10}},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			pointsCopy := make([][]int, len(tt.points))
			for i := range tt.points {
				pointsCopy[i] = make([]int, len(tt.points[i]))
				copy(pointsCopy[i], tt.points[i])
			}

			got := kClosest(pointsCopy, tt.k)

			if len(got) != len(tt.want) {
				t.Errorf("kClosest() returned %d points, want %d", len(got), len(tt.want))
				return
			}

			sortPoints := func(points [][]int) {
				sort.Slice(points, func(i, j int) bool {
					di := distance(points[i])
					dj := distance(points[j])
					if di != dj {
						return di < dj
					}
					if points[i][0] != points[j][0] {
						return points[i][0] < points[j][0]
					}
					return points[i][1] < points[j][1]
				})
			}

			sortPoints(got)
			sortPoints(tt.want)

			for i := range got {
				if got[i][0] != tt.want[i][0] || got[i][1] != tt.want[i][1] {
					t.Errorf("kClosest() result mismatch at index %d: got %v, want %v", i, got[i], tt.want[i])
				}
			}

			for i := range got {
				maxDist := distance(got[i])
				for j := range tt.points {
					pointInResult := false
					for k := range got {
						if got[k][0] == tt.points[j][0] && got[k][1] == tt.points[j][1] {
							pointInResult = true
							break
						}
					}
					if !pointInResult {
						dist := distance(tt.points[j])
						if dist < maxDist {
							t.Errorf("kClosest() included point %v (distance %d) but excluded closer point %v (distance %d)",
								got[i], maxDist, tt.points[j], dist)
						}
					}
				}
			}
		})
	}
}
