#!/usr/bin/python3

def pow(a, b):
    """Function to compute a to the power of b using a loop."""
    if b == 0:
        return 1  # Any number to the power of 0 is 1
    elif b < 0:
        a = 1 / a  # Take the reciprocal for negative powers
        b = -b  # Make b positive
    
    result = 1
    for _ in range(b):
        result *= a  # Multiply a, b times
    
    return result
