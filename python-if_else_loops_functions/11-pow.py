#!/usr/bin/python3

def pow(a, b):
    """Function to compute a to the power of b using recursion."""
    if b == 0:
        return 1  # Base case: any number to the power of 0 is 1
    elif b < 0:
        return 1 / pow(a, -b)  # Handle negative powers
    
    return a * pow(a, b - 1)  # Recursive case
