"""
Tic Tac Toe Player
"""

import math
import copy

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

    for row in board:
        for cell in row:
            if cell == O:
                o += 1
            if cell == X:
                x += 1

    if x == 0:
        return X
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
    if board[action[0]][action[1]] == EMPTY:
        symbol = player(board)
        board_cpy = copy.deepcopy(board)
        board_cpy[action[0]][action[1]] = symbol

        return board_cpy

    else:
        raise Exception('Invalid Move')


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in board:
        # player has compleated a row
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O

    if (board[0][0] == board[1][0] == board[2][0] == O) or (
            board[0][1] == board[1][1] == board[2][1] == O) or (
            board[0][2] == board[1][2] == board[2][2] == O) or (
            board[0][2] == board[1][1] == board[2][0] == O) or (
            board[0][0] == board[1][1] == board[2][2] == O):
        return O

    elif (board[0][0] == board[1][0] == board[2][0] == X) or (
            board[0][1] == board[1][1] == board[2][1] == X) or (
            board[0][2] == board[1][2] == board[2][2] == X) or (
            board[0][2] == board[1][1] == board[2][0] == X) or (
            board[0][0] == board[1][1] == board[2][2] == X):
        return X

    else:
        # tie
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        win_player = winner(board)

        if win_player is None:
            # tie
            return 0
        elif win_player == X:
            return 1
        else:
            return -1

    return


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    symbol = player(board)
    moves = []

    if terminal(board):
        return None
    else:
        if symbol == X:
            for action in actions(board):
                moves.append([min_value(result(board, action)), action])
                moves.sort(key=lambda x: x[0], reverse=True)
        else:
            for action in actions(board):
                moves.append([max_value(result(board, action)), action])
                moves.sort(key=lambda x: x[0])

        return moves[0][1]


def min_value(board):
    """
    Returns the best move for the min player 'O'.
    """
    if terminal(board):
        return utility(board)

    value = math.inf
    for action in actions(board):
        val = max_value(result(board, action))
        value = min(value, val)

    return value


def max_value(board):
    """
    Returns the best move for the max player 'X'.
    """
    if terminal(board):
        return utility(board)

    value = -math.inf
    for action in actions(board):
        val = min_value(result(board, action))
        value = max(value, val)

    return value
