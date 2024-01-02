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
    # raise NotImplementedError
    x_count = 0
    o_count = 0
    user = X
    for row in board:
        for item in row:
            if item == X:
                x_count += 1
            if item == O:
                o_count += 1
    if x_count > o_count:
        user = O
    return user


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i, row in board:
        for j, item in row:
            if item == EMPTY:
                action.add((i, j))


    print("action", action)
    raise NotImplementedError
    # return X


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    print("board-result", board)
    print("board-result", action)
    print("board:", board)
    print("action:", action)
    user = player(board)
    board[action[0]][action[1]] = player(board)
    print("board:", board)
    # raise NotImplementedError
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    win = None
    score = utility(board)
    if score == 1:
        win = X
    elif score == -1:
        win = O

    return win


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # raise NotImplementedError

    is_teminal = False
    score = utility(board)
    if score == 1 or score == -1 or minimax(board) == None:
        is_teminal = True

    return is_teminal


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # print("utility(board)", board)
    score = 0
    for i in range(3):
        # print(i)
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][0] == X:
                score = 1
                break
            elif board[i][0] == O:
                score = -1
                break

        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[0][i] == X:
                score = 1
                break;
            elif board[0][i] == O:
                score = -1
                break;

    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        if board[1][1] == X:
            score = 1
        elif board[1][1] == O:
            score = -1

    if (board[2][0] == board[1][1] and board[1][1] == board[0][2]):
        if board[1][1] == X:
            score = 1
        elif board[1][1] == O:
            score = -1

    # raise NotImplementedError
    for row in board:
        print(row)
    print("score:", score)
    return score


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    user = player(board)
    fair = set()
    win = set()
    minimx_action = None
    print("minimax action ===============")
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY :
                # temp_board = board
                temp_board = copy.deepcopy(board)
                temp_board[i][j] = user
                # print("temp_board:", temp_board)
                score = utility(temp_board)
                # print("user, score:", user, score)
                if user == X and score == 1:
                    # win.add(i)
                    # win.add(j)
                    win = (i, j)
                    print("win:", win)
                    break
                elif user == O and score == -1:
                    # win.add(i)
                    # win.add(j)
                    win = (i, j)
                    print("win:", win)
                    break
                elif score == 0 and len(fair) == 0:
                    # fair.add(i)
                    # fair.add(j)
                    fair = (i, j)
                    print("fair:", fair)
    if len(win) > 0:
        minimx_action = win
    elif len(fair) > 0:
        minimx_action = fair
    print("minimax action:", minimx_action)
    # raise NotImplementedError
    return minimx_action
