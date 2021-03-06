"""
Monte Carlo Tic-Tac-Toe Player
"""

import random

from tictactoe_board import (DRAW, EMPTY, switch_player)

SCORE = 1.0

def mc_trial(board, player):
    """
    This function takes a current board and the next player to move.
    The function should play a game starting with the given player
    by making random moves, alternating between players. The function
    should return when the game is over. The modified board will
    contain the state of the game, so the function does not return
    anything. In other words, the function should modify the board input.
    """
    if board.evaluate_win_status():
        return None
    row, col = get_random_move(board)
    board.move(row, col, player)
    return mc_trial(board, switch_player(player))

def get_random_move(board):
    """
    Return the index of a random open tile on the board
    """
    random_square = random.randint(0, len(board.get_empty_squares())) - 1
    return board.get_empty_squares()[random_square]

def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores (a list of lists) with
    the same dimensions as the Tic-Tac-Toe board, a board from a
    completed game, and which player the machine player is. The
    function should score the completed board and update the scores
    grid. As the function updates the scores grid directly,
    it does not return anything.
    """
    if board.evaluate_win_status() != DRAW:
        apply_score(scores, board, player)

def get_score_values(board, player):
    """
    Return the values to score each players moves with
    """
    if player == board.evaluate_win_status():
        return SCORE, -SCORE
    return -SCORE, SCORE

def apply_score(scores, board, player):
    """
    Add the scores to the scores grid
    """
    def update_tile_scores(row, col):
        """
        Update an individual tile in the scores board
        """
        if board.square(row, col) == player:
            scores[row][col] += score_current
        elif board.square(row, col) != EMPTY:
            scores[row][col] += score_other

    score_current, score_other = get_score_values(board, player)

    return [[update_tile_scores(row, col) for col in range(board.dimension)]
            for row in range(board.dimension)]

def get_best_move(board, scores):
    """
    This function takes a current board and a grid of scores.
    The function should find all of the empty squares with the
    maximum score and randomly return one of them as a (row,column)
    tuple. It is an error to call this function with a board that
    has no empty squares (there is no possible next move), so your
    function may do whatever it wants in that case. The case where
    the board is full will not be tested.
    """
    if board.get_empty_squares():
        high_scores = get_high_score(board, scores)
        return select_random_highest_tile(high_scores)
    return None

def get_high_score(board, scores):
    """
    Generates a list of the indices high scores to choose from
    """
    available_scores = [scores[index[0]][index[1]] for index in board.get_empty_squares()]
    max_score = max(available_scores)
    return [index for index in board.get_empty_squares() if scores[index[0]][index[1]] == max_score]

def select_random_highest_tile(high_scores):
    """
    Returns a randomly selected index for an open tile
    in the list of high scores
    """
    random_square = random.randint(0, len(high_scores) - 1)
    row, column = high_scores[random_square]
    return (row, column)

def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine
    player is, and the number of trials to run. The function
    should use the Monte Carlo simulation described above to return
    a move for the machine player in the form of a (row,column) tuple.
    Be sure to use the other functions you have written!
    """
    scores = run_set_of_trials(board, player, trials)
    return get_best_move(board, scores)

def run_set_of_trials(board, player, trials):
    """
    Run set number of trials on the given board
    """
    scores = [[0 for dummy_col in range(board.dimension)] for dummy_row in range(board.dimension)]
    for dummy_num in range(trials):
        score_trial(board, player, scores)
    return scores

def score_trial(board, player, scores):
    """
    Set up and score a single trial
    """
    trial_board = board.clone()
    mc_trial(trial_board, player)
    mc_update_scores(scores, trial_board, player)
