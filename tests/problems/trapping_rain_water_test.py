import pytest

from src.problems.trapping_rain_water import Solution


@pytest.mark.parametrize(
    "height,expected",
    [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([5, 4, 1, 2], 1),
        ([9,6,8,8,5,6,3], 3)
    ],
)
def test_solution(height, expected):
    assert Solution().trap(height) == expected
