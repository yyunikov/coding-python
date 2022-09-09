from src.problems.hit_counter import HitCounter


def test_hit_counter():
    hit_counter = HitCounter()
    hit_counter.hit(1)
    hit_counter.hit(2)
    hit_counter.hit(3)

    assert hit_counter.getHits(4) == 3

    hit_counter.hit(300)
    assert hit_counter.getHits(300) == 4
    assert hit_counter.getHits(301) == 3
