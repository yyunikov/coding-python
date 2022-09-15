import pytest

from src.problems.sub_array_sum_equals_k_positives import Solution


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([1], 0, 0)
    ],
)
def test_solution(nums, k, expected):
    assert Solution().subarraySum(nums, k) == expected
