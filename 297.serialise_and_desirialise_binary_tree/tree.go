// 297. Serialize and Deserialize Binary Tree
// Topics: 'String', 'Tree', 'Depth-First Search', 'Breadth-First Search', 'Design', 'Binary Tree'
// Level: 'Medium'

// Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

// Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

// Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

// Example 1:

// Input: root = [1,2,3,null,null,4,5]
// Output: [1,2,3,null,null,4,5]

// Example 2:

// Input: root = []
// Output: []

// Constraints:

//     The number of nodes in the tree is in the range [0, 104].
//     -1000 <= Node.val <= 1000

package serialiseanddesirialisebinarytree

import (
	"strconv"
	"strings"
)

type Codec struct {
}

func Constructor() Codec {
	return Codec{}
}

func (c *Codec) serialize(root *TreeNode) string {
	var b strings.Builder
	q := []*TreeNode{}
	q = append(q, root)

	for len(q) != 0 {
		node := q[0]
		q = q[1:]
		if b.Len() > 0 {
			b.WriteString(",")
		}
		if node != nil {
			b.WriteString(strconv.Itoa(node.Val))
			q = append(q, node.Left)
			q = append(q, node.Right)
		} else {
			b.WriteString("nil")
		}

	}
	return b.String()
}

func (c *Codec) deserialize(data string) *TreeNode {
	var root *TreeNode
	stream, ok := newStream(data)
	if !ok {
		return root
	}
	root = stream.next()
	if stream.empty() {
		return root
	}
	q := []*TreeNode{root}

	for len(q) != 0 {
		if stream.empty() {
			return root
		}
		node := q[0]
		q = q[1:]
		node.Left = stream.next()
		if node.Left != nil {
			q = append(q, node.Left)
		}
		if stream.empty() {
			return root
		}
		node.Right = stream.next()
		if node.Right != nil {
			q = append(q, node.Right)
		}
	}
	return root
}

type stream struct {
	arr []string
	cur int
}

func newStream(data string) (*stream, bool) {
	if len(data) == 0 {
		return nil, false
	}
	arr := strings.Split(data, ",")
	if len(arr) == 0 {
		return nil, false
	}
	return &stream{
		arr: arr,
		cur: 0,
	}, true
}

func (s *stream) empty() bool {
	return s.cur == len(s.arr)
}

func (s *stream) next() *TreeNode {
	data := s.arr[s.cur]
	s.cur++
	return s.node(data)
}

func (s *stream) node(data string) *TreeNode {
	if data == "nil" {
		return nil
	}
	v, _ := strconv.Atoi(data)
	return &TreeNode{Val: v}
}

type TreeNode struct {
	Val   int
	Right *TreeNode
	Left  *TreeNode
}
