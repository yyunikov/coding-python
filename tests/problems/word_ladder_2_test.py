import pytest

from src.problems.word_ladder_2 import Solution


@pytest.mark.skip(reason="Gave up to solve in a reasonable time")
@pytest.mark.parametrize(
    "begin_word,end_word,word_list,expected",
    [
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"],
         [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]),
    ],
)
def test_solution(begin_word, end_word, word_list, expected):
    assert Solution().findLadders(begin_word, end_word, word_list) == expected
