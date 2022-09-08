from typing import Optional

from src.utils.tree_node import TreeNode

"""
PROBLEM

Given the root of a binary tree, return the length of the longest consecutive sequence path.

A consecutive sequence path is a path where the values increase by one along the path.

Note that the path can start at any node in the tree, and you cannot go from a node to its parent in the path.

Example 1:

Input: root = [1,null,3,2,4,null,null,null,5]
Output: 3
Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input: root = [2,null,3,2,null,1]
Output: 2
Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
"""


class Solution:

    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        max_length = 1

        def dfs(node: Optional[TreeNode],
                parent: Optional[TreeNode],
                current_length: int):
            if not node:
                return
            if parent and node.val == parent.val + 1:
                current_length = current_length + 1
            else:
                current_length = 1

            nonlocal max_length
            max_length = max(current_length, max_length)
            dfs(node.left, node, current_length)
            dfs(node.right, node, current_length)

        dfs(root, None, 1)

        return max_length

