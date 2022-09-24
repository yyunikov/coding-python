import pytest

from src.problems.remove_intervals import Solution


@pytest.mark.parametrize(
    "intervals,removal_interval,expected",
    [
        ([[0, 2], [3, 4], [5, 7]], [1, 6], [[0, 1], [6, 7]]),
        ([[0, 5]], [2, 3], [[0, 2], [3, 5]]),
        ([[-5, -4], [-3, -2], [1, 2], [3, 5], [8, 9]], [-1, 4],
         [[-5, -4], [-3, -2], [4, 5], [8, 9]]),
        ([[0, 100]], [0, 50], [[50, 100]]),
        ([[-1000, 1000]], [-1000, 1000], []),
    ],
)
def test_solution(intervals, removal_interval, expected):
    assert Solution().removeInterval(intervals, removal_interval) == expected
