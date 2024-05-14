class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert_bst(root, key):
    """
    Insert a new TreeNode with the given key into the binary search tree rooted at 'root'.
    Return the root of the modified tree.
    """
    if root is None:
        # If the tree is empty, create a new node and return it as the new root
        return TreeNode(key)
    
    # Traverse the tree to find the appropriate position to insert the new node
    if key < root.val:
        # If the key is less than the current node's key, insert into the left subtree
        root.left = insert_bst(root.left, key)
    else:
        # If the key is greater than or equal to the current node's key, insert into the right subtree
        root.right = insert_bst(root.right, key)
    
    # Return the root of the modified tree
    return root

def find_max_heap(arr):
    """
    Given a max heap 'arr', return the maximum element (i.e., the root of the heap).
    If the heap is empty, return None.
    """
    if not arr:
        return None
    else:
        return arr[0]

def is_full_binary_tree(root: TreeNode):
    """
    Check if the binary tree rooted at 'root' is a full binary tree.
    Return True if it is, otherwise return False.
    """
    if root is None: 
        return True

    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return is_full_binary_tree(root.left) and is_full_binary_tree(root.right)

    return False

def get_tree_height(root: TreeNode):
    """
    Return the height of the binary tree rooted at 'root'.
    """
    if not root:
      return 0

    left_height = get_tree_height(root.left)
    right_height = get_tree_height(root.right)

    return 1 + max(left_height, right_height)