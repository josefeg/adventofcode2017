#!/usr/bin/env python3
# --- Day 16: Permutation Promenade ---
# You come upon a very unusual sight; a group of programs here appear to be
# dancing.
#
# There are sixteen programs in total, named a through p. They start by
# standing in a line: a stands in position 0, b stands in position 1, and so
# on until p, which stands in position 15.
#
# The programs' dance consists of a sequence of dance moves:
# - Spin, written sX, makes X programs move from the end to the front, but
#   maintain their order otherwise. (For example, s3 on abcde produces cdeab).
# - Exchange, written xA/B, makes the programs at positions A and B swap
#   places.
# - Partner, written pA/B, makes the programs named A and B swap places.
#
# For example, with only five programs standing in a line (abcde), they could
# do the following dance:
# - s1, a spin of size 1: eabcd.
# - x3/4, swapping the last two programs: eabdc.
# - pe/b, swapping programs e and b: baedc.
#
# After finishing their dance, the programs end up in order baedc.
#
# You watch the dance for a while and record their dance moves (your puzzle
# input). In what order are the programs standing after their dance?
#
# --- Part Two ---
# Now that you're starting to get a feel for the dance moves, you turn your
# attention to the dance as a whole.
#
# Keeping the positions they ended up in from their previous dance, the
# programs perform it again and again: including the first dance, a total of
# one billion (1000000000) times.
#
# In the example above, their second dance would begin with the order baedc,
# and use the same dance moves:
# s1, a spin of size 1: cbaed.
# x3/4, swapping the last two programs: cbade.
# pe/b, swapping programs e and b: ceadb.
#
# In what order are the programs standing after their billion dances?
#

import re
import string
import sys


def swap(string: str, p1: int, p2: int) -> string:
    src = min(p1, p2)
    target = max(p1, p2)
    return string[0:src] + string[target] + string[src+1:target] + string[src] + string[target+1:]


def perform_dance(dancers: str, moves: list) -> str:
    pattern = re.compile(r"([sxp])(\d{1,2}|[a-p])(?:/(\d{1,2}|[a-p]))?")
    for move in moves:
        match = pattern.match(move)
        operator = match.group(1)
        if operator == "s":
            operand = int(match.group(2))
            dancers = dancers[-operand:] + dancers[0:-operand]
        elif operator == "x":
            op1 = int(match.group(2))
            op2 = int(match.group(3))
            dancers = swap(dancers, op1, op2)
        elif operator == "p":
            op1 = match.group(2)
            op2 = match.group(3)
            dancers = swap(dancers, dancers.index(op1), dancers.index(op2))
    return dancers


def after_billion_dances(original_lineup: str, moves: list) -> str:
    iterations = 0
    dancers = original_lineup
    while True:
        dancers = perform_dance(dancers, moves)
        iterations += 1
        if dancers == string.ascii_lowercase[:16]:
            break

    req_iterations = 1000000000 % iterations
    for i in range(req_iterations):
        dancers = perform_dance(dancers, moves)

    return dancers


def main():
    input_file = sys.argv[1]
    with open(input_file) as f:
        moves = f.read().strip().split(",")

    dancers = string.ascii_lowercase[:16]
    print("after 1 dance    =>", perform_dance(dancers, moves))
    print("after 1bn dances =>", after_billion_dances(dancers, moves))


if __name__ == "__main__":
    main()
