from collections import deque
import copy
from colorama import Back

from board import Board


class MagnetSolverBFS:
    def __init__(self, grid):
        self.grid = grid
        self.visited = set()
        self.path = []
        # self.magnet_positions = self.find_magnets()
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.board = Board(self.rows, self.cols)
        self.queue = deque()
    def bfs_solve(self):
        initial_state = (tuple(map(tuple, self.grid)),)
        self.stack.append((initial_state, copy.deepcopy(self.grid), []))  # Save the initial state, grid, and path in the stack

        while self.stack:
            current_state, current_grid, path = self.stack.pop()
            if self.is_visited(current_state):
                continue
            self.visited.add(current_state)
            self.path.append(current_state)
            self.grid = current_grid  # Restore the grid from the stack

            self.print_board(self.grid)

            if self.is_winner(self.grid):
                return True

            magnet_positions = self.find_magnets(self.grid, self.rows, self.cols)
            for magnet_x, magnet_y in magnet_positions:
                moves = self.available_positions()
                for move in moves:
                    n_board = copy.deepcopy(self.grid)
                    self.move_magnet(magnet_x, magnet_y, move[0], move[1], n_board)
                    new_state = (tuple(map(tuple, n_board)),)
                    if not self.is_visited(new_state):
                        self.stack.append((new_state, n_board, path + [(magnet_x, magnet_y, move[0], move[1])]))

            self.path.pop()

        return False

def is_visited(self, state):
    return state in self.visited

def move_magnet(self, magnet_x, magnet_y, pos_x, pos_y, grid):
    # Move red magnet to the positive position
    self.red_magnet_pos(grid, pos_x, pos_y)
    # Move purple magnet to the negative position
    self.purple_magnet_neg(grid, pos_x, pos_y)

    
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