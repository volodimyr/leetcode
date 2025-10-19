package copylistwithrandompointer

import "testing"

func TestCopyRandomList(t *testing.T) {
	tests := []struct {
		name  string
		input [][]interface{}
	}{
		{
			name:  "example 1",
			input: [][]interface{}{{7, nil}, {13, 0}, {11, 4}, {10, 2}, {1, 0}},
		},
		{
			name:  "example 2",
			input: [][]interface{}{{1, 1}, {2, 1}},
		},
		{
			name:  "example 3",
			input: [][]interface{}{{3, nil}, {3, 0}, {3, nil}},
		},
		{
			name:  "empty list",
			input: [][]interface{}{},
		},
		{
			name:  "single node no random",
			input: [][]interface{}{{1, nil}},
		},
		{
			name:  "single node self random",
			input: [][]interface{}{{1, 0}},
		},
		{
			name:  "all random null",
			input: [][]interface{}{{1, nil}, {2, nil}, {3, nil}},
		},
		{
			name:  "all random to first",
			input: [][]interface{}{{1, nil}, {2, 0}, {3, 0}, {4, 0}},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			head := buildList(tt.input)
			copied := copyRandomList(head)

			if !verifyDeepCopy(head, copied, tt.input) {
				t.Errorf("Deep copy verification failed")
			}
		})
	}
}

func buildList(data [][]interface{}) *Node {
	if len(data) == 0 {
		return nil
	}

	nodes := make([]*Node, len(data))
	for i, pair := range data {
		nodes[i] = &Node{Val: pair[0].(int)}
	}

	for i := 0; i < len(nodes)-1; i++ {
		nodes[i].Next = nodes[i+1]
	}

	for i, pair := range data {
		if pair[1] != nil {
			idx := pair[1].(int)
			nodes[i].Random = nodes[idx]
		}
	}

	return nodes[0]
}

func verifyDeepCopy(original, copied *Node, data [][]interface{}) bool {
	if original == nil && copied == nil {
		return true
	}
	if original == nil || copied == nil {
		return false
	}

	origNodes := []*Node{}
	copyNodes := []*Node{}

	for cur := original; cur != nil; cur = cur.Next {
		origNodes = append(origNodes, cur)
	}

	for cur := copied; cur != nil; cur = cur.Next {
		copyNodes = append(copyNodes, cur)
	}

	if len(origNodes) != len(copyNodes) {
		return false
	}

	for i := 0; i < len(origNodes); i++ {
		if origNodes[i] == copyNodes[i] {
			return false
		}

		if origNodes[i].Val != copyNodes[i].Val {
			return false
		}
	}

	for i := 0; i < len(origNodes); i++ {
		origRandom := origNodes[i].Random
		copyRandom := copyNodes[i].Random

		if origRandom == nil && copyRandom == nil {
			continue
		}
		if origRandom == nil || copyRandom == nil {
			return false
		}

		origIdx := -1
		for j, node := range origNodes {
			if node == origRandom {
				origIdx = j
				break
			}
		}

		if origIdx == -1 {
			return false
		}

		if copyRandom != copyNodes[origIdx] {
			return false
		}

		if copyRandom == origRandom {
			return false
		}
	}

	return true
}
