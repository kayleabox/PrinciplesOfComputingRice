"""
Clone of 2048 game.
"""
import random

#import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    line_without_zeros = [value for value in line if value != 0]
    return (try_merge(line_without_zeros) +
           [0 for dummy_num in range(len(line) - len(line_without_zeros))])

def try_merge(line_wo_zeros):
    """
    Attempts to merge each number in an array with the one after it.
    If the number was already merged with the one before it, 
    no merge will occur.
    """
    return [ get_new_value(line_wo_zeros, index, value) for index, value in enumerate(line_wo_zeros)]

def get_new_value(line_wo_zeros, index, value):
    """
    Return the value multiplied by 2 if it can be merged with the next one 
    and remove the element at the next index
    Return the value if it cannot be merged with the next one
    """
    if index < len(line_wo_zeros) - 1 and value == line_wo_zeros[index + 1]:
        line_wo_zeros.pop(index + 1)
        return value * 2 
    return value

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height = 4, grid_width = 4):
        # replace with your code
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid = self.generate_empty_grid()
        self._move_grid_indices = self.generate_move_grid_indices()

    def set_move_grid_indices(self, move_dict):
        """
        Set the value of move_grid_indices
        """
        self._move_grid_indices = move_dict

    def get_move_grid_indices(self):
        """
        Get move_grid_indices
        """
        return self._move_grid_indices

    def generate_move_grid_indices(self):
        """
        Returns a dictionary with lists of indices for each row/column
        in the grid
        """    
        return {
            UP: [(0, index) for index in range(self.get_grid_width())],
            DOWN: [(self.get_grid_height() - 1, index) for index in range(self.get_grid_width())],
            RIGHT: [(index, self.get_grid_width() - 1) for index in range(self.get_grid_height())],
            LEFT: [(index, 0) for index in range(self.get_grid_height())]
        }

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._grid_width

    def get_grid(self):
        """
        Get the grid.
        """
        return self._grid

    def set_grid(self, grid):
        """
        Set the value of the game grid.
        """
        self._grid = grid

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._grid[row][col]

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        #self.set_grid(self.generate_empty_grid())
        for dummy_num in range(2):
            self.new_tile()

    def generate_empty_grid(self):
        """
        Generates an empty grid of the size
        _grid_height by _grid_width
        """
        return [[ 0 for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return str(self.get_grid()).replace('],', '],\n')

    def set_direction(self, value):
        """
        Sets the direction of the move
        """
        self._direction = value

    def get_direction(self):
        """
        Returns the direction of the move
        """
        return self._direction

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        self.set_direction(direction)

        if direction in (UP, DOWN):        
            self.move_tiles(self.get_grid_height())
        else:
            self.move_tiles(self.get_grid_width())

    def move_tiles(self, height_width):
        """
        Implements merge and moves tiles to their new location on the grid
        """
        new_grid = self.generate_empty_grid()
        for row in self.generate_index_grid(height_width):
            self.add_merged_to_temp_grid(row, new_grid)
        #if self.get_grid() != new_grid:
        #    self.set_grid(new_grid)
        #    self.new_tile()
        self.set_grid(new_grid)

    def add_merged_to_temp_grid(self, row, new_grid):
        temp_row = merge([self.get_grid()[pair[0]][pair[1]] for pair in row])
        for index, value in enumerate(row):
            new_grid[value[0]][value[1]] = temp_row [index]

    def generate_index_grid(self, height_width):
        """
        Generates a grid of the indices
        """
        return [self.add_to_indices_grid(index, height_width) 
                for index in self.get_move_grid_indices()[self.get_direction()]]

    def add_to_indices_grid(self, index, height_width):
        """
        Adds each row of indices to the grid
        """
        return [index] + self.generate_row_indices(index[0], index[1], height_width)

    def generate_row_indices(self, index0, index1, height_width):
        """
        Generates each row of indices to insert into the grid
        """
        temp = []
        for dummy_number in range(height_width - 1):
            index0 += OFFSETS[self.get_direction()][0]
            index1 += OFFSETS[self.get_direction()][1]
            temp.append((index0, index1))
        return temp

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        row, column = self.select_tile()
        self.set_tile(row, column, 2) if random.randint(0,100) < 90 else self.set_tile(row, column, 4)

    def check_tile_is_empty(self, row, col):
        """
        Takes in a row and column and returns True
        if the value of grid[row, column] == 0  
        """
        return self.get_tile(row, col) == 0

    def select_tile(self):
        """
        Returns a tuple with a randomly selected coordinate 
        pair in the grid that has a current value of 0
        """
        return self.get_empty_tile(self.get_random_row_index(), self.get_random_col_index())

    def get_empty_tile(self, row, column):
        """
        Takes in the indexes of a tile in the grid and returns
        it if it has a value of 0, if not it returns the 
        indexes of a tile that does have a value of 0.
        """
        while not self.check_tile_is_empty(row, column):
            row, column = self.get_random_row_index(), self.get_random_col_index()
        return row, column

    def get_random_row_index(self):
        """
        Returns a random index between 0 and get_grid_height
        """
        return random.randint(0, self.get_grid_height() - 1)

    def get_random_col_index(self):
        """
        Returns a random index between 0 and get_grid_width
        """
        return  random.randint(0, self.get_grid_width() - 1)



#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
