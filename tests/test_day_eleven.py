import src.day_eleven as day_eleven


def test_one():
    distance, _ = day_eleven.count_steps(["ne", "ne", "ne"])
    assert distance == 3

    distance, _ = day_eleven.count_steps(["ne", "ne", "sw", "sw"])
    assert distance == 0

    distance, _ = day_eleven.count_steps(["ne", "ne", "s", "s"])
    assert distance == 2

    distance, _ = day_eleven.count_steps(["se", "sw", "se", "sw", "sw"])
    assert distance == 3
