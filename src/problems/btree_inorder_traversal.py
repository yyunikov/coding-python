from typing import List, Optional

from src.utils.tree_node import BTreeNode

"""
PROBLEM

Given the root of a binary tree, 
return the inorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
"""


class Solution:

    def inorderTraversal(self, root: Optional[BTreeNode]) -> List[int]:
        values = []

        def dfs(node: Optional[BTreeNode]):
            if not node:
                return

            if node.left:
                dfs(node.left)

            nonlocal values
            values.append(node.val)

            if node.right:
                dfs(node.right)

        dfs(root)
        return values
