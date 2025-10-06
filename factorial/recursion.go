package factorial

func find(n int) int {
	if n == 1 {
		return n
	}
	return n * find(n-1)
}
