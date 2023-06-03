#!/usr/bin/python3
"""Module for add_integer method"""

def add_integer(a, b=98):
    """
    adds two integers
    args :
            a = first integer
            b = second integer with a default number 98
    raises  : TypeError: if a and b are neither integers or floats
    returns : the addition of a and b
    """
    if type(a) not in (int, float):
         raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
if __name__ == '__main__':
    import doctest
doctest.testfile("tests/0-add_integer.txt")