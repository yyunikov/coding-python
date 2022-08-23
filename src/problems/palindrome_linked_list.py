from typing import Optional

from src.utils.list_node import ListNode


"""
PROBLEM

Given the head of a singly linked list, return true if it is a palindrome.

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
"""


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_size = 0

        # figure out the size
        current = head
        while current:
            list_size += 1
            current = current.next

        is_even_size = list_size % 2 == 0

        # figure out if palindrome
        current = head
        i = 0
        middle = list_size // 2
        stack = []
        while current:
            if is_even_size:
                if i < middle:
                    stack.append(current.val)
                else:
                    top = stack.pop()
                    if current.val != top:
                        return False
            else:
                if i < middle:
                    stack.append(current.val)
                elif i > middle:
                    top = stack.pop()
                    if current.val != top:
                        return False

            current = current.next
            i += 1

        return True
