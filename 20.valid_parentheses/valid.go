// 20. Valid Parentheses
// Topics: 'Stack', 'String'

// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

//     Open brackets must be closed by the same type of brackets.
//     Open brackets must be closed in the correct order.
//     Every close bracket has a corresponding open bracket of the same type.

// Example 1:

// Input: s = "()"

// Output: true

// Example 2:

// Input: s = "()[]{}"

// Output: true

// Example 3:

// Input: s = "(]"

// Output: false

// Example 4:

// Input: s = "([])"

// Output: true

// Example 5:

// Input: s = "([)]"

// Output: false

package validparentheses

import "github.com/volodimyr/leetcode/ds"

var ps = map[rune]rune{
	')': '(',
	']': '[',
	'}': '{',
}

func isValid(s string) bool {
	stack := &ds.Stack[rune]{}
	for _, r := range s {
		if r == '(' || r == '{' || r == '[' {
			stack.Push(r)
			continue
		}
		if ps[r] != stack.Pop() {
			return false
		}
	}
	return stack.Empty()
}
