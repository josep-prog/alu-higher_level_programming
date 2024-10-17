#!/usr/bin/python3
# Author - JOSEPH Nishimwe

def uppercase(str):
    """Function to print a string in uppercase."""
    result = []
    for char in str:
        if 'a' <= char <= 'z':
            # Convert to uppercase and add to the list
            result.append(chr(ord(char) - 32))
        else:
            result.append(char)  # Keep the character as is
    # Join the list into a string and print it
    print("{}".format("".join(result)))

# Example usage
uppercase("best")
uppercase("Best School 98 Battery street")
