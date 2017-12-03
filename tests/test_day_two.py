import src.day_two as day_two


def test_checksum():
    input = """5 1 9 5
7 5 3
2 4 6 8"""
    assert day_two.checksum(input) == 18


def test_checksum2():
    input = """5 9 2 8
9 4 7 3
3 8 6 5"""
    assert day_two.checksum2(input) == 9
