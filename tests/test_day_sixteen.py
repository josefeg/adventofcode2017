import src.day_sixteen as day_sixteen


def test_one():
    dancers = "abcde"
    moves = ["s1", "x3/4", "pe/b"]
    assert day_sixteen.perform_dance(dancers, moves) == "baedc"
