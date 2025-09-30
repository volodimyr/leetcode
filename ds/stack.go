// Design Stack
// Topics: 'Data structures'

package ds

type Stack[T any] struct {
	arr []T
}

func (s *Stack[T]) Pop() T {
	if s.Empty() {
		return s.zero()
	}
	v := s.arr[len(s.arr)-1]
	s.arr = s.arr[:len(s.arr)-1]
	return v
}

func (s *Stack[T]) zero() T {
	var zero T
	return zero
}

func (s *Stack[T]) Push(v T) {
	s.arr = append(s.arr, v)
}

func (s *Stack[T]) Peek() T {
	return s.arr[len(s.arr)-1]
}

func (s *Stack[T]) Empty() bool {
	return len(s.arr) == 0
}
