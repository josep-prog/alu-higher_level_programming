#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """Load and return an object from a JSON file.

    Args:
        filename (str): The name of the file to load from.

    Returns:
        object: The Python object represented by the JSON data in the file.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        content = file.read()
        return json.loads(content)
