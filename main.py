from algorithm import MagnetSolverDFS
from algorithm2 import MagnetSolverBFS
from board import Board, place_piece
from celles import EmptyCell, GreyIron, PurpleMagnet, RedMagnet, WhitePiece
from ucs_algorithm import ucs_solve

class Level:
    def __init__(self, row, col, placements):
        self.board = Board(row, col)
        self.setup(placements)

    def setup(self, placements):
        for x, y, piece in placements:
            place_piece(self.board.grid, x, y, piece)


level_data = [
    (3, 4, [(1, 2, GreyIron()), (2, 0, PurpleMagnet()), (1, 1, WhitePiece()), (1, 3, WhitePiece())]),  # Level 1
    (5, 5, [(1, 2, GreyIron()), (4, 0, PurpleMagnet()), (2, 1, GreyIron()), (2, 0, WhitePiece()), (2, 2, WhitePiece()),(2, 4, WhitePiece()),(4, 2, WhitePiece()),(0, 2, WhitePiece()),(3, 2, GreyIron()),(2, 3, GreyIron())]),  # Level 2
    (3, 4, [(1, 2, GreyIron()), (2, 0, PurpleMagnet()), (0, 3, WhitePiece()), (2, 3, WhitePiece()) , (0,0,EmptyCell()),(0,1,EmptyCell()),(0,2,EmptyCell())]),  # Level 3
    (5, 3, [(1, 1, GreyIron()),(3, 1, GreyIron()), (2, 0, PurpleMagnet()), (4, 1, WhitePiece()), (0, 0, WhitePiece()) , (0, 2, WhitePiece()),(1,0,EmptyCell()),(3,0,EmptyCell())]),  # Level 4
    (4, 3, [(1, 0, GreyIron(True)),(2, 0, GreyIron()),(1, 2, GreyIron(True)),(2, 2, GreyIron()), (3, 1, PurpleMagnet()), (3, 0, WhitePiece()), (0, 0, WhitePiece()) , (0, 2, WhitePiece()),(1,1,EmptyCell()),(0,1,EmptyCell()),(2,1,EmptyCell())]),  # Level 5****
    (3, 5, [(1, 1, GreyIron()),(1, 3, GreyIron()), (2, 0, PurpleMagnet()), (0, 3, WhitePiece()), (2, 3, WhitePiece()) , (1, 2, WhitePiece())]),  # Level 6
    (5, 4, [(1, 0, GreyIron(True)),(2, 0, GreyIron()),(3, 1, GreyIron()),(3, 2, GreyIron(True)), (2, 1, PurpleMagnet()), (4, 3, WhitePiece()), (0, 0, WhitePiece()) , (2, 3, WhitePiece()),(4,0,EmptyCell()),(4,1,EmptyCell()),(4,2,EmptyCell())]),  # Level 7***
    (3, 4, [(1, 1, GreyIron()),(1, 2, GreyIron()), (2, 0, PurpleMagnet()), (0, 0, WhitePiece()), (0, 2, WhitePiece()) , (2, 2, WhitePiece())]),  # Level 8
    (1, 7, [(0, 3, GreyIron(True)),(0, 5, GreyIron()), (0, 0, PurpleMagnet()), (0, 1, WhitePiece()), (0, 6, WhitePiece())]),  # Level 9 ******
    (4, 4, [(2, 2, GreyIron()),(2, 3, GreyIron()),(3, 1, GreyIron()), (0, 0, PurpleMagnet()), (1, 1, WhitePiece()), (1, 3, WhitePiece()),(3, 0, WhitePiece()),(3, 3, WhitePiece()) ]),  # Level 10
    (2, 5, [(0, 0, GreyIron()),(0, 4, GreyIron()), (1, 2, RedMagnet()), (0, 1, WhitePiece()), (0, 2, WhitePiece()),(0, 3, WhitePiece()),(1,0,EmptyCell()),(1,1,EmptyCell()),(1,3,EmptyCell()),(1,4,EmptyCell()) ]),  # Level 11
    (5, 4, [(0, 0, GreyIron()),(1, 0, GreyIron()),(4, 3, GreyIron()), (3, 1, RedMagnet()), (1, 0, WhitePiece()), (2, 0, WhitePiece()),(4, 0, WhitePiece()),(4, 2, WhitePiece()),(0,2,EmptyCell()),(0,3,EmptyCell()),(1,3,EmptyCell()),(1,2,EmptyCell()) ]),  # Level 12 ***
    (3, 6, [(0, 0, GreyIron()),(0, 4, GreyIron(True)),(0, 5, GreyIron()), (2, 3, RedMagnet()), (0, 3, WhitePiece()), (1, 1, WhitePiece()),(2, 1, WhitePiece()),(1,0,EmptyCell()),(2,0,EmptyCell()),(1,5,EmptyCell()),(1,4,EmptyCell()),(2,5,EmptyCell()),(2,4,EmptyCell()) ]),  # Level 13***

    (4, 4, [(0, 3, GreyIron()),(2, 0, GreyIron()),(3, 0, GreyIron()), (3, 3, RedMagnet()), (1, 0, WhitePiece()), (1, 2, WhitePiece()),(2, 2, WhitePiece()),(2, 1, WhitePiece())  ]),  # Level 14
    (3, 5, [(0, 1, GreyIron()),(0, 3, GreyIron()), (2, 2, RedMagnet()),(1,2,PurpleMagnet()), (0, 0, WhitePiece()), (0, 2, WhitePiece()),(1, 4, WhitePiece()) ,(2, 4, WhitePiece()) ]),  # Level 15
    (5, 5, [(1, 2, GreyIron()),(3, 2, GreyIron()), (2, 0, RedMagnet()), (2,4,PurpleMagnet()),(0, 3, WhitePiece()), (0, 4, WhitePiece()),(4, 0, WhitePiece()),(4, 3, WhitePiece()) ]),  # Level 16
    (4, 4, [(2, 0, GreyIron()),(0, 2, GreyIron()), (0, 0, RedMagnet()), (3,3,PurpleMagnet()), (1, 1, WhitePiece()), (2, 2, WhitePiece()),(1, 3, WhitePiece()),(3, 1, WhitePiece()) ]),  # Level 17
    (5, 6, [(2, 0, GreyIron()),(2, 5, GreyIron(True)),(0, 3, GreyIron()), (4, 2, RedMagnet()),(4,3,PurpleMagnet()), (2, 1, WhitePiece()), (2, 2, WhitePiece()),(2, 3, WhitePiece()),(1, 3, WhitePiece()),(0,0,EmptyCell()),(1,0,EmptyCell()),(0,1,EmptyCell()),(1,1,EmptyCell()) ,
    (0,4,EmptyCell()),(0,5,EmptyCell()),(1,5,EmptyCell()),(1,4,EmptyCell()),(4,0,EmptyCell()),(4,1,EmptyCell()),(4,5,EmptyCell()),(4,4,EmptyCell())  ]),  # Level 18***
    (5, 5, [(0, 1, GreyIron()),(0, 3, GreyIron()),(4, 1, GreyIron()),(4, 3, GreyIron()), (2, 2, RedMagnet()), (0,2,PurpleMagnet()), (1, 0, WhitePiece()), (3, 0, WhitePiece()),(2, 1, WhitePiece()),(3, 2, WhitePiece()),(1, 4, WhitePiece()),(3, 4, WhitePiece())
     ,(0,0,EmptyCell()),(2,0,EmptyCell()),(4,0,EmptyCell()),(0,4,EmptyCell()),(2,4,EmptyCell()),(4,4,EmptyCell()) ]),  # Level 19
    (5, 4, [(0, 1, GreyIron(True)),(0, 2, GreyIron()),(4, 0, GreyIron()), (4, 3, RedMagnet()), (4,2,PurpleMagnet()), (0, 3, WhitePiece()),(1, 0, WhitePiece()),(2, 0, WhitePiece()),(3, 0, WhitePiece()) ]),  # Level 20  ***
    (3, 4, [(1, 1, GreyIron(True)),(1, 2, GreyIron()),(0, 1, GreyIron()), (2, 3, RedMagnet()), (2,0,PurpleMagnet(True)), (1, 0, WhitePiece()),(0, 2, WhitePiece()),(2, 1, WhitePiece()) ]),  # Level 21
    (4, 5, [(3, 0, GreyIron()),(0, 4, GreyIron()),(0, 3, GreyIron(True)), (3, 2, RedMagnet()), (0,0,PurpleMagnet()), (0, 1, WhitePiece()), (1, 0, WhitePiece()),(1, 4, WhitePiece()),(2, 1, WhitePiece()),(3,4,EmptyCell()),(0,2,EmptyCell()),(1,2,EmptyCell())]),  # Level 22 ***
    (4, 5, [(3, 0, GreyIron()),(0, 3, GreyIron()),(1, 4, GreyIron()), (3, 2, RedMagnet(True)), (3,4,PurpleMagnet()), (0, 2, WhitePiece()), (2, 1, WhitePiece()),(2, 2, WhitePiece()),(2, 3, WhitePiece())]),  # Level 23***

    (5, 5, [(0, 1, GreyIron()),(1, 3, GreyIron()),(3, 4, GreyIron()), (3, 0, RedMagnet()), (1,4,PurpleMagnet()), (0, 3, WhitePiece()), (2, 3, WhitePiece()),(2, 1, WhitePiece()),(4, 2, WhitePiece()),(4, 1, WhitePiece()) ,(4,0,EmptyCell()),(4,4,EmptyCell())]),  # Level 24

    (5, 4, [(0, 0, GreyIron(True)),(1, 2, GreyIron()),(3, 2, GreyIron()), (4, 3, GreyIron()),(0, 3, RedMagnet(True)) ,(4,0,PurpleMagnet(True)),(2, 0, WhitePiece()),(4, 1, WhitePiece()),(4, 2, WhitePiece()) ]),  # Level 25***

]


def main():
    print("Choose a solving method:")
    print("1. User input")
    print("2. DFS (Depth-First Search)")
    print("3. BFS (Breadth-First Search)")
    method_choice = int(input("Enter your choice (1, 2, or 3): "))

    level_choice = int(input("Choose a level (1 to 25): "))

    if 1 <= level_choice <= 25:
        row, col, placements = level_data[level_choice - 1]
        level = Level(row, col, placements)
    else:
        print("Invalid choice. Defaulting to Level 1.")
        row, col, placements = level_data[0]
        level = Level(row, col, placements)

    board = level.board
    board.print_board()
    grid = level.board.grid

    if method_choice == 1:
        # User input method
        while True:
             board.magnet_selector()
            
    elif method_choice == 2:
        # DFS method
        solver = MagnetSolverDFS(grid)
        solver.dfs_solve()
    elif method_choice == 3:
        # BFS method
        solver = MagnetSolverBFS(grid)
        solver.bfs_solve()
    elif method_choice == 4:
        # UCS method
        solver = ucs_solve(grid)
        solver.uniform_cost_search()    
    else:
        print("Invalid choice. Please restart the program and choose a valid method.")

if __name__ == "__main__":
    main()

