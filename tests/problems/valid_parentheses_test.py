import pytest

from src.problems.valid_parentheses import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("(())", True),
        ("[", False),
        ("]", False),
    ]
)
def test_solution(s, expected):
    assert Solution().isValid(s) == expected
