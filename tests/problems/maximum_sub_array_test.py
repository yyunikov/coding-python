import pytest

from src.problems.maximum_subarray import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([-2, -3, 4, -1, -2, 5, -3], 6),
        ([-1], -1)
    ],
)
def test_solution(nums, expected):
    assert Solution().max_sub_array(nums) == expected
