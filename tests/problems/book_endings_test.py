from src.problems.book_endings import findEnding


def test_book_endings():
    assert findEnding([25, 26], [[3, 16, 24], [17, 2, 25]], 1) == -1
    assert findEnding([25, 26], [[3, 16, 24], [17, 2, 25]], 2) == 25
    assert findEnding([21, 30, 40], [[9, 16, 26], [14, 16, 13], [27, 29, 28], [28, 15, 34], [29, 30, 38]], 1) == 21
    assert findEnding([21, 30, 40], [[9, 16, 26], [13, 31, 14], [14, 16, 13], [27, 12, 24], [32, 34, 15]], 2) == -1
