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
        array_list = []
        if not head:
            return None

        while current:
            array_list.append(current.val)
            current = current.next

        array_list = array_list[::-1]
        reversed_head = ListNode(array_list[0])
        current = reversed_head
        for i in range(1, len(array_list)):
            current.next = ListNode(array_list[i])
            current = current.next

        return reversed_head
