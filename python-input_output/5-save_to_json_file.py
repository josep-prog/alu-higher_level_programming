#!/usr/bin/python3
import json

def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using JSON representation.

    Args:
        my_obj (type): Object to write to text file.
        filename (str): name of the file.
    """
    # Use json.dump to serialize and write the object to the file
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

