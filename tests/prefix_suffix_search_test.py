import pytest

from problems.prefix_suffix_search import WordFilter


@pytest.mark.parametrize(
    "words,prefix,suffix,expected",
    [
        (["apple"], "a", "e", 0),
        (["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"], "cabaaba","abaaaa", 0),
        (["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"], "ab","abcaccbcaa", 4),
        (["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"], "bccbacbcba","a", 9),
        (["apple","cidre"], "app", "e", 0),
        (["apple","cidre"], "ci", "e", 1),
    ]
)
def test_prefix_suffix_search(words, prefix, suffix, expected):
    assert WordFilter(words).f(prefix, suffix) == expected
