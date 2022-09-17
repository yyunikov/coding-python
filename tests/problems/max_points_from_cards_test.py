import pytest

from src.problems.max_points_from_cards import Solution


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([1, 2, 3, 4, 5, 6, 1], 3, 12),
        ([2, 2, 2], 2, 4),
        ([9, 7, 7, 9, 7, 7, 9], 7, 55),
        ([1, 79, 80, 1, 1, 200, 1], 3, 202)
    ],
)
def test_solution(nums, k, expected):
    assert Solution().maxScore(nums, k) == expected
