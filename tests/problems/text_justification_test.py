import pytest

from src.problems.text_justification import Solution


@pytest.mark.parametrize(
    "words,max_width,expected",
    [
        (["This", "is", "an", "example", "of", "text", "justification."], 16,
         ["This    is    an", "example  of text", "justification.  "]),
        (["What", "must", "be", "acknowledgment", "shall", "be"], 16,
         ["What   must   be", "acknowledgment  ", "shall be        "]),
        (["Science", "is", "what", "we", "understand", "well", "enough", "to",
          "explain", "to", "a", "computer.", "Art", "is", "everything", "else",
          "we", "do"], 20,
         ["Science  is  what we", "understand      well",
          "enough to explain to", "a  computer.  Art is",
          "everything  else  we", "do                  "]),
    ],
)
def test_solution(words, max_width, expected):
    assert Solution().fullJustify(words, max_width) == expected
