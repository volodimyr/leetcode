package numberofstudentsunabletoeatlunch

import "testing"

func TestCountStudents(t *testing.T) {
	tests := []struct {
		name       string
		students   []int
		sandwiches []int
		want       int
	}{
		{
			name:       "all students can eat",
			students:   []int{1, 1, 0, 0},
			sandwiches: []int{0, 1, 0, 1},
			want:       0,
		},
		{
			name:       "some students cannot eat",
			students:   []int{1, 1, 1, 0, 0, 1},
			sandwiches: []int{1, 0, 0, 0, 1, 1},
			want:       3,
		},
		{
			name:       "single student can eat",
			students:   []int{0},
			sandwiches: []int{0},
			want:       0,
		},
		{
			name:       "single student cannot eat",
			students:   []int{0},
			sandwiches: []int{1},
			want:       1,
		},
		{
			name:       "all students prefer circular, all sandwiches circular",
			students:   []int{0, 0, 0, 0},
			sandwiches: []int{0, 0, 0, 0},
			want:       0,
		},
		{
			name:       "all students prefer square, all sandwiches square",
			students:   []int{1, 1, 1, 1},
			sandwiches: []int{1, 1, 1, 1},
			want:       0,
		},
		{
			name:       "all students prefer circular, all sandwiches square",
			students:   []int{0, 0, 0, 0},
			sandwiches: []int{1, 1, 1, 1},
			want:       4,
		},
		{
			name:       "all students prefer square, all sandwiches circular",
			students:   []int{1, 1, 1, 1},
			sandwiches: []int{0, 0, 0, 0},
			want:       4,
		},
		{
			name:       "two students same preference, two different sandwiches",
			students:   []int{0, 0},
			sandwiches: []int{1, 0},
			want:       2,
		},
		{
			name:       "alternating preferences matching sandwiches",
			students:   []int{0, 1, 0, 1},
			sandwiches: []int{0, 1, 0, 1},
			want:       0,
		},
		{
			name:       "one of each preference, one of each sandwich",
			students:   []int{0, 1},
			sandwiches: []int{0, 1},
			want:       0,
		},
		{
			name:       "one of each preference, reversed sandwiches",
			students:   []int{0, 1},
			sandwiches: []int{1, 0},
			want:       0,
		},
		{
			name:       "multiple rotations needed",
			students:   []int{1, 0, 1, 0},
			sandwiches: []int{0, 0, 1, 1},
			want:       0,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := countStudents(tt.students, tt.sandwiches)
			if got != tt.want {
				t.Errorf("countStudents() = %v, want %v", got, tt.want)
			}
		})
	}
}
