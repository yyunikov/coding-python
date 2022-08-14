import pytest

from src.problems.maximum_subarray import max_sub_array


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([-2, -3, 4, -1, -2, 5, -3], 6),
        ([-1], -1)
    ],
)
def test_algorithm(nums, expected):
    assert max_sub_array(nums) == expected