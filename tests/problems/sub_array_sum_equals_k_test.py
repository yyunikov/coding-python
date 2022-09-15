import pytest

from src.problems.sub_array_sum_equals_k import Solution
from src.problems.sub_array_sum_equals_k_2 import Solution as Solution2
from src.problems.sub_array_sum_equals_k_optimal import Solution as SolutionOptimal

test_cases = [
    ([1, 1, 1], 2, 2),
    ([1, 2, 3], 3, 2),
    ([1], 0, 0),
    ([-1, -1, 1], 0, 1),
    ([1, -1, 0], 0, 3)
]


@pytest.mark.parametrize(
    "nums,k,expected",
    test_cases,
)
def test_solution(nums, k, expected):
    assert Solution().subarraySum(nums, k) == expected


@pytest.mark.parametrize(
    "nums,k,expected",
    test_cases,
)
def test_solution_2(nums, k, expected):
    assert Solution2().subarraySum(nums, k) == expected


@pytest.mark.parametrize(
    "nums,k,expected",
    test_cases,
)
def test_solution_optimal(nums, k, expected):
    assert SolutionOptimal().subarraySum(nums, k) == expected
