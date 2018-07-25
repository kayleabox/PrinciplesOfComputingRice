"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
#import poc_ttt_gui
#import poc_ttt_provided as provided
import cv_tictactoe_board as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 100         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.
def mc_trial(board,player):
    """
    This function takes a current board and the next player to move.
    The function should play a game starting with the given player
    by making random moves, alternating between players. The function
    should return when the game is over. The modified board will
    contain the state of the game, so the function does not return
    anything. In other words, the function should modify the board input.
    """
    while not board.check_win():
        random_square = random.randint(0, len(board.get_empty_squares())) - 1
        row, col = board.get_empty_squares()[random_square]
        board.move(row, col, player)
        player = provided.switch_player(player)
    
def mc_update_scores(scores,board,player):
    """
    This function takes a grid of scores (a list of lists) with
    the same dimensions as the Tic-Tac-Toe board, a board from a
    completed game, and which player the machine player is. The
    function should score the completed board and update the scores
    grid. As the function updates the scores grid directly,
    it does not return anything.
    """
    if not board.check_win() == provided.DRAW:
        apply_score(scores, board, player)

def get_score_values(board, player):
    """
    Return the values to score each players moves with
    """
    if player == board.check_win():
        return SCORE_CURRENT, -SCORE_OTHER
    else:
        return -SCORE_CURRENT, SCORE_OTHER    

def apply_score(scores, board, player):
    """
    Add the scores to the scores grid
    """
    def update_tile_scores(): 
        """
        Update an individual tile in the scores board
        """
        if board.square(row, col) == player:
            scores[row][col] += score_current
        elif not board.square(row, col) == provided.EMPTY:
            scores[row][col] += score_other  
    
    score_current, score_other = get_score_values(board, player)

    [[update_tile_scores() for col in range(board.get_dim())] 
    for row in range(board.get_dim())]
            
    # for row in range(board.get_dim()):
    #     for col in range(board.get_dim()):
            # if board.square(row, col) == player:
            #     scores[row][col] += score_current
            # elif not board.square(row, col) == provided.EMPTY:
            #     scores[row][col] += score_other
    
# def update_tile_scores(board, scores, row, col, player, score_current, score_other): 
#     #I don't like that I am passing in soooo many parameters
#     #I will keep working on a refactor
#     """
#     Update an individual tile in the scores board
#     """
#     if board.square(row, col) == player:
#         scores[row][col] += score_current
#     elif not board.square(row, col) == provided.EMPTY:
#         scores[row][col] += score_other   

def get_best_move(board,scores):
    """
    This function takes a current board and a grid of scores.
    The function should find all of the empty squares with the
    maximum score and randomly return one of them as a (row,column)
    tuple. It is an error to call this function with a board that
    has no empty squares (there is no possible next move), so your
    function may do whatever it wants in that case. The case where
    the board is full will not be tested.
    """
    if len(board.get_empty_squares()) > 0:
        high_scores = get_high_score(board, scores)
        return select_random_highest_tile(high_scores)

def get_high_score(board, scores):
    """
    Generates a list of the indices high scores to choose from
    """
    high_scores = []
    high_index = board.get_empty_squares()[0]
    highest_score = scores[high_index[0]][high_index[1]]

    for index in board.get_empty_squares():
        high_scores, highest_score = update_high_scores(scores[index[0]][index[1]], index, highest_score, high_scores)
    return high_scores    
    
def update_high_scores(score, index, highest_score, high_scores):
    """
    Checks to see if the current tile is a high score for the remaining open
    tiles and returns it if it is or returns the list of high scores
    if it is not a new high score
    """
    if score == highest_score:
        return high_scores + [index], highest_score
    elif score > highest_score:
        highest_score = score
        return [index], highest_score
    return high_scores, highest_score

def select_random_highest_tile(high_scores):
    """
    Returns a randomly selected index for an open tile
    in the list of high scores
    """
    random_square = random.randint(0, len(high_scores) - 1)
    row, column = high_scores[random_square]
    return (row, column)

def mc_move(board,player,trials):
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
    scores = [[0 for dummy_col in range(board.get_dim())] for dummy_row in range(board.get_dim())]
    [score_trial(board, player, scores) for dummy_num in range(trials)]
    return scores

def score_trial(board, player, scores):
    """
    Set up and score a single trial
    """
    trial_board = board.clone()
    mc_trial(trial_board, player)
    mc_update_scores(scores, trial_board, player)    
