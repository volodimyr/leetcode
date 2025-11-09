// 284. Peeking Iterator
// Topics: 'Array', 'Design', 'Iterator'
// Level: 'Medium'

// Design an iterator that supports the peek operation on an existing iterator in addition to the hasNext and the next operations.

// Implement the PeekingIterator class:

//     PeekingIterator(Iterator<int> nums) Initializes the object with the given integer iterator iterator.
//     int next() Returns the next element in the array and moves the pointer to the next element.
//     boolean hasNext() Returns true if there are still elements in the array.
//     int peek() Returns the next element in the array without moving the pointer.

// Note: Each language may have a different implementation of the constructor and Iterator, but they all support the int next() and boolean hasNext() functions.

// Example 1:

// Input
// ["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
// [[[1, 2, 3]], [], [], [], [], []]
// Output
// [null, 1, 2, 2, 3, false]

// Explanation
// PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [1,2,3]
// peekingIterator.next();    // return 1, the pointer moves to the next element [1,2,3].
// peekingIterator.peek();    // return 2, the pointer does not move [1,2,3].
// peekingIterator.next();    // return 2, the pointer moves to the next element [1,2,3]
// peekingIterator.next();    // return 3, the pointer moves to the next element [1,2,3]
// peekingIterator.hasNext(); // return False

// Constraints:

//     1 <= nums.length <= 1000
//     1 <= nums[i] <= 1000
//     All the calls to next and peek are valid.
//     At most 1000 calls will be made to next, hasNext, and peek.

package peekingiterator

type Iterator[T any] struct {
	arr []T
	i   int
}

func (i *Iterator[T]) hasNext() bool {
	return i.i < len(i.arr)
}

func (i *Iterator[T]) next() T {
	v := i.arr[i.i]
	i.i++
	return v
}

type PeekingIterator[T any] struct {
	arr  []T
	iter *Iterator[T]
	i    int
}

func Constructor[T any](iter *Iterator[T]) *PeekingIterator[T] {
	return &PeekingIterator[T]{
		i:    0,
		arr:  []T{},
		iter: iter,
	}
}

func (p *PeekingIterator[T]) hasNext() bool {
	return p.iter.hasNext() || p.i < len(p.arr)
}

func (p *PeekingIterator[T]) next() T {
	if p.i < len(p.arr) {
		v := p.arr[p.i]
		p.i++
		return v
	}
	return p.iter.next()
}

func (p *PeekingIterator[T]) peek() T {
	if p.i < len(p.arr) {
		return p.arr[p.i]
	}
	v := p.iter.next()
	p.arr = append(p.arr, v)
	return v
}
