import pytest

from src.problems.split_array_largest_sum import Solution
from src.problems.split_array_largest_sum_brute_force import Solution as SolutionBruteForce


@pytest.mark.parametrize(
    "nums,m,expected",
    [
        ([7, 2, 5, 10, 8], 2, 18),
        ([1, 2, 3, 4, 5], 2, 9),
        ([1, 4, 4], 3, 4),
        ([2, 16, 14, 15], 2, 29),
        ([2, 3, 1, 2, 4, 3], 5, 4),
    ],
)
def test_solution(nums, m, expected):
    assert Solution().splitArray(nums, m) == expected


@pytest.mark.parametrize(
    "nums,m,expected",
    [
        ([7, 2, 5, 10, 8], 2, 18),
        ([1, 2, 3, 4, 5], 2, 9),
        ([1, 4, 4], 3, 4),
        ([2, 16, 14, 15], 2, 29),
        ([2, 3, 1, 2, 4, 3], 5, 4)
    ],
)
def test_solution_brute_force(nums, m, expected):
    assert SolutionBruteForce().splitArray(nums, m) == expected
