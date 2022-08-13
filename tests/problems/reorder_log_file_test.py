import pytest

from src.problems.reorder_log_file import Solution


@pytest.mark.parametrize(
    "log,expected",
    [
        (["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art "
                                                                       "zero"],
          ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]),
    ],
)
def test_solution(log, expected):
    assert Solution().reorderLogFiles(log) == expected
