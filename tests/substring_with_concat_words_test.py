import pytest

from problems.substring_with_concat_words import Solution


@pytest.mark.parametrize(
    "s,words,expected",
    [
        ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], [])
    ],
)
def test_solution(s, words, expected):
    assert Solution().findSubstring(s, words) == expected
