from recover import TreeNode, Solution


def make_tree(vals: list) -> TreeNode | None:
    """Build a tree from level-order list (None = missing node)."""
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    queue = [root]
    i = 1
    while queue and i < len(vals):
        node = queue.pop(0)
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


def level_order(root: TreeNode | None) -> list:
    """Serialize tree to level-order list (None = missing node)."""
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


sol = Solution()


def test_example1():
    # [1,3,null,null,2] -> [3,1,null,null,2]
    root = make_tree([1, 3, None, None, 2])
    sol.recoverTree(root)
    assert level_order(root) == [3, 1, None, None, 2]


def test_example2():
    # [3,1,4,null,null,2] -> [2,1,4,null,null,3]
    root = make_tree([3, 1, 4, None, None, 2])
    sol.recoverTree(root)
    assert level_order(root) == [2, 1, 4, None, None, 3]


def test_adjacent_swap():
    # BST [2,1,3] with adjacent nodes 1 and 2 swapped -> [1,2,3] invalid, recover
    root = make_tree([1, 2, 3])  # 2 and 1 swapped: left child > parent
    sol.recoverTree(root)
    assert level_order(root) == [2, 1, 3]


def test_two_nodes():
    # Minimum tree: two nodes swapped
    root = make_tree([2, 1])  # valid BST, but swap root and left: [1,2]
    # [1,2] means left child 2 > root 1 — invalid
    root2 = make_tree([1, 2])
    sol.recoverTree(root2)
    assert level_order(root2) == [2, 1]


if __name__ == "__main__":
    tests = [test_example1, test_example2, test_adjacent_swap, test_two_nodes]
    passed = 0
    for t in tests:
        try:
            t()
            print(f"PASS  {t.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"FAIL  {t.__name__}: {e}")
    print(f"\n{passed}/{len(tests)} passed")
