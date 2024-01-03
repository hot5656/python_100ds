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
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item == EMPTY:
                action.add((i, j))
    # raise NotImplementedError
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    user = player(board)
    board_run = copy.deepcopy(board)
    board_run[action[0]][action[1]] = player(board)
    return board_run


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

    is_teminal = False
    empty_count = 0
    for row in board:
        for item in row:
            if item == EMPTY:
                empty_count += 1

    score = utility(board)
    if score == 1 or score == -1 or empty_count == 0:
        is_teminal = True

    return is_teminal


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    score = 0
    for i in range(3):
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

    return score

def score_count(board) :
    user = player(board)
    if user == X:
        score = -100
    else:
        score = 100

    if terminal(board):
        return utility(board)

    all_actions = actions(board)
    for action in all_actions:
        next = result(board, action)
        run_score = score_count(next)
        if user == X:
            if run_score > score:
                score = run_score
                if score == 1:
                    break
        else:
            if run_score < score:
                score = run_score
                if score == -1:
                    break
    return  score

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    user = player(board)
    minimx_action = None
    if user == X:
        score = -1
    else:
        score = 1
    # print("minimax action ===============")
    all_aictions = actions(board)
    # print("action", all_aictions)
    for action in all_aictions:
          next = result(board, action)
          run_score = score_count(next)
        #   print("action, score:", action, run_score)
          if user == X:
              if run_score > score:
                  score = run_score
                  minimx_action = action
                  if score == 1:
                      break
          else:
              if run_score < score:
                  score = run_score
                  minimx_action = action
                  if score == -1:
                      break
    return minimx_action

