import src.day_eight as day_eight


def test_one():
    listing = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""
    registers, max_value = day_eight.process(listing)
    assert day_eight.max_register_value(registers) == 1
    assert max_value == 10
