"""
PROBLEM

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
"""
from typing import MutableSet

from src.utils.tree_node import BTreeNode


class Solution:
    def lowestCommonAncestor(self, root: BTreeNode, p: BTreeNode,
                             q: BTreeNode) -> BTreeNode:
        p_ancestors = {root}
        self.find_ancestors(root, p, p_ancestors)
        found, ancestor = self.find_common_ancestor(root, q, p_ancestors)
        return ancestor

    def find_ancestors(self, current: BTreeNode, node: BTreeNode,
                       ancestors: MutableSet[BTreeNode]) -> bool:
        if current.val == node.val:
            ancestors.add(current)
            return True  # node found

        if current.left:
            node_found = self.find_ancestors(current.left, node, ancestors)
            if node_found:
                ancestors.add(current)
                return True

        if current.right:
            node_found = self.find_ancestors(current.right, node, ancestors)
            if node_found:
                ancestors.add(current)
                return True

        return False  # node not found

    def find_common_ancestor(self, current: BTreeNode, node: BTreeNode,
                             ancestors: MutableSet[BTreeNode]) -> (bool, BTreeNode):
        if current.val == node.val:
            # node found
            if current in ancestors:
                return True, current
            # keep looking
            return True, None

        if current.left:
            node_found, ancestor = self.find_common_ancestor(current.left, node,
                                                             ancestors)
            if node_found:
                if not ancestor and current in ancestors:
                    return True, current
                return True, ancestor

        if current.right:
            node_found, ancestor = self.find_common_ancestor(current.right, node,
                                                             ancestors)
            if node_found:
                if not ancestor and current in ancestors:
                    return True, current
                return True, ancestor

        return False, None  # node not found
