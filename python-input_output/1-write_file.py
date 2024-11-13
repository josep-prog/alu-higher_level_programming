#!/usr/bin/python3
"""Module containing the function write_file"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename (str, optional): name of the file. Defaults to "".
        text (str, optional): string of text to write to file. Defaults to "".

    Returns:
        int: number of characters written to file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        lines = [text]  # Wrap text in a list to use writelines
        f.writelines(lines)  # Write the list to the file
        return sum(len(line) for line in lines)  # Return the total length of written characters
