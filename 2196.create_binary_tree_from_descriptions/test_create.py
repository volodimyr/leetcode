from collections import defaultdict
from typing import List, Optional
from create import Solution, TreeNode

# Helper functions for testing
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Convert tree to level-order list representation (BFS)"""
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result


def print_tree(root: Optional[TreeNode], level=0, prefix="Root: "):
    """Print tree structure in a readable format"""
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            if root.left:
                print_tree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")


def run_tests():
    solution = Solution()
    
    # Test 1: Example 1 from problem
    print("Test 1: Multiple levels with full tree")
    descriptions1 = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
    root1 = solution.createBinaryTree(descriptions1)
    result1 = tree_to_list(root1)
    print(f"Input: {descriptions1}")
    print(f"Output: {result1}")
    print(f"Expected: [50, 20, 80, 15, 17, 19]")
    print_tree(root1)
    print()
    
    # Test 2: Example 2 from problem
    print("Test 2: Linear tree with sparse nodes")
    descriptions2 = [[1,2,1],[2,3,0],[3,4,1]]
    root2 = solution.createBinaryTree(descriptions2)
    result2 = tree_to_list(root2)
    print(f"Input: {descriptions2}")
    print(f"Output: {result2}")
    print(f"Expected: [1, 2, None, None, 3, 4]")
    print_tree(root2)
    print()
    
    # Test 3: Single parent with two children
    print("Test 3: Simple tree - one parent, two children")
    descriptions3 = [[1,2,1],[1,3,0]]
    root3 = solution.createBinaryTree(descriptions3)
    result3 = tree_to_list(root3)
    print(f"Input: {descriptions3}")
    print(f"Output: {result3}")
    print(f"Expected: [1, 2, 3]")
    print_tree(root3)
    print()
    
    # Test 4: Only left children
    print("Test 4: Only left children chain")
    descriptions4 = [[1,2,1],[2,3,1],[3,4,1]]
    root4 = solution.createBinaryTree(descriptions4)
    result4 = tree_to_list(root4)
    print(f"Input: {descriptions4}")
    print(f"Output: {result4}")
    print(f"Expected: [1, 2, None, 3, None, 4]")
    print_tree(root4)
    print()
    
    # Test 5: Only right children
    print("Test 5: Only right children chain")
    descriptions5 = [[1,2,0],[2,3,0],[3,4,0]]
    root5 = solution.createBinaryTree(descriptions5)
    result5 = tree_to_list(root5)
    print(f"Input: {descriptions5}")
    print(f"Output: {result5}")
    print(f"Expected: [1, None, 2, None, 3, None, 4]")
    print_tree(root5)
    print()
    
    # Test 6: Single node
    print("Test 6: Single parent-child relationship")
    descriptions6 = [[1,2,1]]
    root6 = solution.createBinaryTree(descriptions6)
    result6 = tree_to_list(root6)
    print(f"Input: {descriptions6}")
    print(f"Output: {result6}")
    print(f"Expected: [1, 2]")
    print_tree(root6)
    print()
    
    # Test 7: Larger values
    print("Test 7: Large node values")
    descriptions7 = [[100000,50000,1],[100000,75000,0],[50000,25000,1]]
    root7 = solution.createBinaryTree(descriptions7)
    result7 = tree_to_list(root7)
    print(f"Input: {descriptions7}")
    print(f"Output: {result7}")
    print(f"Expected: [100000, 50000, 75000, 25000]")
    print_tree(root7)
    print()
    
    # Test 8: Unordered descriptions
    print("Test 8: Descriptions in random order")
    descriptions8 = [[3,4,0],[1,2,1],[2,3,0]]
    root8 = solution.createBinaryTree(descriptions8)
    result8 = tree_to_list(root8)
    print(f"Input: {descriptions8}")
    print(f"Output: {result8}")
    print(f"Expected: [1, 2, None, None, 3, None, 4]")
    print_tree(root8)
    print()


if __name__ == "__main__":
    run_tests()