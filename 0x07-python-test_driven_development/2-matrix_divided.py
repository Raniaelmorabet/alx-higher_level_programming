#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    A function that divides matrix elements.

    Args:
        matrix (list): Contains the elements that are going to be divided by `div`.
        div (int or float): The dividing number.

    Raises:
        TypeError: If `matrix` is not a list of lists or if each row of the matrix
                   does not have the same size.
        TypeError: If `div` is not an integer or float.
        ZeroDivisionError: If `div` is equal to 0.

    Returns:
        list: A new matrix with elements divided by `div` and rounded to 2 decimal places.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix
