class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if not other and not isinstance(other, self.__class__):
            return False

        return self.val == other.val and \
            self.left == other.left and \
            self.right == other.right

    def __hash__(self) -> int:
        return hash((self.val, self.left, self.right))

