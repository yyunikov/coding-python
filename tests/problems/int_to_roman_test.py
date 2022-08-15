import pytest

from src.problems.int_to_roman import Solution
from src.problems.int_to_roman_simplified_recursive import Solution as SolutionSimplifiedRecursive
from src.problems.int_to_roman_simplified import Solution as SolutionSimplified


@pytest.mark.parametrize(
    "num,expected",
    [
        (3, "III"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
        (621, "DCXXI"),
        (2000, "MM")
    ],
)
def test_solution(num, expected):
    assert Solution().intToRoman(num) == expected


@pytest.mark.parametrize(
    "num,expected",
    [
        (3, "III"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
        (621, "DCXXI"),
        (2000, "MM")
    ],
)
def test_solution_simplified_recursive(num, expected):
    assert SolutionSimplifiedRecursive().intToRoman(num) == expected


@pytest.mark.parametrize(
    "num,expected",
    [
        (3, "III"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
        (621, "DCXXI"),
        (2000, "MM")
    ],
)
def test_solution_simplified(num, expected):
    assert SolutionSimplified().intToRoman(num) == expected
