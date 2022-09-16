import pytest

from src.problems.max_score_from_multiply_operations import Solution


@pytest.mark.parametrize(
    "nums,multipliers,expected",
    [
        ([1, 2, 3], [3, 2, 1], 14),
        ([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6], 102)
    ],
)
def test_solution(nums, multipliers, expected):
    assert Solution().maximumScore(nums, multipliers) == expected
