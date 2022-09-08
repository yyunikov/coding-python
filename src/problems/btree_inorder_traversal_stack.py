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
        stack = []

        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            if node:
                values.append(node.val)
                node = node.right

        return values
