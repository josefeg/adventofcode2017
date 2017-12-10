import src.day_five as day_five


def test_one():
    instructions = [0, 3, 0, 1, -3]
    assert day_five.find_steps_for_exit(instructions[:]) == 5
    assert day_five.find_steps_for_exit(instructions[:], True) == 10
