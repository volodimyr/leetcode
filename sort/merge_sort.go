// Merge Sort

// Implement Merge Sort.

// Merge Sort is a divide-and-conquer algorithm for sorting an array or list of elements. It works by recursively dividing the unsorted list into n sub-lists, each containing one element. Then, it repeatedly merges sub-lists to produce new sorted sub-lists until there is only one sub-list remaining.

// Objective:

// Given a list of key-value pairs, sort the list by key using Merge Sort. If two key-value pairs have the same key, maintain their relative order in the sorted list.

// Input:

//     pairs - a list of key-value pairs, where each key-value has an integer key and a string value. (0 <= pairs.length <= 100).

// Example 1:

// Input:
// pairs = [(5, "apple"), (2, "banana"), (9, "cherry"), (1, "date"), (9, "elderberry")]

// Output:
// [(1, "date"), (2, "banana"), (5, "apple"), (9, "cherry"), (9, "elderberry")]

// Note: As you can see, the solution is always stable. The two pairs with the key 9 maintained their relative positions.

// Example 2:

// Input:
// pairs = [(3, "cat"), (2, "dog"), (3, "bird")]

// Output:
// [(2, "dog"), (3, "cat"), (3, "bird")]

package sort

func mergeSort(pairs []Pair) []Pair {
	msort(pairs, 0, len(pairs)-1)
	return pairs
}

func msort(pairs []Pair, l, r int) {
	if l < r {
		m := (l + r) / 2
		msort(pairs, l, m)
		msort(pairs, m+1, r)

		merge(pairs, l, m, r)
	}
}

func merge(pairs []Pair, l, m, r int) {
	L := make([]Pair, m-l+1)
	R := make([]Pair, r-m)
	copy(L, pairs[l:m+1])
	copy(R, pairs[m+1:r+1])

	var i, j int
	k := l

	for i < len(L) && j < len(R) {
		if L[i].Key <= R[j].Key {
			pairs[k] = L[i]
			i++
		} else {
			pairs[k] = R[j]
			j++
		}
		k++
	}

	for i < len(L) {
		pairs[k] = L[i]
		i++
		k++
	}
	for j < len(R) {
		pairs[k] = R[j]
		j++
		k++
	}
}
