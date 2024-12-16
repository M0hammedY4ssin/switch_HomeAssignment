class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_max_node(root: Optional[TreeNode]):
    if not(root.left and root.right):
        return root.val

    l = find_max_node(root.left)
    r = find_max_node(root.right) 

    return max(l,r)