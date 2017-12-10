import src.day_four as day_four


def test_one():
    assert day_four.has_no_duplicates("aa bb cc dd ee")
    assert not day_four.has_no_duplicates("aa bb cc dd aa")
    assert day_four.has_no_duplicates("aa bb cc dd aaa")


def test_two():
    assert day_four.has_no_anagrams("abcde fghij")
    assert not day_four.has_no_anagrams("abcde xyz ecdab")
    assert day_four.has_no_anagrams("a ab abc abd abf abj")
    assert day_four.has_no_anagrams("iiii oiii ooii oooi oooo")
    assert not day_four.has_no_anagrams("oiii ioii iioi iiio")
