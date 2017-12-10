import src.day_three as day_three


def test_one():
    assert day_three.manhattan_distance(1) == 0
    assert day_three.manhattan_distance(12) == 3
    assert day_three.manhattan_distance(23) == 2
    assert day_three.manhattan_distance(1024) == 31


def test_two():
    assert day_three.next_value_after(4) == 5
    assert day_three.next_value_after(147) == 304
    assert day_three.next_value_after(11) == 23
    assert day_three.next_value_after(747) == 806
