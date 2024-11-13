#!/usr/bin/python3
"""Module containing the function read_file"""


def read_file(filename=""):
    """Reads a file and prints to stdout, line by line.

    Args:
        filename (str, optional): name of file to read. Defaults to "".
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
