#!/usr/bin/env python3
# --- Day 7: Recursive Circus ---
#
# Wandering further through the circuits of the computer, you come upon a
# tower of programs that have gotten themselves into a bit of trouble. A
# recursive algorithm has gotten out of hand, and now they're balanced
# precariously in a large tower.
#
# One program at the bottom supports the entire tower. It's holding a large
# disc, and on the disc are balanced several more sub-towers. At the bottom of
# these sub-towers, standing on the bottom disc, are other programs, each
# holding their own disc, and so on. At the very tops of these
# sub-sub-sub-...-towers, many programs stand simply keeping the disc below
# them balanced but with no disc of their own.
#
# You offer to help, but first you need to understand the structure of these
# towers. You ask each program to yell out their name, their weight, and (if
# they're holding a disc) the names of the programs immediately above them
# balancing on that disc. You write this information down (your puzzle input).
# Unfortunately, in their panic, they don't do this in an orderly fashion; by
# the time you're done, you're not sure which program gave which information.
#
# For example, if your list is the following:
# pbga (66)
# xhth (57)
# ebii (61)
# havc (66)
# ktlj (57)
# fwft (72) -> ktlj, cntj, xhth
# qoyq (66)
# padx (45) -> pbga, havc, qoyq
# tknk (41) -> ugml, padx, fwft
# jptl (61)
# ugml (68) -> gyxo, ebii, jptl
# gyxo (61)
# cntj (57)
# ...then you would be able to recreate the structure of the towers that looks
# like this:
#
#                 gyxo
#               /
#          ugml - ebii
#        /      \
#       |         jptl
#       |
#       |         pbga
#      /        /
# tknk --- padx - havc
#      \        \
#       |         qoyq
#       |
#       |         ktlj
#        \      /
#          fwft - cntj
#               \
#                 xhth
# In this example, tknk is at the bottom of the tower (the bottom program),
# and is holding up ugml, padx, and fwft. Those programs are, in turn, holding
# up other programs; in this example, none of those programs are holding up
# any other programs, and are all the tops of their own towers. (The actual
# tower balancing in front of you is much larger.)
#
# Before you're ready to help them, you need to make sure your information is
# correct. What is the name of the bottom program?
#
# --- Part Two ---
#
# The programs explain the situation: they can't get down. Rather, they could
# get down, if they weren't expending all of their energy trying to keep the
# tower balanced. Apparently, one program has the wrong weight, and until it's
# fixed, they're stuck here.
#
# For any program holding a disc, each program standing on that disc forms a
# sub-tower. Each of those sub-towers are supposed to be the same weight, or
# the disc itself isn't balanced. The weight of a tower is the sum of the
# weights of the programs in that tower.
#
# In the example above, this means that for ugml's disc to be balanced, gyxo,
# ebii, and jptl must all have the same weight, and they do: 61.
#
# However, for tknk to be balanced, each of the programs standing on its disc
# and all programs above it must each match. This means that the following
# sums must all be the same:
# - ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
# - padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
# - fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243
#
# As you can see, tknk's disc is unbalanced: ugml's stack is heavier than the
# other two. Even though the nodes above ugml are balanced, ugml itself is too
# heavy: it needs to be 8 units lighter for its stack to weigh 243 and keep
# the towers balanced. If this change were made, its weight would be 60.
#
# Given that exactly one program is the wrong weight, what would its weight
# need to be to balance the entire tower?

import sys
import collections


class Node:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight
        self.__children = []

    @property
    def name(self) -> str:
        return self.__name

    @property
    def weight(self) -> int:
        return self.__weight

    @property
    def children(self) -> list:
        return self.__children

    @property
    def total_weight(self) -> int:
        return self.__total_weight

    @total_weight.setter
    def total_weight(self, total_weight) -> None:
        self.__total_weight = total_weight

    def add_child(self, child) -> None:
        self.__children.append(child)


def get_program_name(line: str) -> str:
    return line.split()[0]


def get_weight(line: str) -> int:
    start = line.index("(") + 1
    end = line.index(")")
    return int(line[start:end])


def get_subprograms(line: str) -> list:
    if line.find("->") < 0:
        return []
    return list(map(lambda x: x.strip(), line[line.index("->")+2:].split(",")))


def find_root(listing: list) -> str:
    programs = []
    children = []
    for line in listing:
        programs.append(get_program_name(line))
        subprograms = get_subprograms(line)
        if len(subprograms) > 0:
            children.extend(subprograms)

    for program in programs:
        if program not in children:
            return program


def build_tree(directory: dict, root: str) -> Node:
    elem = directory[root]
    node = Node(root, elem["weight"])

    total_weight = node.weight
    for subprogram in elem["subprograms"]:
        child_node = build_tree(directory, subprogram)
        total_weight += child_node.total_weight
        node.add_child(child_node)
    node.total_weight = total_weight

    return node


def parse_listing(listing: list) -> Node:
    directory = {}
    for line in listing:
        name = get_program_name(line)
        weight = get_weight(line)
        subprograms = get_subprograms(line)
        directory[name] = {
            "weight": weight,
            "subprograms": subprograms
        }

    root_name = find_root(listing)
    return build_tree(directory, root_name)


def find_unbalanced_child(root: Node, ideal_weight=0) -> (Node, int):
    weights = list(map(lambda n: n.total_weight, root.children))
    most_common = collections.Counter(weights).most_common()
    if len(most_common) == 1:
        difference = ideal_weight - (root.total_weight - root.weight)
        return root, difference

    for child in root.children:
        if child.total_weight == most_common[1][0]:
            return find_unbalanced_child(child, most_common[0][0])


def main():
    input_file = sys.argv[1]
    with open(input_file) as f:
        listing = f.readlines()

    root = parse_listing(listing)
    _, ideal_weight = find_unbalanced_child(root)
    print("bottom program                     =>", root.name)
    print("ideal weight of unbalanced element =>", ideal_weight)


if __name__ == "__main__":
    main()
