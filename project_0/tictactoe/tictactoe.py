"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0

    if empty_board(board):
        return X

    for row in board:
        for cell in row:
            if cell == O:
                o += 1
            if cell == X:
                x += 1

    if x > o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                possible_actions.append((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if empty_board(board):
        return False

    for row in board:
        # player has compleated a row
        if (row.count(X) or row.count(O)) == 3:
            return True

    if (board[0][0] == board[1][0] == board[2][0]) or (board[0][1] == board[1][1] == board[2][1]) or (
            board[0][2] == board[1][2] == board[2][2]) or (board[0][0] == board[1][1] == board[2][2]):
        return True

    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError


def empty_board(board):
    """
    Returns True if the board is empty, False otherwise
    """
    for row in board:
        if not row == [EMPTY, EMPTY, EMPTY]:
            return False

    return True
