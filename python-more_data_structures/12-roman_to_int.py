#!/usr/bin/python3


def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer."""
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def helper(index):
        if index >= len(roman_string):
            return 0
        current_value = roman_values[roman_string[index]]
        if index + 1 < len(roman_string) and current_value < roman_values[roman_string[index + 1]]:
            return -current_value + helper(index + 1)
        else:
            return current_value + helper(index + 1)

    return helper(0)
