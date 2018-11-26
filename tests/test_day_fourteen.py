import src.day_fourteen as day_fourteen


def test_one():
    assert day_fourteen.count_used_squares("flqrgnkx") == 8108


def test_two():
    assert day_fourteen.count_regions("flqrgnkx") == 1242
