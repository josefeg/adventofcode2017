import src.day_seven as day_seven


def test_one():
    listing = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""

    root = day_seven.parse_listing(listing.splitlines())
    assert root.name == "tknk"
    _, ideal_weight = day_seven.find_unbalanced_child(root)
    assert ideal_weight == 60
