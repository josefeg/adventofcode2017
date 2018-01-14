#!/usr/bin/env python3
# --- Day 11: Hex Ed ---
# Crossing the bridge, you've barely reached the other side of the stream when
# a program comes up to you, clearly in distress. "It's my child process," she
# says, "he's gotten lost in an infinite grid!"
#
# Fortunately for her, you have plenty of experience with infinite grids.
#
# Unfortunately for you, it's a hex grid.
#
# The hexagons ("hexes") in this grid are aligned such that adjacent hexes can
# be found to the north, northeast, southeast, south, southwest, and northwest:
#
#   \ n  /
# nw +--+ ne
#   /    \
# -+      +-
#   \    /
# sw +--+ se
#   / s  \
#
# You have the path the child process took. Starting where he started, you
# need to determine the fewest number of steps required to reach him. (A
# "step" means to move from the hex you are in to any adjacent hex.)
#
# For example:
#
# ne,ne,ne is 3 steps away.
# ne,ne,sw,sw is 0 steps away (back where you started).
# ne,ne,s,s is 2 steps away (se,se).
# se,sw,se,sw,sw is 3 steps away (s,s,sw).
#
# --- Part Two ---
#
# How many steps away is the furthest he ever got from his starting position?

import sys


def count_steps(path: list) -> int:
    # ref: https://www.redblobgames.com/grids/hexagons/#distances
    x = 0
    y = 0
    z = 0
    max_distance = 0
    for step in path:
        if step == "n":
            y += 1
            z -= 1
        elif step == "ne":
            x += 1
            z -= 1
        elif step == "nw":
            x -= 1
            y += 1
        elif step == "s":
            y -= 1
            z += 1
        elif step == "se":
            x += 1
            y -= 1
        elif step == "sw":
            x -= 1
            z += 1

        current_distance = ((abs(x) + abs(y) + abs(z)) // 2)
        if current_distance > max_distance:
            max_distance = current_distance

    return ((abs(x) + abs(y) + abs(z)) // 2), max_distance


def main():
    input_file = sys.argv[1]
    with open(input_file) as f:
        path = f.read().strip().split(",")

    steps, max_distance = count_steps(path)
    print("steps        =>", steps)
    print("max distance =>", max_distance)


if __name__ == "__main__":
    main()
