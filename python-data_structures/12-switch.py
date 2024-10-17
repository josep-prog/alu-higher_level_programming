#!/usr/bin/python3
a = 89
b = 10
temp = a  # Use a temporary variable to hold the value of a
a = b
b = temp
print("a={:d} - b={:d}".format(a, b))
