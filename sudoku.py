import numpy as np

sudoku_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def possible(y, x, n):
    global sudoku_board
    for i in range(0, 9):
        if sudoku_board[y][i] == n:
            return False
    for i in range(0, 9):
        if sudoku_board[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku_board[y0 + i][x0 + j] == n:
                return False
    return True


def solver():
    global sudoku_board
    for y in range(9):
        for x in range(9):
            if sudoku_board[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        sudoku_board[y][x] = n
                        solver()
                        sudoku_board[y][x] = 0
                return
    print(np.matrix(sudoku_board))


solver()
