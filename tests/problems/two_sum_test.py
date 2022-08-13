import pytest

from src.problems.two_sum import Solution


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([2, 7, 11, 15], 9, [0, 1])
    ],
)
def test_solution(nums, target, expected):
    assert Solution().twoSum(nums, target) == expected
