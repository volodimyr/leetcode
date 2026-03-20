from typing import Optional

from range import Solution
from range import TreeNode

def build_tree(values):
    """Helper function to build a tree from level-order list."""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


def test_example_1():
    """Test Example 1: root = [10,5,15,3,7,null,18], low = 7, high = 15"""
    sol = Solution()
    root = build_tree([10, 5, 15, 3, 7, None, 18])
    result = sol.rangeSumBST(root, 7, 15)
    assert result == 32, f"Expected 32, got {result}"
    print("[PASS] Test Example 1 passed")


def test_example_2():
    """Test Example 2: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10"""
    sol = Solution()
    root = build_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
    result = sol.rangeSumBST(root, 6, 10)
    assert result == 23, f"Expected 23, got {result}"
    print("[PASS] Test Example 2 passed")


def test_single_node_in_range():
    """Test with single node that is in range"""
    sol = Solution()
    root = TreeNode(10)
    result = sol.rangeSumBST(root, 5, 15)
    assert result == 10, f"Expected 10, got {result}"
    print("[PASS] Test single node in range passed")


def test_single_node_out_of_range():
    """Test with single node that is out of range"""
    sol = Solution()
    root = TreeNode(10)
    result = sol.rangeSumBST(root, 15, 20)
    assert result == 0, f"Expected 0, got {result}"
    print("[PASS] Test single node out of range passed")


def test_all_nodes_in_range():
    """Test where all nodes are in the range"""
    sol = Solution()
    root = build_tree([10, 5, 15, 3, 7])
    result = sol.rangeSumBST(root, 1, 20)
    assert result == 40, f"Expected 40, got {result}"
    print("[PASS] Test all nodes in range passed")


def test_no_nodes_in_range():
    """Test where no nodes are in the range"""
    sol = Solution()
    root = build_tree([10, 5, 15, 3, 7])
    result = sol.rangeSumBST(root, 20, 30)
    assert result == 0, f"Expected 0, got {result}"
    print("[PASS] Test no nodes in range passed")


def test_range_equals_root():
    """Test where range exactly matches root value"""
    sol = Solution()
    root = build_tree([10, 5, 15])
    result = sol.rangeSumBST(root, 10, 10)
    assert result == 10, f"Expected 10, got {result}"
    print("[PASS] Test range equals root passed")


def test_only_left_subtree_in_range():
    """Test where only left subtree nodes are in range"""
    sol = Solution()
    root = build_tree([10, 5, 15, 3, 7])
    result = sol.rangeSumBST(root, 3, 7)
    assert result == 15, f"Expected 15, got {result}"
    print("[PASS] Test only left subtree in range passed")


def test_only_right_subtree_in_range():
    """Test where only right subtree nodes are in range"""
    sol = Solution()
    root = build_tree([10, 5, 15, 3, 7, 12, 18])
    result = sol.rangeSumBST(root, 12, 20)
    assert result == 45, f"Expected 45, got {result}"
    print("[PASS] Test only right subtree in range passed")

def test_unbalanced_tree():
    """Test with an unbalanced tree (left-skewed)"""
    sol = Solution()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(1)
    result = sol.rangeSumBST(root, 1, 5)
    assert result == 9, f"Expected 9, got {result}"
    print("[PASS] Test unbalanced tree passed")


def test_minimum_values():
    """Test with minimum constraint values"""
    sol = Solution()
    root = TreeNode(1)
    result = sol.rangeSumBST(root, 1, 1)
    assert result == 1, f"Expected 1, got {result}"
    print("[PASS] Test minimum values passed")


def run_all_tests():
    """Run all test cases"""
    print("Running Range Sum of BST Tests...\n")
    
    test_example_1()
    test_example_2()
    test_single_node_in_range()
    test_single_node_out_of_range()
    test_all_nodes_in_range()
    test_no_nodes_in_range()
    test_range_equals_root()
    test_only_left_subtree_in_range()
    test_only_right_subtree_in_range()
    test_unbalanced_tree()
    test_minimum_values()
    
    print("\n[PASS] All tests passed!")


if __name__ == "__main__":
    run_all_tests()