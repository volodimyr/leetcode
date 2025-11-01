// 973. K closes points to origin
// Topics: 'Array', 'Math', 'Divide and Conquer', 'Geometry', 'Sorting', 'Heap (Priority Queue)', 'Quickselect',
// Level: 'Medium'

// Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

// The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

// You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

// Example 1:

// Input: points = [[1,3],[-2,2]], k = 1
// Output: [[-2,2]]
// Explanation:
// The distance between (1, 3) and the origin is sqrt(10).
// The distance between (-2, 2) and the origin is sqrt(8).
// Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
// We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

// Example 2:

// Input: points = [[3,3],[5,-1],[-2,4]], k = 2
// Output: [[3,3],[-2,4]]
// Explanation: The answer [[-2,4],[3,3]] would also be accepted.

// Constraints:

//     1 <= k <= points.length <= 104
//     -104 <= xi, yi <= 104

package kclosespointstoorigin

func kClosest(points [][]int, max int) [][]int {
	arr := [][]int{}
	for i := 0; i < len(points); i++ {
		if i < max {
			arr = append(arr, points[i])
			j := len(arr) - 1
			for j > 0 && distance(arr[(j-1)/2]) < distance(arr[j]) {
				arr[(j-1)/2], arr[j] = arr[j], arr[(j-1)/2]
				j = (j - 1) / 2
			}

		} else if distance(points[i]) < distance(arr[0]) {
			arr[0] = points[i]
			j := 0
			for {
				largest := j
				left := 2*j + 1
				right := 2*j + 2

				if left < len(arr) && distance(arr[left]) > distance(arr[largest]) {
					largest = left
				}
				if right < len(arr) && distance(arr[right]) > distance(arr[largest]) {
					largest = right
				}
				if largest != j {
					arr[j], arr[largest] = arr[largest], arr[j]
					j = largest
				} else {
					break
				}
			}
		}
	}

	return arr
}

func distance(points []int) int {
	return points[0]*points[0] + points[1]*points[1]
}
