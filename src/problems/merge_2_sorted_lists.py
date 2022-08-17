# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from src.utils.list_node import ListNode

"""
PROBLEM

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        result_root_node = None
        result_current_node = None

        while list1 and list2:
            if list1.val < list2.val:
                list1, result_current_node = self.insert_next_node(list1, result_current_node)
            else:
                list2, result_current_node = self.insert_next_node(list2, result_current_node)

            if not result_root_node:
                result_root_node = result_current_node

        while list1:
            list1, result_current_node = self.insert_next_node(list1, result_current_node)

        while list2:
            list2, result_current_node = self.insert_next_node(list2, result_current_node)

        return result_root_node

    def insert_next_node(self, list_node: Optional[ListNode], result_current_node: Optional[ListNode]):
        if result_current_node:
            result_current_node.next = ListNode(list_node.val)
            result_current_node = result_current_node.next
            list_node = list_node.next
        else:
            result_current_node = ListNode(list_node.val)
            list_node = list_node.next
        return list_node, result_current_node
