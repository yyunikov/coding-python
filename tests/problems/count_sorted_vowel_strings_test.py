import pytest

from src.problems.count_sorted_vowel_strings_backtrack import Solution


@pytest.mark.parametrize(
    "num,expected",
    [
        (1, 5),
        (2, 15),
        (3, 35),
        # (33, 66045)
    ],
)
def test_solution(num, expected):
    assert Solution().countVowelStrings(num) == expected
