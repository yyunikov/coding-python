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

        smallest_item = min(list1.val, list2.val)
        first_list, second_list = (list1, list2) if list1.val == smallest_item else (list2, list1)
        result_root_node = first_list

        while second_list:
            # if first list has next and we can insert second item
            if first_list.next and second_list.val <= first_list.next.val:
                first_list.next, first_list.next.next = ListNode(second_list.val), first_list.next

                second_list = second_list.next
            # reached the end of first list, just append the second one
            elif not first_list.next:
                first_list.next = second_list
                second_list = None

            if first_list.next:
                first_list = first_list.next

        return result_root_node

