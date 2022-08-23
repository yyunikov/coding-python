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
        if not head or not head.next:
            return head

        # 1, 2, 3, 4
        current = self.reverseList(head.next)  # reached current = 4
        head.next.next = head  # head is 3 at this point, head.next.next is current.next therefore we set it to 3
        head.next = None  # need to remove pointer from to 4

        return current
