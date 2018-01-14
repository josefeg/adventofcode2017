import src.day_twelve as day_twelve


def test_one():
    lines = [
        "0 <-> 2",
        "1 <-> 1",
        "2 <-> 0, 3, 4",
        "3 <-> 2, 4",
        "4 <-> 2, 3, 6",
        "5 <-> 6",
        "6 <-> 4, 5",
    ]
    network = day_twelve.build_network(lines)
    connected = day_twelve.b.find_connected_to(network, "0")
    assert len(connected) == 6


def test_two():
    lines = [
        "0 <-> 2",
        "1 <-> 1",
        "2 <-> 0, 3, 4",
        "3 <-> 2, 4",
        "4 <-> 2, 3, 6",
        "5 <-> 6",
        "6 <-> 4, 5",
    ]
    assert day_twelve.count_groups(lines) == 2
