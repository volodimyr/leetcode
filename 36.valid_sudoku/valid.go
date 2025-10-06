// 36. Valid Sudoku
// Topics: 'Array', 'Hash Table', 'Matrix'
// Level: 'Medium'

// Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

//     Each row must contain the digits 1-9 without repetition.
//     Each column must contain the digits 1-9 without repetition.
//     Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

// Note:

//     A Sudoku board (partially filled) could be valid but is not necessarily solvable.
//     Only the filled cells need to be validated according to the mentioned rules.

// Example 1:

// Input: board =
// [["5","3",".",".","7",".",".",".","."]
// ,["6",".",".","1","9","5",".",".","."]
// ,[".","9","8",".",".",".",".","6","."]
// ,["8",".",".",".","6",".",".",".","3"]
// ,["4",".",".","8",".","3",".",".","1"]
// ,["7",".",".",".","2",".",".",".","6"]
// ,[".","6",".",".",".",".","2","8","."]
// ,[".",".",".","4","1","9",".",".","5"]
// ,[".",".",".",".","8",".",".","7","9"]]
// Output: true

// Example 2:

// Input: board =
// [["8","3",".",".","7",".",".",".","."]
// ,["6",".",".","1","9","5",".",".","."]
// ,[".","9","8",".",".",".",".","6","."]
// ,["8",".",".",".","6",".",".",".","3"]
// ,["4",".",".","8",".","3",".",".","1"]
// ,["7",".",".",".","2",".",".",".","6"]
// ,[".","6",".",".",".",".","2","8","."]
// ,[".",".",".","4","1","9",".",".","5"]
// ,[".",".",".",".","8",".",".","7","9"]]
// Output: false
// Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

// Constraints:

//     board.length == 9
//     board[i].length == 9
//     board[i][j] is a digit 1-9 or '.'.

package validsudoku

func isValidSudoku(board [][]byte) bool {
	for row := range len(board) {
		if !valid(board[row]) {
			return false
		}
	}
	for col := range len(board) {
		if !valid(extractcol(col, board)) {
			return false
		}
	}

	for i := 0; i <= len(board)-3; i += 3 {
		for j := 0; j <= len(board[i])-3; j += 3 {
			if !valid(extractbox(i, j, board)) {
				return false
			}
		}
	}

	return true
}

func extractbox(row, col int, board [][]byte) []byte {
	arr := make([]byte, 9)
	var index int
	for i := row; i < row+3; i++ {
		for j := col; j < col+3; j++ {
			arr[index] = board[i][j]
			index++
		}
	}
	return arr
}

func extractcol(col int, board [][]byte) []byte {
	arr := make([]byte, len(board))
	for i := range len(board) {
		arr[i] = board[i][col]
	}
	return arr
}

func valid(arr []byte) bool {
	counter := make([]int, 10)
	for _, a := range arr {
		if a == '.' {
			continue
		}
		id := a - '0'
		c := counter[id]
		if c > 0 {
			return false
		}
		counter[id]++
	}
	return true
}
