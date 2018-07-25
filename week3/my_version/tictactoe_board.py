"""
Module sets up the TicTacToeBoard class that can be used
to play tictactoe
"""

EMPTY = 0
PLAYERX = 1
PLAYERO = 2
DRAW = -2
PLAYER = {
    "playerx": 1,
    "playero": 2
}

def switch_player(player):
    if player == PLAYERO:
        return PLAYERX
    return PLAYERO

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
        if self.board[row][col] == 1:
            return PLAYERX
        elif self.board[row][col] == 2:
            return PLAYERO
        return EMPTY

    def get_empty_squares(self):
        """
        Return a list of (row, col) tuples for all empty squares
        """
        index_grid = [[(row, col) for col in range(self.dimension) if self.board[row][col] == EMPTY]
                      for row in range(self.dimension)]
        index_list = []
        for l_list in index_grid:
            index_list += l_list
        return index_list

    def move(self, row, col, player):
        """
        Place player on the board at position (row, col).
        player should be either the constant PLAYERX or PLAYERO.
        Does nothing if board square is not empty.
        """
        if self.board[row][col] == EMPTY:
            self.board[row][col] = player

    def check_win(self):
        """
        Returns a constant associated with the state of the game
        If PLAYERX wins, returns PLAYERX.
        If PLAYERO wins, returns PLAYERO.
        If game is drawn, returns DRAW.
        If game is in progress, returns None.
        """
        game_checks = {
            "rows": self.check_grid(self.board),
            "columns": self.check_grid(self.column_grid()),
            "uleft_diagonal": self.check_diagonal(self.uleft_bright()),
            "bleft_diagonal": self.check_diagonal(self.bleft_uright())
        }
        for check in game_checks:
            if game_checks[check] != []:
              return game_checks[check][0]
        
        if len(self.get_empty_squares()) > 0:
            return 
        return DRAW

    def column_grid(self):
        """
        Returns column values as rows
        """
        return [[self.board[col][row] for col in range(self.dimension)]
                for row in range(self.dimension)]


    # def check_rows(self):
    #     """
    #     Checks to see if there is a winning row
    #     """
    #     return [row[0] for row in self.board
    #             if len(set(row)) == 1 and set(row) != set([EMPTY])]

    def check_grid(self, grid):
        """
        Returns an array with winning player in it if there is a winner
        or an empty array if there was not a winner
        """
        return [col[0] for col in grid
                if len(set(col)) == 1 and not set(col) == set([EMPTY])]

    def check_diagonal(self, row):
        """
        Returns the player that won if there was a winner
        or None if there was not a winner
        """
        if len(set(row)) == 1 and not set(row) == set([EMPTY]):
            return [row[0]]
        return []

    # def check_columns(self):
    #     """
    #     Checks to see if there is a winning column
    #     """
    #     return [col[0] for col in self.column_grid()
    #             if len(set(col)) == 1 and not set(col) == set([EMPTY])]

    def uleft_bright(self):
        """
        Returns a list of the values in the diagonal from upper
        left corner to bottom right
        """
        return[self.board[dim][dim] for dim in range(self.dimension)]

    def bleft_uright(self):
        """
        Returns a list of the values in the diagonal
        going from bottom left to upper right corner
        """
        return[self.board[self.dimension-(num+1)][num] for num in range(self.dimension)]

    def clone(self):
        """
        Return a copy of the board.
        """
        return self.board[:]


