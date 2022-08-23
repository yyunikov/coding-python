import pytest

from src.problems.palindrome_linked_list import Solution
from src.utils.list_node import ListNode


@pytest.mark.parametrize(
    "nums,expected",
    [
        (ListNode.from_int_list([1, 2, 2, 1]), True),
        (ListNode.from_int_list([1, 2, 3, 2, 1]), True),
        (ListNode.from_int_list([1, 2, 3, 4, 2, 3, 1]), False),
        (ListNode.from_int_list([1]), True),
        (ListNode.from_int_list([1, 2]), False),
    ],
)
def test_solution(nums, expected):
    assert Solution().isPalindrome(nums) == expected
