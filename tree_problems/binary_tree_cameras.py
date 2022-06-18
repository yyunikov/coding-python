from typing import Optional, List, Set


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_cameras = [0]
        right_cameras = [0]

        if root.left:
            setattr(root.left, 'parent', root)
            self.traverse(left_cameras, root.left)
        if root.right:
            setattr(root.right, 'parent', root)
            self.traverse(right_cameras, root.right)

        self.cover(left_cameras, root)

        total = left_cameras[0] + right_cameras[0]
        return total if not total == 0 else 1

    def traverse(self, cameras_count: List, node: Optional[TreeNode]):
        if not node:
            return

        # visit left
        if node.left:
            setattr(node.left, 'parent', node)
            self.traverse(cameras_count, node.left)

        # visit right
        if node.right:
            setattr(node.right, 'parent', node)
            self.traverse(cameras_count, node.right)

        self.cover(cameras_count, node)

    def cover(self, cameras_count: List, node: Optional[TreeNode]):
        if ((not hasattr(node, 'parent') and node.val == 0) or
                (node.left and node.left.val == 0) or
                (node.right and node.right.val == 0)):
            node.val = 1
            if hasattr(node, 'parent') and node.parent:
                node.parent.val = 1
            if node.left:
                node.left.val = 1
            if node.right:
                node.right.val = 1
            cameras_count[0] = cameras_count[0] + 1
