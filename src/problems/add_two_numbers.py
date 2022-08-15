"""
PROBLEM

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
from typing import Optional

from src.utils.list_node import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root_node = None
        current_node = None
        left_over = 0

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            result = l1_val + l2_val + left_over
            if result >= 10:
                result = result % 10
                left_over = 1
            else:
                left_over = 0

            if not root_node:
                root_node = ListNode(result)
                current_node = root_node
            else:
                current_node.next = ListNode(result)
                current_node = current_node.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if left_over != 0:
            current_node.next = ListNode(left_over)

        return root_node
