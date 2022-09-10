from typing import List, Optional

from src.utils.tree_node import BTreeNode

"""
PROBLEM

Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.
 
Example 1:

Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
Example 2:

Input: root = [1]
Output: [[1]]
"""


class Solution:

    def findLeaves(self, root: Optional[BTreeNode]) -> List[List[int]]:
        results = []
        self.dfs(root, results, 0)
        return results

    def dfs(self, node: Optional[BTreeNode], results: List[List[int]],
            floor: int):
        if not node:
            return floor

        # post order traversal
        left_floor = self.dfs(node.left, results, floor)
        right_floor = self.dfs(node.right, results, floor)

        floor = max(left_floor, right_floor)

        # init new array
        if len(results) <= floor:
            results.insert(floor, [])

        results[floor].append(node.val)

        # reached the leaf
        # floor corresponds to index in array
        return floor + 1
