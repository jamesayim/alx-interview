#!/usr/bin/python3
"""
N Queens Puzzle
"""

import sys

def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at a given position
    """
    # Check for queens in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, n):
    """
    Solve N Queens using backtracking
    """
    if row == n:
        # All queens are placed, print the solution
        print([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n)

def nqueens(n):
    """
    Main function to solve N Queens problem
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize an empty board
    board = [-1] * n

    # Start solving from the first row (row 0)
    solve_nqueens(board, 0, n)

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    try:
        # Convert the argument to an integer
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Call the main function to solve N Queens
    nqueens(n)

