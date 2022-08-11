import sys
from typing import Optional, List

from utils.tree_node import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root, 0 - sys.maxsize - 1, sys.maxsize)

    def traverse(self, root: Optional[TreeNode], lowest: int, highest: int) -> bool:
        left_visit_result = True
        right_visit_result = True

        if not lowest < root.val < highest:
            return False

        if root.left:
            if root.val > root.left.val:
                left_visit_result = self.traverse(root.left, lowest, root.val)
            else:
                return False

        if root.right:
            if root.val < root.right.val:
                right_visit_result = self.traverse(root.right, root.val, highest)
            else:
                return False

        return left_visit_result and right_visit_result
