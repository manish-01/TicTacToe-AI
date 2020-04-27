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
    if board == initial_state():
        return X
    count = 9
    for row in board:
        for box in row:
            if box != EMPTY:
                count -= 1
    
    if not count % 2:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    setOfActions = set()
    for i, row in enumerate(board):
        for j, box in enumerate(row):
            if box == EMPTY:
                setOfActions.add((i, j))

    return setOfActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoardState = copy.deepcopy(board)
    i, j = action
    newBoardState[i][j] = player(board)
    return newBoardState
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i, row in enumerate(board):
        if row[0] == row[1] == row[2]:
            return row[0]
    
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    
    for row in board:
        for box in row:
            if box == EMPTY:
                return False

    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    
    if board == initial_state():
        return (0,0)

    turn = player(board)
    bestAction = None
    
    if turn == X:
        v = float("-inf")
        for action in actions(board):
            minValueResult = minValue(result(board, action))
            if minValueResult > v:
                v = minValueResult
                bestAction = action

    elif turn == O:
        v = float("inf")
        for action in actions(board):
            maxValueResult = maxValue(result(board, action))
            if maxValueResult < v:
                v = maxValueResult
                bestAction = action

    return bestAction



def maxValue(board):
    if terminal(board):
        return utility(board)
    v = -1
    max_action = -1
    for action in actions(board):
        v = max(v, minValue(result(board, action)))
    return v

def minValue(board):
    if terminal(board):
        return utility(board)
    v = 1
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
    return v