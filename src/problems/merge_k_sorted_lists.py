# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional

from src.utils.list_node import ListNode

"""
PROBLEM

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
"""


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1:
            return lists[0]

        result_list = None
        for list_node in lists:
            result_list = self.mergeTwoLists(result_list, list_node)

        return result_list

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


