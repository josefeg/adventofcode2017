import src.day_one as day_one


def test_captcha():
    assert day_one.captcha("1122") == 3
    assert day_one.captcha("1111") == 4
    assert day_one.captcha("1234") == 0
    assert day_one.captcha("91212129") == 9


def test_captcha2():
    assert day_one.captcha2("1212") == 6
    assert day_one.captcha2("1221") == 0
    assert day_one.captcha2("123425") == 4
    assert day_one.captcha2("123123") == 12
    assert day_one.captcha2("12131415") == 4
