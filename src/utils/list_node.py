# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val

    def __eq__(self, other):
        if not other or not isinstance(other, ListNode):
            return False

        return self.val == other.val and self.next == other.next

    def __hash__(self):
        return hash((self.val, self.next))

    @classmethod
    def from_int_list(cls, int_list: List[int]):
        if not int_list:
            return None

        head = ListNode(val=int_list[0])
        current = head
        for i in range(1, len(int_list)):
            current.next = ListNode(val=int_list[i])
            current = current.next

        return head
