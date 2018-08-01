"""
Clone of 2048 game.
"""
import random

from merge import merge

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

class TwentyFortyEight(object):
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height=4, grid_width=4):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid = self.generate_empty_grid()
        self._move_grid_indices = self.generate_move_grid_indices()

    @property
    def move_grid_indices(self):
        """
        Get move_grid_indices
        """
        return self._move_grid_indices

    @move_grid_indices.setter
    def move_grid_indices(self, move_dict):
        """
        Set the value of move_grid_indices
        """
        self._move_grid_indices = move_dict

    def generate_move_grid_indices(self):
        """
        Returns a dictionary with lists of indices for each row/column
        in the grid
        """
        return {
            UP: [(0, index) for index in range(self.grid_width)],
            DOWN: [(self.grid_height - 1, index) for index in range(self.grid_width)],
            RIGHT: [(index, self.grid_width - 1) for index in range(self.grid_height)],
            LEFT: [(index, 0) for index in range(self.grid_height)]
        }

    @property
    def direction(self):
        """
        Returns the direction of the move
        """
        return self._direction
    
    @direction.setter
    def direction(self, value):
        """
        Sets the direction of the move
        """
        self._direction = value

    @property
    def grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    @property
    def grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    @property
    def grid(self):
        """
        Get the grid.
        """
        return self._grid

    @grid.setter
    def grid(self, grid):
        """
        Set the value of the game grid.
        """
        self._grid = grid

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        #self.set_grid(self.generate_empty_grid())
        [self.new_tile() for dummy_num in range(2)]

    def generate_empty_grid(self):
        """
        Generates an empty grid of the size
        _grid_height by _grid_width
        """
        return [[0 for dummy_col in range(self._grid_width)]
                for dummy_row in range(self._grid_height)]

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self.grid).replace('],', '],\n')

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        self.direction = direction

        if direction in (UP, DOWN):
            self.move_tiles(self.grid_height)
        else:
            self.move_tiles(self.grid_width)

    def move_tiles(self, height_width):
        """
        Moves tiles to their new location on the grid
        """
        new_grid = self.generate_empty_grid()
        [self.add_merged_to_grid(row, new_grid) for row in self.generate_index_grid(height_width)]
        #if self.get_grid() != new_grid:
        #    self.set_grid(new_grid)
        #    self.new_tile()
        self.grid = new_grid

    def add_merged_to_grid(self, row, new_grid):
        """
        Calls merge on each row and adds it to a placeholder grid
        """
        temp_row = merge([self.get_tile(pair[0], pair[1]) for pair in row])
        for index, value in enumerate(row):
            new_grid[value[0]][value[1]] = temp_row[index]

    def generate_index_grid(self, height_width):
        """
        Generates a grid of the indices
        """
        return [self.add_to_indices_grid(index, height_width)
                for index in self.move_grid_indices[self.direction]]

    def add_to_indices_grid(self, index, height_width):
        """
        Adds each row of indices to the grid
        """
        return [index] + self.row_indices(index[0], index[1], height_width)

    def row_indices(self, index0, index1, height_width):
        """
        Creates an array of the remaining rows of indices
        to insert into the grid
        """
        return [row_index for row_index in self.generate_row_indices(index0, index1, height_width)]

    def generate_row_indices(self, index0, index1, height_width):
        """
        Uses a generator to yield each index to be appended to the
        grid of indices
        """
        for dummy_number in range(height_width - 1):
            index0 += OFFSETS[self.direction][0]
            index1 += OFFSETS[self.direction][1]
            yield index0, index1

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        row, column = self.select_tile()
        self.set_tile(row, column, 2) if random.randint(0, 100) < 90 else self.set_tile(row, column, 4)

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
        if not self.check_tile_is_empty(row, column):
            return self.get_empty_tile(self.get_random_row_index(), self.get_random_col_index())
        return row, column

    def get_random_row_index(self):
        """
        Returns a random index between 0 and get_grid_height
        """
        return random.randint(0, self.grid_height - 1)

    def get_random_col_index(self):
        """
        Returns a random index between 0 and get_grid_width
        """
        return  random.randint(0, self.grid_width - 1)
