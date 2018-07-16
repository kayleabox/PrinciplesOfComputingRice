    def generate_index_grid(self, height_width):
        """
        Generates a grid of the indices
        """
        indices_grid = []
        for index in self.get_move_grid_indices()[self.get_direction()]:
            temp = [index]
            self.generate_row_indices(index[0], index[1], temp, height_width)
            indices_grid.append(temp)
        return indices_grid

    def generate_row_indices(self, index0, index1, temp, height_width):
        for dummy_number in range(height_width - 1):
            index_tuple = self.increment_by_offset(index0, index1)
            temp.append(index_tuple)

    def increment_by_offset(self, index0, index1):
        return (index0 + OFFSETS[self.get_direction()][0], index1 + OFFSETS[self.get_direction()][1])



    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        if direction in (UP, DOWN):        
            self.move_tiles(direction, self.get_grid_height())
        else:
            self.move_tiles(direction, self.get_grid_width())


    def move_tiles(self, direction, height_width):
        """
        Implements merge and moves tiles
        """
        new_grid = self.generate_empty_grid()
        for row in self.generate_index_grid(direction, height_width):
            temp_row = [self.get_grid()[pair[0]][pair[1]] for pair in row]
            temp_row = merge(temp_row)
            for index in range(len(row)):
                new_grid[row[index][0]][row[index][1]] = temp_row [index]
        if self.get_grid() != new_grid:
            self.set_grid(new_grid)
            self.new_tile()

    def generate_index_grid(self, direction, height_width):
        """
        Generates a grid of the indices
        """
        indices_grid = []
        for index in self.get_move_grid_indices()[direction]:
            temp = [index]
            index0 = index[0]
            index1 = index[1]
            for dummy_number in range(height_width - 1):
                index0 += OFFSETS[direction][0]
                index1 += OFFSETS[direction][1]
                temp.append((index0, index1))
            indices_grid.append(temp)
        return indices_grid