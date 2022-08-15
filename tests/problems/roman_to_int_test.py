import pytest as pytest

from src.problems.roman_to_int import Solution
from src.problems.roman_to_int_simplified import Solution as SolutionSimplified


@pytest.mark.parametrize(
    "roman_number,expected",
    [("III", 3), ("LVIII", 58), ("MCMXCIV", 1994), ("DCXXI", 621)],
)
def test_solution(roman_number, expected):
    assert expected == Solution().romanToInt(roman_number)


@pytest.mark.parametrize(
    "roman_number,expected",
    [("III", 3), ("LVIII", 58), ("MCMXCIV", 1994), ("DCXXI", 621)],
)
def test_solution_simplified(roman_number, expected):
    assert expected == SolutionSimplified().romanToInt(roman_number)
