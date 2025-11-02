package taskscheduler

import "testing"

func TestLeastInterval(t *testing.T) {
	tests := []struct {
		name  string
		tasks []byte
		n     int
		want  int
	}{
		{
			name:  "example 1",
			tasks: []byte{'A', 'A', 'A', 'B', 'B', 'B'},
			n:     2,
			want:  8,
		},
		{
			name:  "example 2",
			tasks: []byte{'A', 'C', 'A', 'B', 'D', 'B'},
			n:     1,
			want:  6,
		},
		{
			name:  "example 3",
			tasks: []byte{'A', 'A', 'A', 'B', 'B', 'B'},
			n:     3,
			want:  10,
		},
		{
			name:  "no cooling period",
			tasks: []byte{'A', 'A', 'A', 'B', 'B', 'B'},
			n:     0,
			want:  6,
		},
		{
			name:  "single task",
			tasks: []byte{'A'},
			n:     2,
			want:  1,
		},
		{
			name:  "single task type multiple times",
			tasks: []byte{'A', 'A', 'A'},
			n:     2,
			want:  7,
		},
		{
			name:  "all different tasks",
			tasks: []byte{'A', 'B', 'C', 'D', 'E'},
			n:     2,
			want:  5,
		},
		{
			name:  "high frequency single task",
			tasks: []byte{'A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D'},
			n:     2,
			want:  16,
		},
		{
			name:  "multiple tasks with varying frequencies",
			tasks: []byte{'A', 'A', 'A', 'B', 'B', 'C'},
			n:     2,
			want:  7,
		},
		{
			name:  "large cooling period",
			tasks: []byte{'A', 'A', 'B', 'B'},
			n:     5,
			want:  8,
		},
		{
			name:  "many different tasks no idle needed",
			tasks: []byte{'A', 'B', 'C', 'D', 'E', 'F', 'A', 'B', 'C'},
			n:     2,
			want:  9,
		},
		{
			name:  "two tasks equal frequency",
			tasks: []byte{'A', 'A', 'B', 'B'},
			n:     2,
			want:  5,
		},
		{
			name:  "minimum constraint",
			tasks: []byte{'A', 'A'},
			n:     1,
			want:  3,
		},
		{
			name:  "complex pattern",
			tasks: []byte{'A', 'A', 'A', 'A', 'B', 'B', 'C', 'C', 'D'},
			n:     2,
			want:  10,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := leastInterval(tt.tasks, tt.n)
			if got != tt.want {
				t.Errorf("leastInterval() = %v, want %v", got, tt.want)
			}
		})
	}
}
