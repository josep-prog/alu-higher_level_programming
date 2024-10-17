#!/usr/bin/python3

def print_last_digit(number):
    """Prints and returns the last digit of a number."""
    last_digit = abs(number) % 10  # Get the last digit
    print(last_digit)  # Print the last digit
    return last_digit  # Return the last digit
