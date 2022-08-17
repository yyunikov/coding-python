import pytest

from src.problems.merge_2_sorted_lists import Solution
from src.problems.merge_2_sorted_lists_2 import Solution as Solution2
from src.utils.list_node import ListNode


@pytest.mark.parametrize(
    "l1,l2,expected",
    [
        (
                ListNode(1, next=
                         ListNode(2, next=
                                  ListNode(4))),
                ListNode(1, next=
                         ListNode(3, next=
                                  ListNode(4))),
                ListNode(1, next=
                         ListNode(1, next=
                                  ListNode(2, next=
                                           ListNode(3, next=
                                                    ListNode(4, next=
                                                             ListNode(4))))))
        ),
        (None, ListNode(0), ListNode(0)),
        (ListNode(1), ListNode(1), ListNode(1, next=ListNode(1)))
    ],
)
def test_solution(l1, l2, expected):
    assert Solution().mergeTwoLists(l1, l2) == expected


@pytest.mark.parametrize(
    "l1,l2,expected",
    [
        (
                ListNode(1, next=
                         ListNode(2, next=
                                  ListNode(4))),
                ListNode(1, next=
                         ListNode(3, next=
                                  ListNode(4))),
                ListNode(1, next=
                         ListNode(1, next=
                                  ListNode(2, next=
                                           ListNode(3, next=
                                                    ListNode(4, next=
                                                             ListNode(4))))))
        ),
        (
                ListNode(1, next=
                         ListNode(2, next=
                                  ListNode(4))),
                ListNode(1, next=
                         ListNode(3)),
                ListNode(1, next=
                         ListNode(1, next=
                                  ListNode(2, next=
                                           ListNode(3, next=
                                                    ListNode(4)))))
        ),
        (None, ListNode(0), ListNode(0)),
        (ListNode(1), ListNode(1), ListNode(1, next=ListNode(1)))
    ],
)
def test_solution_2(l1, l2, expected):
    assert Solution2().mergeTwoLists(l1, l2) == expected
