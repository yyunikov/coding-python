import pytest

from src.problems.reduce_array_size_to_half import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([3, 3, 3, 3, 5, 5, 5, 2, 2, 7], 2),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
    ],
)
def test_algorithm(nums, expected):
    assert Solution().minSetSize(nums) == expected
