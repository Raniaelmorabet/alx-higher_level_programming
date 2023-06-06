#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """
    Check if it is safe to place a queen at board[row][col]
    """
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col, solutions):
    """
    Recursive function to solve the N queens problem using backtracking
    """
    if col >= N:
        # All queens are successfully placed, add the solution to the list
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for row in range(N):
        if is_safe(board, row, col):
            # Place the queen at board[row][col]
            board[row][col] = 1

            # Move to the next column
            solve_nqueens(board, col + 1, solutions)

            # Backtrack and remove the queen from board[row][col]
            board[row][col] = 0


if __name__ == "__main__":
    # Check the number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get N from command-line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check the value of N
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty chessboard
    board = [[0] * N for _ in range(N)]

    # Solve the N queens problem
    solutions = []
    solve_nqueens(board, 0, solutions)

    # Print the solutions
    for solution in solutions:
        print(solution)
