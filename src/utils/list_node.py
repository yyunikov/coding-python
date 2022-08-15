# Definition for singly-linked list.

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
