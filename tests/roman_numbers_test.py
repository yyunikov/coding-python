import pytest as pytest

from problems.roman_numbers import Solution


@pytest.mark.parametrize(
    "roman_number,expected",
    [
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("DCXXI", 621)
    ]
)
def test_results(roman_number, expected):
    assert expected == Solution().romanToInt(roman_number)

