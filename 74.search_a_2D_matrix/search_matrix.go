// 74. Search a 2D matrix
// Topics: 'Array', 'Binary Search', 'Matrix'

// You are given an m x n integer matrix matrix with the following two properties:

//     Each row is sorted in non-decreasing order.
//     The first integer of each row is greater than the last integer of the previous row.

// Given an integer target, return true if target is in matrix or false otherwise.

// You must write a solution in O(log(m * n)) time complexity.

// Example 1:

// Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
// Output: true

// Example 2:

// Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
// Output: false

// Constraints:

//     m == matrix.length
//     n == matrix[i].length
//     1 <= m, n <= 100
//     -104 <= matrix[i][j], target <= 104

package searcha2dmatrix

func searchMatrix(matrix [][]int, target int) bool {
	rows, columns := len(matrix), len(matrix[0])

	low, high := 0, rows*columns-1

	for low <= high {
		mid := low + (high-low)/2
		val := matrix[mid/columns][mid%columns]
		if val == target {
			return true
		}
		if val > target {
			high = mid - 1
		} else {
			low = mid + 1
		}
	}
	return false
}

// O(m + log n) solution, not optiomal
// func searchMatrix(matrix [][]int, target int) bool {
// 	for i := 0; i < len(matrix); i++ {
// 		if matrix[i][len(matrix[i])-1] < target {
// 			continue
// 		}
// 		return search(matrix[i], target, 0, len(matrix[i])-1)
// 	}
// 	return false
// }

// func search(numbers []int, t, s, e int) bool {
// 	for s <= e {
// 		m := s + (e-s)/2
// 		if numbers[m] == t {
// 			return true
// 		}
// 		if numbers[m] < t {
// 			s = m + 1
// 		} else {
// 			e = m - 1
// 		}
// 	}
// 	return false
// }
