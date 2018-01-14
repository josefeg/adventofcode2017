import src.day_nine as day_nine


def test_one():
    assert day_nine.calculate_score("{}") == 1
    assert day_nine.calculate_score("{{{}}}") == 6
    assert day_nine.calculate_score("{{},{}}") == 5
    assert day_nine.calculate_score("{{{},{},{{}}}}") == 16
    assert day_nine.calculate_score("{<a>,<a>,<a>,<a>}") == 1
    assert day_nine.calculate_score("{{<ab>},{<ab>},{<ab>},{<ab>}}") == 9
    assert day_nine.calculate_score("{{<!!>},{<!!>},{<!!>},{<!!>}}") == 9
    assert day_nine.calculate_score("{{<a!>},{<a!>},{<a!>},{<ab>}}") == 3


def test_two():
    assert day_nine.remove_garbage("<>") == 0
    assert day_nine.remove_garbage("<random characters>") == 17
    assert day_nine.remove_garbage("<<<<>") == 3
    assert day_nine.remove_garbage("<{!>}>") == 2
    assert day_nine.remove_garbage("<!!>") == 0
    assert day_nine.remove_garbage("<!!!>>") == 0
    assert day_nine.remove_garbage("<{o\"i!a,<{i<a>") == 10
