import pytest

from src.problems.kth_largest_element import Solution


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([-1, -2, -3, -4, -5], 1, -1),
        ([1, 2, 3, 4, 5], 2, 4)
    ],
)
def test_solution(nums, k, expected):
    assert Solution().findKthLargest(nums, k) == expected
