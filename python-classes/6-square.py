#!/usr/bin/python3


"""Defines a class Square"""


class Square:
    """
    Class that defines properties of a square.

    Attributes:
        size: size of the square (1 side).
        position: position of the square in a 2D space.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Creates new instances of square.

        Args:
            size (int): size of the square (1 side).
            position (tuple): position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size.

        Args:
            value (int): size of the square (1 side).

        Raises:
            TypeError: size must be an integer.
            ValueError: size must be >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Property setter for position.

        Args:
            value (tuple): position of the square.

        Raises:
            TypeError: position must be a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square.

        Returns: the current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #."""
        if self.__size == 0:
            print()
        else:
            # Print the vertical position (y-axis)
            for _ in range(self.__position[1]):
                print()  # Print empty lines for vertical position
            # Print the square
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
