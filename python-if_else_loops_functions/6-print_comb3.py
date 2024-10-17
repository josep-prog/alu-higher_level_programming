#!/usr/bin/python3
# Author - Joseph Nishimwe

for digit1 in range(10):
    for digit2 in range(digit1 + 1, 10):
        print("{}{}".format(digit1, digit2), end=", " if not (digit1 == 8 and digit2 == 9) else "\n")
