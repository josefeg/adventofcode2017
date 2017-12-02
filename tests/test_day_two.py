import src.day_two as day_two


def test_checksum():
    input = """5 1 9 5
7 5 3
2 4 6 8"""
    assert day_two.checksum(input) == 18
