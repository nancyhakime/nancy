import heapq

from colorama import Back

from board import Board
from celles import PurpleMagnet, RedMagnet

class ucs_solve:
    def __init__(self, grid):
        self.grid = grid
        self.visited = set()
        self.path = []
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.board = Board(self.rows, self.cols)
        self.priority_queue = []

    def available_neighbors(self):
        positions = []
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell.cell_type == '.':
                    positions.append((i, j))
        return positions

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

    

    def uniform_cost_search(self, start):
        priority_queue = [(0, start)]
        visited = {}
        visited[start] = (0, None)
        total_cost_magnet = 0  

        while priority_queue:
            current_cost, current_node = heapq.heappop(priority_queue)
            total_cost_magnet += current_cost 

            if self.is_winner(current_node):
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = visited[current_node][1]
                print(f"Total cost of magnet movements: {total_cost_magnet}")  
                return path[::-1]

            for neighbor, cost in self.grid[current_node]:
                total_cost = current_cost + cost
                if neighbor not in visited or total_cost < visited[neighbor][0]:
                    visited[neighbor] = (total_cost, current_node)
                    heapq.heappush(priority_queue, (total_cost, neighbor))

        print(f"Total cost of magnet movements: {total_cost_magnet}")  
        return None
    

    
   


    def add_cost(self, grid, cost):
        for row in grid:
            for cell in row:
                if hasattr(cell, 'movement_cost'):
                    cell.movement_cost += cost
                else:
                    cell.movement_cost = cost

    
    def red_magnet_pos(self, grid, magnet_pos_x, magnet_pos_y):
        cost_per_move = 1
        total_cost = 0

        # up => down
        for x in range(magnet_pos_x - 1, -1, -1):
            if grid[x][magnet_pos_y].cell_type == '.':
                if x - 1 >= 0 and grid[x - 1][magnet_pos_y].cell_type in ['P', 'G']:
                    temp = grid[x][magnet_pos_y].cell_type
                    grid[x][magnet_pos_y].cell_type = grid[x - 1][magnet_pos_y].cell_type
                    grid[x - 1][magnet_pos_y].cell_type = temp
                    total_cost += cost_per_move
            else:
                break

        # down => up
        for x in range(magnet_pos_x + 1, self.rows):
            if grid[x][magnet_pos_y].cell_type == '.':
                if x + 1 < self.rows and grid[x + 1][magnet_pos_y].cell_type in ['P', 'G']:
                    temp = grid[x][magnet_pos_y].cell_type
                    grid[x][magnet_pos_y].cell_type = grid[x + 1][magnet_pos_y].cell_type
                    grid[x + 1][magnet_pos_y].cell_type = temp
                    total_cost += cost_per_move
            else:
                break

        # left => right
        for y in range(magnet_pos_y - 1, -1, -1):
            if grid[magnet_pos_x][y].cell_type == '.':
                if y - 1 >= 0 and grid[magnet_pos_x][y - 1].cell_type in ['P', 'G']:
                    temp = grid[magnet_pos_x][y].cell_type
                    grid[magnet_pos_x][y].cell_type = grid[magnet_pos_x][y - 1].cell_type
                    grid[magnet_pos_x][y - 1].cell_type = temp
                    total_cost += cost_per_move
            else:
                break

        # right => left
        for y in range(magnet_pos_y + 1, self.cols):
            if grid[magnet_pos_x][y].cell_type == '.':
                if y + 1 < self.cols and grid[magnet_pos_x][y + 1].cell_type in ['P', 'G']:
                    temp = grid[magnet_pos_x][y].cell_type
                    grid[magnet_pos_x][y].cell_type = grid[magnet_pos_x][y + 1].cell_type
                    grid[magnet_pos_x][y + 1].cell_type = temp
                    total_cost += cost_per_move
            else:
                break

        self.add_cost(grid, total_cost)

   
    def purple_magnet_neg(self, grid, magnet_neg_x, magnet_neg_y):
        cost_per_move = 1
        total_cost = 0

        # up
        for x in range(magnet_neg_x - 1, -1, -1):
            if grid[x][magnet_neg_y].cell_type == '.':
                pass
            elif grid[x][magnet_neg_y].cell_type in ['R', 'G']:
                if x - 1 >= 0 and grid[x - 1][magnet_neg_y].cell_type == '.':
                    grid[x - 1][magnet_neg_y].cell_type = grid[x][magnet_neg_y].cell_type
                    grid[x][magnet_neg_y].cell_type = '.'
                    total_cost += cost_per_move
                    break
                elif x - 2 >= 0 and grid[x - 1][magnet_neg_y].cell_type in ['R', 'G']:
                    temp = grid[x - 1][magnet_neg_y].cell_type
                    grid[x - 2][magnet_neg_y].cell_type = grid[x - 1][magnet_neg_y].cell_type
                    grid[x - 1][magnet_neg_y].cell_type = '.'
                    grid[x - 2][magnet_neg_y].cell_type = temp
                    grid[x - 1][magnet_neg_y].cell_type = grid[x][magnet_neg_y].cell_type
                    grid[x][magnet_neg_y].cell_type = '.'
                    total_cost += cost_per_move
                    break

        # down
        for x in range(magnet_neg_x + 1, self.rows):
            if grid[x][magnet_neg_y].cell_type == '.':
                pass
            elif grid[x][magnet_neg_y].cell_type in ['R', 'G']:
                if x + 1 < self.rows and grid[x + 1][magnet_neg_y].cell_type == '.':
                    grid[x + 1][magnet_neg_y].cell_type = grid[x][magnet_neg_y].cell_type
                    grid[x][magnet_neg_y].cell_type = '.'
                    total_cost += cost_per_move
                    break
                elif x + 2 < self.rows and grid[x + 1][magnet_neg_y].cell_type in ['R', 'G']:
                    temp = grid[x + 1][magnet_neg_y].cell_type
                    grid[x + 2][magnet_neg_y].cell_type = grid[x + 1][magnet_neg_y].cell_type
                    grid[x + 1][magnet_neg_y].cell_type = '.'
                    grid[x + 2][magnet_neg_y].cell_type = temp
                    grid[x + 1][magnet_neg_y].cell_type = grid[x][magnet_neg_y].cell_type
                    grid[x][magnet_neg_y].cell_type = '.'
                    total_cost += cost_per_move
                    break

        # left
        for y in range(magnet_neg_y - 1, -1, -1):
            if grid[magnet_neg_x][y].cell_type == '.':
                pass
            elif grid[magnet_neg_x][y].cell_type in ['R', 'G']:
                if y - 1 >= 0 and grid[magnet_neg_x][y - 1].cell_type == '.':
                    grid[magnet_neg_x][y - 1].cell_type = grid[magnet_neg_x][y].cell_type
                    grid[magnet_neg_x][y].cell_type = '.'
                    total_cost += cost_per_move
                    break
                elif y - 2 >= 0 and grid[magnet_neg_x][y - 1].cell_type in ['R', 'G']:
                    temp = grid[magnet_neg_x][y - 1].cell_type
                    grid[magnet_neg_x][y - 2].cell_type = grid[magnet_neg_x][y - 1].cell_type
                    grid[magnet_neg_x][y - 1].cell_type = '.'
                    grid[magnet_neg_x][y - 2].cell_type = temp
                    grid[magnet_neg_x][y - 1].cell_type = grid[magnet_neg_x][y].cell_type
                    grid[magnet_neg_x][y].cell_type = '.'
                    total_cost += cost_per_move
                    break

        # right
        for y in range(magnet_neg_y + 1, self.cols):
            if grid[magnet_neg_x][y].cell_type == '.':
                pass
            elif grid[magnet_neg_x][y].cell_type in ['R', 'G']:
                if y + 1 < self.cols and grid[magnet_neg_x][y + 1].cell_type == '.':
                    grid[magnet_neg_x][y + 1].cell_type = grid[magnet_neg_x][y].cell_type
                    grid[magnet_neg_x][y].cell_type = '.'
                    total_cost += cost_per_move
                    break
                elif y + 2 < self.cols and grid[magnet_neg_x][y + 1].cell_type in ['R', 'G']:
                    temp = grid[magnet_neg_x][y + 1].cell_type
                    grid[magnet_neg_x][y + 2].cell_type = grid[magnet_neg_x][y + 1].cell_type
                    grid[magnet_neg_x][y + 1].cell_type = '.'
                    grid[magnet_neg_x][y + 2].cell_type = temp
                    grid[magnet_neg_x][y + 1].cell_type = grid[magnet_neg_x][y].cell_type
                    grid[magnet_neg_x][y].cell_type = '.'
                    total_cost += cost_per_move
                    break

        self.add_cost(grid, total_cost)

    
    def print_board(self, grid):
        print("-------------------------------")
        for row in grid:
            formatted_row = []
            for cell in row:
                formatted_row.append(
                    (Back.WHITE + cell.cell_type + Back.RESET) if cell.cell_type == cell.headwhite else str(cell)
                )