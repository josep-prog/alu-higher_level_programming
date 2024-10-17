#!/usr/bin/python3

def pow(a, b):
    """Function to compute a to the power of b using recursion."""
    if b == 0:
        return 1  # Base case: any number to the power of 0 is 1
    elif b < 0:
        return 1 / pow(a, -b)  # Handle negative powers

    return a * pow(a, b - 1)  # Recursive case


# Example usage
if __name__ == "__main__":
    print(pow(2, 2))     # Output: 4
    print(pow(98, 2))    # Output: 9604
    print(pow(98, 0))    # Output: 1
    print(pow(100, -2))  # Output: 0.0001
    print(pow(-4, 5))    # Output: -1024
