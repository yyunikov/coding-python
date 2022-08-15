import pytest

from src.problems.add_two_numbers import Solution
from src.utils.list_node import ListNode


@pytest.mark.parametrize(
    "l1,l2,expected",
    [
        (
                ListNode(2, next=
                         ListNode(4, next=
                                  ListNode(3))),
                ListNode(5, next=
                         ListNode(6, next=
                                  ListNode(4))),
                ListNode(7, next=
                         ListNode(0, next=
                                  ListNode(8)))),
        (ListNode(0), ListNode(0), ListNode(0)),
        (
                ListNode(9, next=
                         ListNode(9, next=
                                  ListNode(9))),
                ListNode(9, next=
                         ListNode(9)),
                ListNode(8, next=
                         ListNode(9, next=
                                  ListNode(0, next=
                                           ListNode(1)))),
        ),
    ],
)
def test_solution(l1, l2, expected):
    assert Solution().addTwoNumbers(l1, l2) == expected
