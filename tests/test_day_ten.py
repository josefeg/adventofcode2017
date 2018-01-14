import src.day_ten as day_ten


def test_one():
    lengths = [3, 4, 1, 5]
    numbers, _, _ = day_ten.calculate_hash_round(lengths, [0, 1, 2, 3, 4])
    assert (numbers[0] * numbers[1]) == 12


def test_two():
    assert day_ten.calculate_hash("") == "a2582a3a0e66e6e86e3812dcb672a272"
    assert day_ten.calculate_hash("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"
    assert day_ten.calculate_hash("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"
    assert day_ten.calculate_hash("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"
