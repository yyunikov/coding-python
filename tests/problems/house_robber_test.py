import pytest

from src.problems.house_robber import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
    ],
)
def test_solution(nums, expected):
    assert Solution().rob(nums) == expected
