from typing import Optional, List

from src.utils.tree_node import BTreeNode

"""
PROBLEM
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
"""


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[BTreeNode]:
        return self.insert_middle_node(None, nums)

    def insert_middle_node(self, middle_node: BTreeNode, nums: List[int]) -> BTreeNode:
        # find the root, the average middle
        # if the array is already ordered in ascending order
        # then the middle element would be the root
        middle_index = len(nums) // 2
        if not self.index_exists(nums, middle_index):
            return middle_node

        middle_value = nums[middle_index]

        if not middle_node:
            middle_node = BTreeNode(middle_value)
        else:
            middle_node = self.insert_node(middle_node, middle_value)

        # insert left sub-tree
        self.insert_middle_node(middle_node, nums[0: middle_index])
        # insert right sub-tree
        self.insert_middle_node(middle_node, nums[middle_index + 1: len(nums)])

        return middle_node

    def insert_node(self, root: BTreeNode, insert_value: int) -> BTreeNode:
        if not root.left and insert_value <= root.val:
            root.left = BTreeNode(insert_value)
            return root.left

        if not root.right and insert_value > root.val:
            root.right = BTreeNode(insert_value)
            return root.right

        if root.left and insert_value <= root.left.val:
            self.insert_node(root.left, insert_value)

        if root.right and insert_value > root.right.val:
            self.insert_node(root.right, insert_value)

    def index_exists(self, nums: List[int], index) -> bool:
        try:
            nums[index]
            return True
        except IndexError:
            return False
