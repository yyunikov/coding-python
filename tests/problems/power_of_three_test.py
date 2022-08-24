import pytest

from src.problems.power_of_three import Solution
from src.problems.power_of_three_elegant import Solution as SolutionElegant


@pytest.mark.parametrize(
    "num,expected",
    [
        (1, True),
        (3, True),
        (2, False),
        (9, True),
        (15, False),
        (16, False),
        (27, True),
        (12, False),
        (81, True),
        (1162261467, True),
    ],
)
def test_solution(num, expected):
    assert Solution().isPowerOfThree(num) == expected


@pytest.mark.parametrize(
    "num,expected",
    [
        (1, True),
        (3, True),
        (2, False),
        (9, True),
        (15, False),
        (16, False),
        (27, True),
        (12, False),
        (81, True),
        (1162261467, True),
    ],
)
def test_solution_elegant(num, expected):
    assert SolutionElegant().isPowerOfThree(num) == expected
