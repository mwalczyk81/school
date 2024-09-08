class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def insert_into_bst(root, value):
    """
    Inserts a value into a Binary Search Tree and returns the root of the tree.
    """
    if root is None:
        return TreeNode(value)
    
    if value < root.value:
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)
    
    return root

def is_valid_bst(root):
    """
    Determines if a binary tree is a valid Binary Search Tree.
    """
    def helper(node, left, right):
        if not node:
            return True
        if not (left < node.value < right):
            return False
        return helper(node.left, left, node.value) and helper(node.right, node.value, right)
    
    return helper(root, float('-inf'), float('inf'))

def inorder_traversal(root):
    """
    Performs in-order traversal on a binary tree and returns a list of values.
    """
def inorder_traversal(root):
    result = []
    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.value)
            traverse(node.right)
    
    traverse(root)
    return result
