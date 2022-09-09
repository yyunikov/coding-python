from src.problems.complete_hand_tiles import complete


def test_complete_tile():
    tiles1 = "88844"
    tiles2 = "99"
    tiles3 = "55555"
    tiles4 = "22333333"
    tiles5 = "73797439949499477339977777997394947947477993"
    tiles6 = "111333555"
    tiles7 = "42"
    tiles8 = "888"
    tiles9 = "100100000"
    tiles10 = "346664366"
    tiles11 = "8999998999899"
    tiles12 = "17610177"
    tiles13 = "600061166"
    tiles14 = "6996999"
    tiles15 = "03799449"
    tiles16 = "64444333355556"

    assert complete(tiles1)
    assert complete(tiles2)
    assert complete(tiles3)
    assert complete(tiles4)
    assert complete(tiles5)
    assert not complete(tiles6)
    assert not complete(tiles7)
    assert not complete(tiles8)
    assert not complete(tiles9)
    assert not complete(tiles10)
    assert not complete(tiles11)
    assert not complete(tiles12)
    assert not complete(tiles13)
    assert not complete(tiles14)
    assert not complete(tiles15)
    assert not complete(tiles16)
