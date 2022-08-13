import pytest

from src.problems.max_sub_array import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
    ],
)
def test_solution(nums, expected):
    assert Solution().maxSubArray(nums) == expected
