from tkinter import Grid
from colorama import Back
from celles import PurpleMagnet, RedMagnet
from board import Board
import copy

class MagnetSolverDFS:
    def __init__(self, grid):
        self.grid = grid
        self.visited = set()
        self.path = []
        # self.magnet_positions = self.find_magnets()
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.board = Board(self.rows, self.cols)
        self.stack = []

    def find_magnets(self, grid, rows, cols):
        magnets = []
        for i in range(rows):
            for j in range(cols):
                if isinstance(grid[i][j], (RedMagnet, PurpleMagnet)):
                    magnets.append((i, j))
        return magnets


    def is_winner(self, grid):
        for row in grid:
            for cell in row:
                if cell.cell_type == cell.headwhite:  
                    return False
                if cell.cell_type not in {'I', 'N', 'R'}:
                    return False
        return True

    def available_positions(self):
        positions = []
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell.cell_type == '.':
                    positions.append((i, j))
        return positions

    def is_visited(self, state):
        return state in self.visited

    def dfs_solve(self):
        initial_state = (tuple(map(tuple, self.grid)),)
        self.stack.append((initial_state, copy.deepcopy(self.grid)))  # Save the initial state and grid in the stack

        while self.stack:
            current_state, current_grid = self.stack.pop()
            if self.is_visited(current_state):
                continue
            self.visited.add(current_state)
            self.path.append(current_state)
            self.grid = current_grid  # Restore the grid from the stack

            self.print_board(self.grid)

            if self.is_winner(self.grid):
                return True

            magnets = self.find_magnets(self.grid, self.rows, self.cols)

            for pos in self.available_positions():
                x, y = pos

                # Move red magnet to the positive position
                self.red_magnet_pos(self.grid, x, y)
                new_state = (tuple(map(tuple, self.grid)),)
                if not self.is_visited(new_state):
                    self.stack.append((new_state, copy.deepcopy(self.grid)))  # Save the new state and grid in the stack

                # Move purple magnet to the negative position
                self.purple_magnet_neg(self.grid, x, y)
                new_state = (tuple(map(tuple, self.grid)),)
                if not self.is_visited(new_state):
                    self.stack.append((new_state, copy.deepcopy(self.grid)))  # Save the new state and grid in the stack

            self.path.pop()

        return False


    def red_magnet_pos(self, grid, magnet_pos_x, magnet_pos_y):
    # up => down
        for x in range(magnet_pos_x - 1, 0, -1):
            if grid[x][magnet_pos_y].cell_type == '.':
                if x - 1 >= 0 and grid[x - 1][magnet_pos_y].cell_type in ['P', 'G']:
                    temp = grid[x][magnet_pos_y].cell_type
                    grid[x][magnet_pos_y].cell_type = grid[x - 1][magnet_pos_y].cell_type
                    grid[x - 1][magnet_pos_y].cell_type = temp
            else:
                break

        # down => up
        for x in range(magnet_pos_x + 1, self.rows):
            if grid[x][magnet_pos_y].cell_type == '.':
                if x + 1 < self.rows and grid[x + 1][magnet_pos_y].cell_type in ['P', 'G']:
                    temp = grid[x][magnet_pos_y].cell_type
                    grid[x][magnet_pos_y].cell_type = grid[x + 1][magnet_pos_y].cell_type
                    grid[x + 1][magnet_pos_y].cell_type = temp
            else:
                break

        # left => right
        for y in range(magnet_pos_y - 1, 0, -1):
            if grid[magnet_pos_x][y].cell_type == '.':
                if y - 1 >= 0 and grid[magnet_pos_x][y - 1].cell_type in ['P', 'G']:
                    temp = grid[magnet_pos_x][y].cell_type
                    grid[magnet_pos_x][y].cell_type = grid[magnet_pos_x][y - 1].cell_type
                    grid[magnet_pos_x][y - 1].cell_type = temp
            else:
                break

        # right => left
        for y in range(magnet_pos_y + 1, self.cols):
            if grid[magnet_pos_x][y].cell_type == '.':
                if y + 1 < self.cols and grid[magnet_pos_x][y + 1].cell_type in ['P', 'G']:
                    temp = grid[magnet_pos_x][y].cell_type
                    grid[magnet_pos_x][y].cell_type = grid[magnet_pos_x][y + 1].cell_type
                    grid[magnet_pos_x][y + 1].cell_type = temp
            else:
                break

    def purple_magnet_neg(self, grid, magnet_neg_x, magnet_neg_y):
        # up
        for x in range(magnet_neg_x - 1, -1, -1):
            if grid[x][magnet_neg_y].cell_type == '.':
                pass
            elif grid[x][magnet_neg_y].cell_type in ['R', 'G']:
                if x - 1 >= 0 and grid[x - 1][magnet_neg_y].cell_type == '.':
                    grid[x - 1][magnet_neg_y].cell_type = grid[x][magnet_neg_y].cell_type
                    grid[x][magnet_neg_y].cell_type = '.'
                    break
                elif x - 2 >= 0 and grid[x - 1][magnet_neg_y].cell_type in ['R', 'G']:
                    temp = grid[x - 1][magnet_neg_y].cell_type
                    grid[x - 2][magnet_neg_y].cell_type = grid[x - 1][magnet_neg_y].cell_type
                    grid[x - 1][magnet_neg_y].cell_type = '.'
                    grid[x - 2][magnet_neg_y].cell_type = temp
                    grid[x - 1][magnet_neg_y].cell_type = grid[x][magnet_neg_y].cell_type
                    grid[x][magnet_neg_y].cell_type = '.'
                    break

        # down
        for x in range(magnet_neg_x + 1, self.rows):
            if grid[x][magnet_neg_y].cell_type == '.':
                pass
            elif grid[x][magnet_neg_y].cell_type in ['R', 'G']:
                if x + 1 < self.rows and grid[x + 1][magnet_neg_y].cell_type == '.':
                    grid[x + 1][magnet_neg_y].cell_type = grid[x][magnet_neg_y].cell_type
                    grid[x][magnet_neg_y].cell_type = '.'
                    break
                elif x + 2 < self.rows and grid[x + 1][magnet_neg_y].cell_type in ['R', 'G']:
                    temp = grid[x + 1][magnet_neg_y].cell_type
                    grid[x + 2][magnet_neg_y].cell_type = grid[x + 1][magnet_neg_y].cell_type
                    grid[x + 1][magnet_neg_y].cell_type = '.'
                    grid[x + 2][magnet_neg_y].cell_type = temp
                    grid[x + 1][magnet_neg_y].cell_type = grid[x][magnet_neg_y].cell_type
                    grid[x][magnet_neg_y].cell_type = '.'
                    break

        # left
        for y in range(magnet_neg_y - 1, -1, -1):
            if grid[magnet_neg_x][y].cell_type == '.':
                pass
            elif grid[magnet_neg_x][y].cell_type in ['R', 'G']:
                if y - 1 >= 0 and grid[magnet_neg_x][y - 1].cell_type == '.':
                    grid[magnet_neg_x][y - 1].cell_type = grid[magnet_neg_x][y].cell_type
                    grid[magnet_neg_x][y].cell_type = '.'
                    break
                elif y - 2 >= 0 and grid[magnet_neg_x][y - 1].cell_type in ['R', 'G']:
                    temp = grid[magnet_neg_x][y - 1].cell_type
                    grid[magnet_neg_x][y - 2].cell_type = grid[magnet_neg_x][y - 1].cell_type
                    grid[magnet_neg_x][y - 1].cell_type = '.'
                    grid[magnet_neg_x][y - 2].cell_type = temp
                    grid[magnet_neg_x][y - 1].cell_type = grid[magnet_neg_x][y].cell_type
                    grid[magnet_neg_x][y].cell_type = '.'
                    break

        # right
        for y in range(magnet_neg_y + 1, self.cols):
            if grid[magnet_neg_x][y].cell_type == '.':
                pass
            elif grid[magnet_neg_x][y].cell_type in ['R', 'G']:
                if y + 1 < self.cols and grid[magnet_neg_x][y + 1].cell_type == '.':
                    grid[magnet_neg_x][y + 1].cell_type = grid[magnet_neg_x][y].cell_type
                    grid[magnet_neg_x][y].cell_type = '.'
                    break
                elif y + 2 < self.cols and grid[magnet_neg_x][y + 1].cell_type in ['R', 'G']:
                    temp = grid[magnet_neg_x][y + 1].cell_type
                    grid[magnet_neg_x][y + 2].cell_type = grid[magnet_neg_x][y + 1].cell_type
                    grid[magnet_neg_x][y + 1].cell_type = '.'
                    grid[magnet_neg_x][y + 2].cell_type = temp
                    grid[magnet_neg_x][y + 1].cell_type = grid[magnet_neg_x][y].cell_type
                    grid[magnet_neg_x][y].cell_type = '.'
                    break


    def print_board(self, grid):
        print("-------------------------------")
        for row in grid:
            formatted_row = []
            for cell in row:
                formatted_row.append(
                    (Back.WHITE + cell.cell_type + Back.RESET) if cell.cell_type == cell.headwhite else str(cell)
                )
            print('   '.join(formatted_row))
        print("-------------------------------")
