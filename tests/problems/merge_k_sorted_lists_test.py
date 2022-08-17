import pytest

from src.problems.merge_k_sorted_lists import Solution
from src.utils.list_node import ListNode


@pytest.mark.parametrize(
    "lists,expected",
    [
        (
                [
                    ListNode(1, next=
                             ListNode(4, next=
                                      ListNode(5))),
                    ListNode(1, next=
                             ListNode(3, next=
                                      ListNode(4))),
                    ListNode(2, next=
                             ListNode(6))

                ],
                ListNode(1, next=
                         ListNode(1, next=
                                  ListNode(2, next=
                                           ListNode(3, next=
                                                    ListNode(4, next=
                                                             ListNode(4, next=
                                                                      ListNode(5, next=
                                                                               ListNode(6))))))))
        )
    ],
)
def test_solution(lists, expected):
    assert Solution().mergeKLists(lists) == expected
