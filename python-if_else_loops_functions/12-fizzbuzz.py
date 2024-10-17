#!/usr/bin/python3
"""Print the numbers from 1 to 100 separated by a space.
#For numbers that are divisible by three, output "Fizz" in place of the number.
#For numbers that are divisible by five, output "Buzz" instead of the number.
#For numbers that are divisible by both three and five, output "FizzBuzz" in lieu of the number.

  """


def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
