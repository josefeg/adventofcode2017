import src.day_one as day_one


def test_one():
    assert day_one.solve("1122") == 3


def test_two():
    assert day_one.solve("1111") == 4


def test_three():
    assert day_one.solve("1234") == 0


def test_four():
    assert day_one.solve("91212129") == 9
