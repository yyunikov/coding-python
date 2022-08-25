import pytest

from src.problems.ransom_note import Solution
from src.problems.ransom_note_counter import Solution as SolutionCounter



@pytest.mark.parametrize(
    "ransomNote,magazine,expected",
    [
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
        ("baa", "aab", True),
    ],
)
def test_solution(ransomNote, magazine, expected):
    assert Solution().canConstruct(ransomNote, magazine) == expected


@pytest.mark.parametrize(
    "ransomNote,magazine,expected",
    [
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
        ("baa", "aab", True),
    ],
)
def test_solution(ransomNote, magazine, expected):
    assert SolutionCounter().canConstruct(ransomNote, magazine) == expected
