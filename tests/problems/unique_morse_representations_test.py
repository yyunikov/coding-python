import pytest

from src.problems.unique_morse_representations import Solution


@pytest.mark.parametrize(
    "words,expected",
    [
        (["gin", "zen", "gig", "msg"], 2),
    ],
)
def test_solution(words, expected):
    assert Solution().uniqueMorseRepresentations(words) == expected
