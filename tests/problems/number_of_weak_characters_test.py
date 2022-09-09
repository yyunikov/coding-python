import pytest

from src.problems.number_of_weak_characters import Solution as SolutionBruteForce
from src.problems.number_of_weak_characters_optimized import Solution as SolutionOptimized


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([[5, 5], [6, 3], [3, 6]], 0),
        ([[2, 2], [3, 3]], 1),
        ([[1, 1], [2, 1], [2, 2], [1, 2]], 1),
        ([[1, 5], [10, 4], [4, 3]], 1)
    ],
)
def test_solution_brute_force(nums, expected):
    assert SolutionBruteForce().numberOfWeakCharacters(nums) == expected


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([[5, 5], [6, 3], [3, 6]], 0),
        ([[2, 2], [3, 3]], 1),
        ([[1, 1], [2, 1], [2, 2], [1, 2]], 1),
        ([[1, 5], [10, 4], [4, 3]], 1)
    ],
)
def test_solution_optimized(nums, expected):
    assert SolutionOptimized().numberOfWeakCharacters(nums) == expected
