#!/usr/bin/python3
# Author - Joseph Nishimwe

combinations = []
for digit1 in range(10):
    for digit2 in range(digit1 + 1, 10):
        combinations.append("{:02}{:02}".format(digit1, digit2))

# Join all combinations with ', ' and print
print(", ".join(combinations))
