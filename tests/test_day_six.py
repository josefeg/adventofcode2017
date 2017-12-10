import src.day_six as day_six


def test_one():
    initial_state = [0, 2, 7, 0]
    cycles, size = day_six.count_redesitribuition_cycles(initial_state)
    assert cycles == 5
    assert size == 4
