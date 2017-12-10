#!/usr/bin/env python3
# --- Day 8: I Heard You Like Registers ---
#
# You receive a signal directly from the CPU. Because of your recent
# assistance with jump instructions, it would like you to compute the result
# of a series of unusual register instructions.
#
# Each instruction consists of several parts: the register to modify, whether
# to increase or decrease that register's value, the amount by which to
# increase or decrease it, and a condition. If the condition fails, skip the
# instruction without modifying the register. The registers all start at 0.
# The instructions look like this:
# b inc 5 if a > 1
# a inc 1 if b < 5
# c dec -10 if a >= 1
# c inc -20 if c == 10
#
# These instructions would be processed as follows:
# - Because a starts at 0, it is not greater than 1, and so b is not modified.
# - a is increased by 1 (to 1) because b is less than 5 (it is 0).
# - c is decreased by -10 (to 10) because a is now greater than or equal to 1
#   (it is 1).
# - c is increased by -20 (to -10) because c is equal to 10.
# After this process, the largest value in any register is 1.
#
# You might also encounter <= (less than or equal to) or != (not equal to).
# However, the CPU doesn't have the bandwidth to tell you what all the
# registers are named, and leaves that to you to determine.
#
# --- Part Two ---
#
# To be safe, the CPU also needs to know the highest value held in any
# register during this process so that it can decide how much memory to
# allocate to these operations. For example, in the above instructions, the
# highest value ever held was 10 (in register c after the third instruction
# was evaluated).

import re
import sys


def get_value(registers: dict, name: str) -> int:
    if name not in registers:
        return 0
    return registers[name]


def inc(registers: dict, name: str, value: int) -> None:
    current_value = get_value(registers, name)
    registers[name] = current_value + value
    return registers[name]


def dec(registers: dict, name: str, value: int) -> None:
    current_value = get_value(registers, name)
    registers[name] = current_value - value
    return registers[name]


def eq(registers: dict, name: str, value: int) -> bool:
    current_value = get_value(registers, name)
    return current_value == value


def not_eq(registers: dict, name: str, value: int) -> bool:
    current_value = get_value(registers, name)
    return current_value != value


def gr(registers: dict, name: str, value: int) -> bool:
    current_value = get_value(registers, name)
    return current_value > value


def gr_eq(registers: dict, name: str, value: int) -> bool:
    current_value = get_value(registers, name)
    return current_value >= value


def lt(registers: dict, name: str, value: int) -> bool:
    current_value = get_value(registers, name)
    return current_value < value


def lt_eq(registers: dict, name: str, value: int) -> bool:
    current_value = get_value(registers, name)
    return current_value <= value


def process(listing: str) -> (dict, int):
    operations = {
        "inc": inc,
        "dec": dec
    }
    operators = {
        "==": eq,
        "!=": not_eq,
        ">": gr,
        ">=": gr_eq,
        "<": lt,
        "<=": lt_eq
    }

    registers = {}
    max_value = 0
    regex = re.compile(r"^(\w+)\s+(inc|dec)\s+(-?\d+)\s+if\s+(\w+)\s+(>|>=|<|<=|==|!=)\s+(-?\d+)$")
    for line in listing.splitlines():
        match = regex.match(line)
        reg_op = match.group(1)
        op = match.group(2)
        diff = int(match.group(3))
        reg_comp = match.group(4)
        op_comp = match.group(5)
        value = int(match.group(6))
        if operators[op_comp](registers, reg_comp, value):
            operation_value = operations[op](registers, reg_op, diff)
            if max_value < operation_value:
                max_value = operation_value

    return registers, max_value


def max_register_value(registers: dict) -> int:
    return max(list(registers.values()))


def main():
    input_file = sys.argv[1]
    with open(input_file) as f:
        listing = f.read()

    registers, max_value = process(listing)
    print("max register value          =>", max_register_value(registers))
    print("max value during operations =>", max_value)


if __name__ == "__main__":
    main()
