import pytest

from src.problems.word_ladder_2 import Solution


@pytest.mark.parametrize(
    "begin_word,end_word,word_list,expected",
    [
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"],
        [['hit', 'hot', 'lot', 'log', 'cog'], ['hit', 'hot', 'dot', 'dog', 'cog']]),
        (
           "hit", "cog", ["hot", "dot", "dog", "lot", "log"], []
        ),
        ("a", "c", ["a", "b", "c"], [["a", "c"]])
    ],
)
def test_solution(begin_word, end_word, word_list, expected):
    assert Solution().findLadders(begin_word, end_word, word_list) == expected
