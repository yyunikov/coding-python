import pytest

from src.problems.merge_intervals import Solution


@pytest.mark.parametrize(
    "intervals,expected",
    [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[1, 4], [2, 3]], [[1, 4]]),
        ([[1, 3], [0, 2], [2, 3], [4, 6], [4, 5], [5, 5], [0, 2], [3, 3]],
         [[0, 3], [4, 6]])
    ],
)
def test_solution(intervals, expected):
    assert Solution().merge(intervals) == expected
