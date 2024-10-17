#!/usr/bin/python3
# Author - JOSEPH Nishimwe

def uppercase(str):
    """Function to print a string in uppercase."""
    result = ""
    for char in str:
        if 'a' <= char <= 'z':  # Check if the character is lowercase
            result += chr(ord(char) - (ord('a') - ord('A')))  # Convert to uppercase
        else:
            result += char  # Keep the character as is
    print("{}".format(result))

# Example usage
uppercase("best")
uppercase("Best School 98 Battery street")
