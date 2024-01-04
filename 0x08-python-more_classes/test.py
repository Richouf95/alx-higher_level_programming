#!/usr/bin/python3

def print_solution(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    # Vérifier la ligne sur la gauche
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Vérifier la diagonale supérieure sur la gauche
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Vérifier la diagonale inférieure sur la gauche
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens_util(board, col, n):
    if col == n:
        print_solution(board)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 'Q'
            solve_n_queens_util(board, col + 1, n)
            board[i][col] = '.'

def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solve_n_queens_util(board, 0, n)

# Exemple d'utilisation avec un échiquier 4x4
solve_n_queens(4)

