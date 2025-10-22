package ds

type TreeMap struct {
	node *tmnode
}

type tmnode struct {
	Key   int
	Val   int
	Right *tmnode
	Left  *tmnode
}

func NewTreeMap() *TreeMap {
	return &TreeMap{}
}

func (t *TreeMap) Insert(key, val int) {
	t.node = insert(t.node, key, val)
}

func insert(root *tmnode, key, val int) *tmnode {
	if root == nil {
		root = &tmnode{Key: key, Val: val}
		return root
	}
	if root.Key > key {
		root.Left = insert(root.Left, key, val)
	} else if root.Key < key {
		root.Right = insert(root.Right, key, val)
	} else {
		root.Val = val
	}
	return root
}

func (t *TreeMap) Get(key int) int {
	node := get(t.node, key)
	if node == nil {
		return -1
	}
	return node.Val
}

func get(root *tmnode, key int) *tmnode {
	if root == nil {
		return nil
	}
	if root.Key > key {
		return get(root.Left, key)
	}
	if root.Key < key {
		return get(root.Right, key)
	}
	return root
}

func (t *TreeMap) GetMin() int {
	if t.node == nil {
		return -1
	}
	node := t.node
	for node.Left != nil {
		node = node.Left
	}
	return node.Val
}

func (t *TreeMap) GetMax() int {
	if t.node == nil {
		return -1
	}
	node := t.node
	for node.Right != nil {
		node = node.Right
	}
	return node.Val
}

func (t *TreeMap) Remove(key int) {
	t.node = remove(t.node, key)

}

func remove(root *tmnode, key int) *tmnode {
	if root == nil {
		return root
	}
	if root.Key > key {
		root.Left = remove(root.Left, key)
	} else if root.Key < key {
		root.Right = remove(root.Right, key)
	} else {
		if root.Right == nil {
			return root.Left
		}
		if root.Left == nil {
			return root.Right
		}
		k, v := successor(root, root.Right)
		root.Key, root.Val = k, v
	}
	return root
}

func successor(parent, node *tmnode) (int, int) {
	if node.Left == nil {
		k, v := node.Key, node.Val
		if parent.Right == node {
			parent.Right = node.Right
		} else {
			parent.Left = node.Right
		}
		return k, v
	}
	return successor(node, node.Left)
}

func (t *TreeMap) GetInorderKeys() []int {
	arr := []int{}
	traversal(t.node, &arr)
	return arr
}

func traversal(root *tmnode, arr *[]int) {
	if root == nil {
		return
	}
	traversal(root.Left, arr)
	*arr = append(*arr, root.Key)
	traversal(root.Right, arr)
}
