"""
PROBLEM

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:


Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
"""
from typing import Optional, Dict, List

from src.utils.tree_node import TreeNode


class Solution:
    def _dfs(self,
             root: Optional[TreeNode],
             level: int,
             sums_on_level: Dict[int, int],
             count_on_level: Dict[int, int]):
        if level in sums_on_level:
            sums_on_level[level] = sums_on_level[level] + root.val
        else:
            sums_on_level[level] = root.val

        if level in count_on_level:
            count_on_level[level] = count_on_level[level] + 1
        else:
            count_on_level[level] = 1

        if root.left:
            self._dfs(root.left, level + 1, sums_on_level, count_on_level)
        if root.right:
            self._dfs(root.right, level + 1, sums_on_level, count_on_level)

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sums_on_level: Dict[int, int] = dict()
        count_on_level: Dict[int, int] = dict()
        results = []

        self._dfs(root, 0, sums_on_level, count_on_level)

        for level, value in sums_on_level.items():
            results.append(sums_on_level[level] / count_on_level[level])

        return results
