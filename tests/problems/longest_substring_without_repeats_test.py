import pytest

from src.problems.longest_substring_without_repeats import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
    ]
)
def test_solution(s, expected):
    assert Solution().lengthOfLongestSubstring(s) == expected
