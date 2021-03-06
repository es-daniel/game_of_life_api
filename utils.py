from random import randint
import numpy as np
import json

ALIVE = 1
DEAD = 0


class Utils:

    def __init__(self):
        self.temp_grid = []
        self.grid = []

    # This method creates initial pattern
    # @param grid is the current grid
    def seed(self, grid):
        for row in grid:
            for i in range(2):
                self.rand_living_cell(row)

    # This method add random living cells for the initial pattern
    # @param row is the current row of the pattern
    def rand_living_cell(self, row):
        row[randint(5, 15)] = ALIVE

    # This method creates a new grid

    def build_new_grid(self, rows, columns):
        return [[DEAD] * columns for _ in range(rows)]

    def gosper_glider_gun(self):
        grid = open('gosper_glider_gun.json')
        return json.load(grid)

    def pulsar(self):
        grid = open('pulsar.json')
        return json.load(grid)

    # This method update teh grid
    def update_grid(self, grid):
        self.grid = grid
        self.temp_grid = self.build_new_grid(len(grid), len(grid[0]))
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                self.update_cell(i, j, cell, self.count_neighbors(i, j, row))
        return self.temp_grid

    # This method update de current cells
    # @param axis_i == current row index
    # @param axis_j == current cell index
    # @param cell == current cell
    # @cell_neighbors ==  number of cell's neighbors
    def update_cell(self, axis_i, axis_j, cell, cell_neighbors):
        if (cell == ALIVE and cell_neighbors in [2, 3]) or (cell == DEAD and cell_neighbors == 3):
            self.temp_grid[axis_i][axis_j] = ALIVE
        else:
            self.temp_grid[axis_i][axis_j] = DEAD

    # This method count the total neighbors for a specific cell
    # @param axis_i == current row index
    # @param axis_j == current cell index
    # @param row ==  current row
    def count_neighbors(self, axis_i, axis_j, row):
        # Count top and bottom neighbors
        cell_neighbors = [self.top_neighbors(axis_i, axis_j), self.bottom_neighbors(axis_i, axis_j)]
        # Count right neighbor
        if (len(row) - 1) != axis_j and row[axis_j + 1] == ALIVE:
            cell_neighbors.append(1)
        # Count left neighbor
        if axis_j != DEAD and row[axis_j - 1] == ALIVE:
            cell_neighbors.append(1)
        return sum(cell_neighbors)

    # This method determine the axis_j for the neighbors
    # @param index == axis_j of the current cell
    def neighbor_axis_j(self, index):
        if index == 0:
            return [0, 2]
        elif index == len(self.grid[0]) - 1:
            return [index - 1, index + 1]
        else:
            return [index - 1, index + 2]

    # This method count top neighbors
    # @param axis_i == current row index
    # @param axis_j == current cell index
    def top_neighbors(self, axis_i, axis_j):
        neighbors = self.neighbor_axis_j(axis_j)
        if not axis_i == 0:
            return self.grid[axis_i - 1][neighbors[0]:neighbors[1]].count(ALIVE)
        else:
            return 0

    # This method count bottom neighbors
    # @param axis_i == current row index
    # @param axis_j == current cell index
    def bottom_neighbors(self, axis_i, axis_j):
        neighbors = self.neighbor_axis_j(axis_j)
        if (len(self.grid) - 1) != axis_i:
            return self.grid[axis_i + 1][neighbors[0]:neighbors[1]].count(ALIVE)
        else:
            return 0
