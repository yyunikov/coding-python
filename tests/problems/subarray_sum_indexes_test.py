import pytest

from src.problems.subarray_sum_indexes import Solution


@pytest.mark.parametrize(
    "nums,total,expected",
    [
        ([1, 2, 3], 5, [1, 2]),
        ([4, 4, 4, 5, 7, 2], 9, [2, 3]),
        ([4, 4, 4, 11, 7, 1], 9, []),
        ([4, 4, 4, 11, 7, 2], 9, [4, 5]),
        ([4, 7, 2, 11, 4, 4], 9, [1, 2]),
    ],
)
def test_solution(nums, total, expected):
    assert Solution().find_indexes_for_sum(nums, total) == expected
