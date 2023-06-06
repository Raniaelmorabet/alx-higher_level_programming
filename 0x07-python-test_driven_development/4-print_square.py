#!/usr/bin/python3
def print_square(size):
    """prints a square using #

    Args:
        size (int): length of square

    Raises:
        TypeError: if size is not an integer, or if size is a float
            and is less than 0
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) or size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
