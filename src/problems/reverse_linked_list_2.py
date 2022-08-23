from typing import Optional

from src.utils.list_node import ListNode

"""
PROBLEM

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []
"""


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        if not head:
            return None

        previous_item = None
        # 1->2->3->4->5
        while current:
            next_item = current.next  # 2 # 3
            current.next = previous_item  # 2->1 # 3 -> 2
            previous_item = current  # 1 # 2
            current = next_item  # 2 # 3

        return previous_item
