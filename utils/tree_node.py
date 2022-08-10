class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if not other:
            return False

        return self.val == other.val and self.left == other.left and self.right == other.right
