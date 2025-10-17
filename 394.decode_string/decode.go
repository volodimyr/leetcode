// 394. Decode string
// Topics: 'Recursion', 'String', 'Stack'
// Level: 'Medium'

//Given an encoded string, return its decoded string.

// The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

// You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

// The test cases are generated so that the length of the output will never exceed 105.

// Example 1:

// Input: s = "3[a]2[bc]"
// Output: "aaabcbc"

// Example 2:

// Input: s = "3[a2[c]]"
// Output: "accaccacc"

// Example 3:

// Input: s = "2[abc]3[cd]ef"
// Output: "abcabccdcdcdef"

// Constraints:

//     1 <= s.length <= 30
//     s consists of lowercase English letters, digits, and square brackets '[]'.
//     s is guaranteed to be a valid input.
//     All the integers in s are in the range [1, 300].

package decodestring

import (
	"strconv"
)

type stack struct {
	arr []string
}

func (s *stack) push(str string) {
	s.arr = append(s.arr, str)
}

func (s *stack) pop() string {
	str := s.arr[len(s.arr)-1]
	s.arr = s.arr[:len(s.arr)-1]
	return str
}

func (s *stack) empty() bool {
	return len(s.arr) == 0
}

func decodeString(str string) string {
	var expr stack
	var currentStr, currentNum string
	for i := 0; i < len(str); i++ {
		switch str[i] {
		case ']':
			num := toNumber(expr.pop())
			prevStr := expr.pop()

			var repeated string
			for range num {
				repeated += currentStr
			}
			currentStr = prevStr + repeated
		case '[':
			expr.push(currentStr)
			expr.push(currentNum)
			currentNum, currentStr = "", ""
		default:
			if numeric(str[i]) {
				currentNum += string(str[i])
			} else {
				currentStr += string(str[i])
			}
		}
	}
	return currentStr
}

func toNumber(s string) int {
	n, _ := strconv.Atoi(s)
	return n
}

func letter(b byte) bool {
	return b >= 97 && b <= 122
}

func numeric(b byte) bool {
	return b >= 48 && b <= 57
}
