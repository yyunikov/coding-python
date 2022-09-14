from typing import Optional, Dict, Tuple

from src.utils.tree_node import BTreeNode

"""
PROBLEM

You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

Example 1:


Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
Example 2:


Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.
"""


class Solution:
    def getDirections(self, root: Optional[BTreeNode],
                      startValue: int,
                      destValue: int) -> str:
        # the idea is to find lowest common ancestor
        # and then iterate via it
        nodes_to_parents: Dict[BTreeNode, Tuple[BTreeNode, str]] = {}
        stack = [root]

        start_node = None
        dest_node = None

        # find all parents O(n) time and storage
        while stack:
            node = stack.pop()

            if node.val == startValue:
                start_node = node
            if node.val == destValue:
                dest_node = node
            if node.left:
                nodes_to_parents[node.left] = (node, "L")
                stack.append(node.left)
            if node.right:
                nodes_to_parents[node.right] = (node, "R")
                stack.append(node.right)

        # find all parents of start value - O(n) time and storage
        parent = start_node
        start_node_parents = set()
        while parent is not None:
            if parent in nodes_to_parents:
                parent = nodes_to_parents[parent][0]
                start_node_parents.add(parent)
            else:
                parent = None

        # dest node is one of start node parents
        if dest_node in start_node_parents:
            # path UP from start node to dest node
            return self.path_up_from_start_to_end(start_node, dest_node,
                                                  nodes_to_parents)

        parent = dest_node
        # find all parents of dest value - O(n) time and storage
        while parent not in start_node_parents:
            if parent in nodes_to_parents:
                parent = nodes_to_parents[parent][0]
            # start node is a parent of dest node
            if parent == start_node:
                # path DOWN from start node to dest node - O(n) time and storage
                return self.path_down_from_start_to_end(start_node, dest_node,
                                                        nodes_to_parents)

        # parent is the common ancestor of start node and end node
        # path from start node to end node via common parent - O(n) time and storage
        return self.path_from_start_to_end(parent, start_node, dest_node,
                                           nodes_to_parents)

    def path_up_from_start_to_end(self, start_node: BTreeNode, dest_node: BTreeNode,
                                  nodes_to_parents: Dict[BTreeNode, Tuple[BTreeNode,
                                                         str]]):
        path = ""
        parent = start_node
        while parent != dest_node:
            path += "U"
            parent = nodes_to_parents[parent][0]

        return path

    def path_down_from_start_to_end(self, start_node: BTreeNode, dest_node: BTreeNode,
                                    nodes_to_parents: Dict[BTreeNode,
                                                           Tuple[BTreeNode, str]]):
        # move from lca to dest node
        node = dest_node
        path = ""
        while node != start_node:
            parent = nodes_to_parents[node]
            node = parent[0]
            path += parent[1]

        return path[::-1]

    def path_from_start_to_end(self, lca: BTreeNode, start_node: BTreeNode,
                               dest_node: BTreeNode,
                               nodes_to_parents: Dict[BTreeNode, Tuple[BTreeNode,
                                                                       str]]):
        path = ""
        parent = start_node
        # move to lca
        while parent != lca:
            path += "U"
            parent = nodes_to_parents[parent][0]

        # move from lca to dest node
        lca_path_to_dest = self.path_down_from_start_to_end(lca, dest_node,
                                                            nodes_to_parents)

        return path + lca_path_to_dest
