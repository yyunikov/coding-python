import pytest

from src.problems.reverse_linked_list import Solution
from src.problems.reverse_linked_list_2 import Solution as Solution2
from src.problems.reverse_linked_list_recursive import Solution as SolutionRecursive
from src.utils.list_node import ListNode


@pytest.mark.parametrize(
    "nums,expected",
    [
        (ListNode.from_int_list([1, 2, 2, 1]), ListNode.from_int_list([1, 2, 2, 1])),
        (ListNode.from_int_list([1, 2, 3, 4]), ListNode.from_int_list([4, 3, 2, 1])),
        (ListNode.from_int_list([1, 2, 3, 4, 5]), ListNode.from_int_list([5, 4, 3, 2, 1])),
        (ListNode.from_int_list([1]), ListNode.from_int_list([1])),
    ],
)
def test_solution(nums, expected):
    assert Solution().reverseList(nums) == expected


@pytest.mark.parametrize(
    "nums,expected",
    [
        (ListNode.from_int_list([1, 2, 2, 1]), ListNode.from_int_list([1, 2, 2, 1])),
        (ListNode.from_int_list([1, 2, 3, 4]), ListNode.from_int_list([4, 3, 2, 1])),
        (ListNode.from_int_list([1, 2, 3, 4, 5]), ListNode.from_int_list([5, 4, 3, 2, 1])),
        (ListNode.from_int_list([1]), ListNode.from_int_list([1])),
    ],
)
def test_solution_2(nums, expected):
    assert Solution2().reverseList(nums) == expected


@pytest.mark.parametrize(
    "nums,expected",
    [
        (ListNode.from_int_list([1, 2, 2, 1]), ListNode.from_int_list([1, 2, 2, 1])),
        (ListNode.from_int_list([1, 2, 3, 4]), ListNode.from_int_list([4, 3, 2, 1])),
        (ListNode.from_int_list([1, 2, 3, 4, 5]), ListNode.from_int_list([5, 4, 3, 2, 1])),
        (ListNode.from_int_list([1]), ListNode.from_int_list([1])),
    ],
)
def test_solution_recursive(nums, expected):
    assert SolutionRecursive().reverseList(nums) == expected
