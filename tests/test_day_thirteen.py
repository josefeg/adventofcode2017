import src.day_thirteen as day_thirteen


def test_one():
    lines = [
        "0: 3",
        "1: 2",
        "4: 4",
        "6: 4"
    ]
    assert day_thirteen.get_severity(lines) == 24


def test_two():
    lines = [
        "0: 3",
        "1: 2",
        "4: 4",
        "6: 4"
    ]
    assert day_thirteen.find_smallest_delay(lines) == 10
