import pytest

from src.problems.string_expand import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("a2[b]c", "abbc"),
        ("ab2[abc]dd", "ababcabcdd"),
        ("ab1[a2[b]c]ab3[ba]dd", "ababbcabbababadd")
    ],
)
def test_solution(s, expected):
    assert Solution().expandString(s) == expected
