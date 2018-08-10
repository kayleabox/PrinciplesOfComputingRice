"""
Module sets up the TicTacToeBoard class that can be used
to play tictactoe
"""

from itertools import chain

EMPTY = 0
PLAYERX = 1
PLAYERO = 2
DRAW = -2

def switch_player(player):
    """
    Switch the current value of player to PLAYERX if it is PLAYERO
    or PLAYERO if it is currently PLAYERX
    """
    return PLAYERX if player == PLAYERO else PLAYERO

def convert_grid_to_list(index_grid):
    """
    Convert a two dimensional array to a one dimensional array
    """
    return list(chain(*index_grid))

def evaluate_grid_win(grid):
    """
    Returns an array with winning player in it if there is a winner
    or an empty array if there was not a winner
    """
    return [col[0] for col in grid
            if len(set(col)) == 1 and set(col) != set([EMPTY])]

def evaluate_diagonal_win(row):
    """
    Returns the player that won if there was a winner
    or None if there was not a winner
    """
    if len(set(row)) == 1 and set(row) != set([EMPTY]):
        return [row[0]]
    return []


class TicTacToeBoard(object):
    """
    Class to represent a Tic-Tac-Toe board.
    """

    def __init__(self, dimension, reverse=False, board=None):
        """
        Initialize the TTTBoard object with the given dimension and
        whether or not the game should be reversed.
        """
        self._dimension = dimension
        self._reverse = reverse
        self._board = self.new_board()

    def __str__(self):
        """
        Human readable representation of the board.
        """
        dashes = '---'*self.dimension + '-'*(self.dimension-1)

        replacements = [('[[', ' '), ('[', ''),
                        ('],', '\n'+dashes+'\n'), (', ', ' | '),
                        (']]', ''), ('0', ' '),
                        ('1', 'X'), ('2', 'O')]

        board_string = str(self.board)
        for index in replacements:
            board_string = board_string.replace(index[0], index[1])

        return board_string

    @property
    def dimension(self):
        """
        Return the dimension of the board.
        """
        return self._dimension

    @dimension.setter
    def dimension(self, value):
        """
        Set the value of dim
        """
        self._dimension = value

    @property
    def board(self):
        """
        Return the board
        """
        return self._board

    @board.setter
    def board(self, value):
        """
        Set the value of the board
        """
        self._board = value

    def new_board(self):
        """
        Generates a board of size dimension with 0's as values
        """
        return [[0 for dummy_col in range(self.dimension)]
                for dummy_row in range(self.dimension)]

    def square(self, row, col):
        """
        Returns one of the three constants EMPTY, PLAYERX, or PLAYERO
        that correspond to the contents of the board at position (row, col).
        """
        return self.board[row][col]

    def get_empty_squares(self):
        """
        Return a list of (row, col) tuples for all empty squares
        """
        index_grid = [[(row, col) for col in range(self.dimension) if self.board[row][col] == EMPTY]
                      for row in range(self.dimension)]
        return convert_grid_to_list(index_grid)

    def move(self, row, col, player):
        """
        Place player on the board at position (row, col).
        player should be either the constant PLAYERX or PLAYERO.
        Does nothing if board square is not empty.
        """
        if self.board[row][col] == EMPTY:
            self.board[row][col] = player

    def evaluate_win_status(self):
        """
        Returns a constant associated with the state of the game
        If PLAYERX wins, returns PLAYERX.
        If PLAYERO wins, returns PLAYERO.
        If game is drawn, returns DRAW.
        If game is in progress, returns None.
        """
        winning_moves = {
            "rows": evaluate_grid_win(self.board),
            "columns": evaluate_grid_win(self.column_grid()),
            "uleft_diagonal": evaluate_diagonal_win(self.uleft_bright_diagonal()),
            "bleft_diagonal": evaluate_diagonal_win(self.bleft_uright_diagonal())
        }
        for move in winning_moves:
            if winning_moves[move] != []:
                return winning_moves[move][0]

        if self.get_empty_squares() != []:
            return None
        return DRAW

    def column_grid(self):
        """
        Returns column values as rows
        """
        return [[self.board[col][row] for col in range(self.dimension)]
                for row in range(self.dimension)]

    def uleft_bright_diagonal(self):
        """
        Returns a list of the values in the diagonal from upper
        left corner to bottom right
        """
        return[self.board[dim][dim] for dim in range(self.dimension)]

    def bleft_uright_diagonal(self):
        """
        Returns a list of the values in the diagonal
        going from bottom left to upper right corner
        """
        return[self.board[self.dimension-(num+1)][num] for num in range(self.dimension)]

    def clone(self):
        """
        Return a copy of the board.
        """
        return TicTacToeBoard(self.dimension, self._reverse, self.board)
