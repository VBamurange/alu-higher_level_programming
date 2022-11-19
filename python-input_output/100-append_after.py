#!/usr/bin/python3
"""search and update"""


def append_after(filename="", search_string="", new_string=""):
    """function to append"""
    new_line = []
    with open(filename, 'r', encoding="utf-8") as Q:
        for line in Q:
            new_line += [line]
            if line.find(search_string) != -1:
                new_line += [new_string]

    with open(filename, 'w', encoding="utf-8") as Q:
        Q.write("".join(new_line))
