from queue import Queue


class BTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if not other or not isinstance(other, self.__class__):
            return False

        return self.val == other.val and \
            self.left == other.left and \
            self.right == other.right

    def __hash__(self) -> int:
        return hash((self.val, self.left, self.right))

    @classmethod
    def of(cls, val: int, *args):
        left = None
        right = None

        q = Queue()
        root = BTreeNode(val)
        q.put(root)

        node = root
        for arg in args:
            node = q.get() if not q.empty() and left and not right else node

            if not left:
                left = BTreeNode(arg)
            elif not right:
                right = BTreeNode(arg)

                if left.val:
                    node.left = left
                    q.put(left)

                if right.val:
                    node.right = right
                    q.put(right)

                left = None
                right = None

        node = q.get() if not q.empty() and left and not right else node
        if left:
            node.left = left
        if right:
            node.right = right

        return root
