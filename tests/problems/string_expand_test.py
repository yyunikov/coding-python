import pytest

from src.problems.string_expand import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("xy3[abc]zy", "xyabcabcabczy"),
        ("xy3[a4[b]c]ab2[baaa]zy", "xyabbbbcabbbbcabbbbcabbaaabaaazy")
    ],
)
def test_solution(s, expected):
    assert Solution().expandString(s) == expected
