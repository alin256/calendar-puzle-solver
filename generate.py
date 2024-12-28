import numpy as np

import utils

class Field:
    def __init__(self, rows=None, cols=None, init_grid=None):
        if cols is not None and rows is not None:
            self.rows = rows
            self.cols = cols
            # crearte a grid is numpy array of bool
            self.grid = np.array([[False for _ in range(cols)] for _ in range(rows)], dtype=bool)
            return
        elif init_grid is not None:
            self.rows = len(init_grid)
            self.cols = len(init_grid[0])
            self.grid = np.array(init_grid, dtype=bool)
            return
        else:
            # raise an error
            raise ValueError("Invalid arguments")   

    def encode_to_int64(self):
        # arr = np.full((8, 8), True, dtype=bool)
        # arr[:self.rows, :self.cols] = self.grid
        # return int(''.join([str(int(x)) for x in arr.flatten()]), 2)
        return Field.encode_nd_array_to_int64(self.grid)



    @staticmethod
    def decode_field_from_int64(num, num_rows=8, num_cols=8):
        grid = Field.decode_from_int64(num, num_rows, num_cols)
        return Field(init_grid=grid)

    def fill_cells(self, row, col, num_rows=1, num_cols=1):
        if num_rows is None and num_cols is None:
            if 0 <= row < self.rows and 0 <= col < self.cols:
                self.grid[row][col] = True
            else:
                raise ValueError("Cell position out of bounds")
        else:
            if 0 <= row and row+num_rows <= self.rows \
                    and 0 <= col and col+num_cols <= self.cols:
                for i in range(num_rows):
                    for j in range(num_cols):
                        self.grid[row + i][col + j] = True
            else:
                raise ValueError("Cell position out of bounds")

    def fill(self, pattern, start_row, start_col):
        pattern_rows = len(pattern)
        pattern_cols = len(pattern[0]) if pattern else 0
        # create a deep copy of the current drid in numpy
        grid_copy = np.copy(self.grid)

        # todo change to [:] assignment
        for i in range(pattern_rows):
            for j in range(pattern_cols):
                if pattern[i][j]:
                    # check if the cell is already filled
                    if self.is_filled(start_row + i, start_col + j):
                        return None
                    grid_copy[start_row + i, start_col + j] = True
        # remove the first row if all cells are filled
        while np.all(grid_copy[0]):
            grid_copy = grid_copy[1:, :]
        #remove the first column if all cells are filled
        while np.all(grid_copy[:, 0]):
            grid_copy = grid_copy[:, 1:]
        return Field(init_grid=grid_copy)

    def is_filled(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid[row][col]
        else:
            raise ValueError("Cell position out of bounds")

    def fill_rotations(self, pattern, start_row, start_col):
        # create a deep copy of the current grid in numpy
        grid_copy = np.copy(self.grid)
        for _ in range(4):
            new_field = self.fill(pattern, start_row, start_col)
            if new_field is not None:
                return new_field
            self.rotate()



    def __str__(self):
        return '\n'.join([' '.join(['X' if cell else '.' for cell in row]) for row in self.grid])

# Example usage
if __name__ == "__main__":
    field = Field(init_grid=[[True, False], 
                             [True, True],
                             [True, False],
                             [True, False],
                             [True, False]])


    exit()    

    field = Field(7, 7)
    field.fill_cells(0, 6, 2, 1)
    field.fill_cells(6, 3, 1, 4)
    print(field)
    field_id = field.encode_to_int64()
    print(field_id)
    new_field = Field.decode_from_int64(field_id)
    print(new_field)

    exit()

    new_field = field.fill([[True, True], [True, True]], 2, 2)
    print(new_field)
