import pytest

from src.problems.longest_substr_with_two_dist_chars import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("eceba", 3),
        ("ccaabbb", 5),
        ("ababcbcbaaabbdef", 6),
    ]
)
def test_solution(s, expected):
    assert Solution().lengthOfLongestSubstringTwoDistinct(s) == expected
