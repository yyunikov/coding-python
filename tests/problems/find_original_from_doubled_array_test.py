import pytest

from src.problems.find_original_from_doubled_array import Solution
from src.problems.find_original_from_doubled_array_optimized import Solution as SolutionOptimized


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 3, 4, 2, 6, 8], [1, 3, 4]),
        ([6, 3, 0, 1], []),
        ([1], []),
        ([0, 0, 0, 0], [0, 0]),
        ([2, 1, 2, 4, 2, 4], [1, 2, 2]),
        ([0, 0, 3], []),
        ([2, 1], [1]),
    ],
)
def test_solution(nums, expected):
    assert Solution().findOriginalArray(nums) == expected


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 3, 4, 2, 6, 8], [1, 3, 4]),
        ([6, 3, 0, 1], []),
        ([1], []),
        ([0, 0, 0, 0], [0, 0]),
        ([2, 1, 2, 4, 2, 4], [1, 2, 2]),
        ([0, 0, 3], []),
        ([2, 1], [1]),
    ],
)
def test_solution_optimized(nums, expected):
    assert SolutionOptimized().findOriginalArray(nums) == expected
