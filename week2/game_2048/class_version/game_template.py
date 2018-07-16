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
    merged_line = []
    
    try_merge(line_without_zeros, merged_line)
    while len(line) - len(merged_line) > 0:
        merged_line.append(0)
    return merged_line;

def try_merge(line_wo_zeros, merged_line):
    """
    Attempts to merge each number in an array with the one after it.
    If the number was already merged with the one before it, 
    no merge will occur.
    """
    merged_w_previous = False
    for index in range(len(line_wo_zeros)):
        if index < len(line_wo_zeros) - 1 and line_wo_zeros[index] == line_wo_zeros[index + 1]:
            merged_w_previous = merge_if_not_merged(merged_w_previous, merged_line, line_wo_zeros, index)
        else: 
            merged_w_previous = append_to_line_if_not_merged(merged_w_previous, merged_line, line_wo_zeros, index)

def merge_if_not_merged(merged_with_previous, merged_line, line_without_zeros, index):
    """
    Merges the number at the current index with the number 
    at index + 1 if the number at index has not been merged
    already. Then appends the merged number to a placeholder.
    """
    if merged_with_previous == False:
        merged_line.append(line_without_zeros[index] + line_without_zeros[index + 1])
        return True
    else:
        return False

def append_to_line_if_not_merged(merged_with_previous, merged_line, line_without_zeros, index):
    """
    Appends numbers that are not eligible for merging with their
    neighbors to the placeholder array.
    """
    if merged_with_previous != True:
        merged_line.append(line_without_zeros[index])
    return False

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
        self._direction = value

    def get_direction(self):
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
            temp_row = [self.get_grid()[pair[0]][pair[1]] for pair in row]
            temp_row = merge(temp_row)
            for index in range(len(row)):
                new_grid[row[index][0]][row[index][1]] = temp_row [index]
        #if self.get_grid() != new_grid:
        #    self.set_grid(new_grid)
        #    self.new_tile()
        self.set_grid(new_grid)

    def generate_index_grid(self, height_width):
        """
        Generates a grid of the indices
        """
        return [ self.add_to_indices_grid(index, height_width) 
                         for index in self.get_move_grid_indices()[self.get_direction()]]

    def add_to_indices_grid(self, index, height_width):
        """
        Adds each row of indices to the grid
        """
        temp = [index]
        self.generate_row_indices(index[0], index[1], temp, height_width)
        return temp

    def generate_row_indices(self, index0, index1, temp, height_width):
        """
        Generates each row of indices to insert into the grid
        """
        for dummy_number in range(height_width - 1):
            index0 += OFFSETS[self.get_direction()][0]
            index1 += OFFSETS[self.get_direction()][1]
            temp.append((index0, index1))

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        row, column = self.select_tile_index()
        self.set_tile(row, column, 2) if random.randint(0,100) < 90 else self.set_tile(row, column, 4)

    def check_tile_is_empty(self, row, col):
        """
        Takes in a row and column and returns True
        if the value of grid[row, column] == 0  
        """
        return self.get_tile(row, col) == 0

    def select_tile_index(self):
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
        while self.check_tile_is_empty(row, column) == False:
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
