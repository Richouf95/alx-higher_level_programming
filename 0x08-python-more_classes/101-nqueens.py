#!/usr/bin/python3
"""
    N queens
"""
import sys


def is_safe(board, row, col, n):
    """
        Check if queens are safe
    """
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


def solve_n_queens_util(board, col, n, solutions):
    """
        explore all possible config
    """
    if col == n:
        solutions.append(board[:])
        return

    for row in range(n):
        if is_safe(board, row, col, n):
            board[col] = row
            solve_n_queens_util(board, col + 1, n, solutions)


def solve_n_queens(n):
    """
        initialize the table
    """
    board = [-1] * n
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions


def main():
    """
        execute program
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    z = N - 1

    solutions = solve_n_queens(N)

    for solution in solutions:
        print("[", end="")
        i = 0
        for x in solution:
            pos = solution[i]
            print("[{}, {}]".format(i, pos), end=", " if i != z else "")
            i += 1
        print("]")


if __name__ == "__main__":
    main()
