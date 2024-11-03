
from colorama import  Back, Fore, init
from celles import Cell, PurpleMagnet, RedMagnet

init(autoreset=True)

def create_empty_board(row,col):
    return [[Cell('.') for _ in range(col)] for _ in range(row)]

def place_piece(board, row, col, piece):
    board[row][col] = piece

class Board:
    white_space_counter = 0
    white_filled_counter = 0
    def __init__(self, row,col):
        self.rows = row
        self.cols = col
        self.grid = create_empty_board(row ,col)

   
    def magnet_selector(self):
        attempts = 3 
        attempts_made = 0  

        while attempts_made < attempts:
            input_x = int(input("Enter x for R or P position: "))
            # if input_x == 99:
            #     return
            input_y = int(input("Enter y for R or P position: "))

            if not isinstance(self.grid[input_x][input_y], (RedMagnet, PurpleMagnet)):
                print("This cell isn't a magnet")
                self.print_board()
            else:
                print(f"Magnet at index [{input_x}] [{input_y}] was selected successfully!")
                new_input_x = int(input("Enter x for new magnet position: "))
                new_input_y = int(input("Enter y for new magnet position: "))

                if 0 <= new_input_x < self.rows and 0 <= new_input_y < self.cols:
                    if  self.grid[new_input_x][new_input_y].cell_type in [' ', 'R', 'P', 'G']:
                        print("Cannot place here!")
                        return
                    else:
                        
                        self.grid[new_input_x][new_input_y] = self.grid[input_x][input_y]
                        self.grid[input_x][input_y] = Cell(cell_type=".")

                        print(f"Magnet moved to new position [{new_input_x}] [{new_input_y}]")

                     
                        if isinstance(self.grid[new_input_x][new_input_y], RedMagnet):
                            self.move_red_magnet_pos(new_input_x, new_input_y)
                        else:
                            self.move_purple_magnet_neg(new_input_x, new_input_y)

                        self.print_board()
                        self.check_white( )
                        attempts_made += 1 
                else:
                    print("New position is out of bounds")

        if attempts_made >= attempts:
            print("No attempts left. Please restart the game.")
   
    

    
   
    def move_red_magnet_pos(self, magnet_pos_x, magnet_pos_y):
      # up => down
      for x in range(magnet_pos_x - 1,0,-1):
         if self.grid[x][magnet_pos_y].cell_type == '.':
            if self.grid[x-1][magnet_pos_y].cell_type == '.':
               pass
            elif self.grid[x-1][magnet_pos_y].cell_type in ['P','G']:
                temp = self.grid[x][magnet_pos_y].cell_type
                self.grid[x][magnet_pos_y].cell_type = self.grid[x-1][magnet_pos_y].cell_type
                self.grid[x-1][magnet_pos_y].cell_type = temp
         else:
            self.grid[x][magnet_pos_y].cell_type in ['P','G']
            pass
      #down => up   
      for x in range(magnet_pos_x + 1,self.rows - 1,1):
         if self.grid[x][magnet_pos_y].cell_type == '.':
            if self.grid[x+1][magnet_pos_y].cell_type == '.':
               pass
            elif self.grid[x+1][magnet_pos_y].cell_type in ['P','G']:
                temp = self.grid[x][magnet_pos_y].cell_type
                self.grid[x][magnet_pos_y].cell_type = self.grid[x+1][magnet_pos_y].cell_type
                self.grid[x+1][magnet_pos_y].cell_type = temp
         else:
            self.grid[x][magnet_pos_y].cell_type in ['P','G']
            pass  
      #left => right    
      for y in range(magnet_pos_y - 1,0,-1):
         if self.grid[magnet_pos_x][y].cell_type == '.':
            if self.grid[magnet_pos_x][y-1].cell_type == '.':
               pass
            elif self.grid[magnet_pos_x][y-1].cell_type in['P','G']:
                temp = self.grid[magnet_pos_x][y].cell_type
                self.grid[magnet_pos_x][y].cell_type = self.grid[magnet_pos_x][y-1].cell_type
                self.grid[magnet_pos_x][y-1].cell_type = temp
         else:
            self.grid[magnet_pos_x][y].cell_type in['P','G']
            pass 
      #right => left    
      for y in range(magnet_pos_y + 1,self.cols - 1,1):
         if self.grid[magnet_pos_x][y].cell_type == '.':
            if self.grid[magnet_pos_x][y+1].cell_type == '.':
               pass
            elif self.grid[magnet_pos_x][y+1].cell_type in['P','G']:
                temp = self.grid[magnet_pos_x][y].cell_type
                self.grid[magnet_pos_x][y].cell_type = self.grid[magnet_pos_x][y+1].cell_type
                self.grid[magnet_pos_x][y+1].cell_type = temp
         else:
            self.grid[magnet_pos_x][y].cell_type in['P','G']
            pass    
    def move_purple_magnet_neg(self, magnet_neg_x,magnet_neg_y):
      #up
      for x in range(magnet_neg_x - 1,-1,-1):
         if self.grid[x][magnet_neg_y].cell_type == '.':
            pass
         elif self.grid[x][magnet_neg_y].cell_type in ['R','G']:
           if self.grid[x-1][magnet_neg_y].cell_type == '.':
              self.grid[x-1][magnet_neg_y].cell_type = self.grid[x][magnet_neg_y].cell_type
              self.grid[x][magnet_neg_y].cell_type = '.'
              break
           elif self.grid[x-1][magnet_neg_y].cell_type in ['R','G']:
                temp = self.grid[x-1][magnet_neg_y].cell_type
                self.grid[x-2][magnet_neg_y].cell_type = self.grid[x-1][magnet_neg_y].cell_type
                self.grid[x-1][magnet_neg_y].cell_type = '.'
                self.grid[x-2][magnet_neg_y].cell_type = temp
                self.grid[x-1][magnet_neg_y].cell_type = self.grid[x][magnet_neg_y].cell_type
                self.grid[x][magnet_neg_y].cell_type = '.'
                break
      #down 
      for x in range(magnet_neg_x + 1,self.rows - 1,1):
         if self.grid[x][magnet_neg_y].cell_type == '.':
            pass
         elif self.grid[x][magnet_neg_y].cell_type in ['R','G']:
           if self.grid[x+1][magnet_neg_y].cell_type == '.':
              self.grid[x+1][magnet_neg_y].cell_type = self.grid[x][magnet_neg_y].cell_type
              self.grid[x][magnet_neg_y].cell_type = '.'
              break
           elif self.grid[x+1][magnet_neg_y].cell_type in ['R','G']:
                temp = self.grid[x+1][magnet_neg_y].cell_type
                self.grid[x+2][magnet_neg_y].cell_type = self.grid[x+1][magnet_neg_y].cell_type
                self.grid[x+1][magnet_neg_y].cell_type = '.'
                self.grid[x+2][magnet_neg_y].cell_type = temp
                self.grid[x+1][magnet_neg_y].cell_type = self.grid[x][magnet_neg_y].cell_type
                self.grid[x][magnet_neg_y].cell_type = '.'
                break   
           
      #left
      for y in range(magnet_neg_y - 1, 0,-1):
         if self.grid[magnet_neg_x][y].cell_type == '.':
            pass
         elif self.grid[magnet_neg_x][y].cell_type in ['R','G']:
           if self.grid[magnet_neg_x][y-1].cell_type == '.':
              self.grid[magnet_neg_x][y-1].cell_type = self.grid[magnet_neg_x][y].cell_type
              self.grid[magnet_neg_x][y].cell_type = '.'
              break
           elif self.grid[magnet_neg_x][y-1].cell_type in ['R','G']:
                temp = self.grid[magnet_neg_x][y-1].cell_type
                self.grid[magnet_neg_x][y-2].cell_type = self.grid[magnet_neg_x][y-1].cell_type
                self.grid[magnet_neg_x][y-1].cell_type = '.'
                self.grid[magnet_neg_x][y-2].cell_type = temp
                self.grid[magnet_neg_x][y-1].cell_type = self.grid[magnet_neg_x][y].cell_type
                self.grid[magnet_neg_x][y].cell_type = '.'
                break
      #right 
      for y in range(magnet_neg_y + 1,self.cols - 1,1):
         if self.grid[magnet_neg_x][y].cell_type == '.':
            pass
         elif self.grid[magnet_neg_x][y].cell_type in ['R','G']:
           if self.grid[magnet_neg_x][y+1].cell_type == '.':
              self.grid[magnet_neg_x][y+1].cell_type = self.grid[magnet_neg_x][y].cell_type
              self.grid[magnet_neg_x][y].cell_type = '.'
              break
           elif self.grid[magnet_neg_x][y+1].cell_type in ['R','G']:
                temp = self.grid[magnet_neg_x][y+1].cell_type
                self.grid[magnet_neg_x][y+2].cell_type = self.grid[magnet_neg_x][y+1].cell_type
                self.grid[magnet_neg_x][y+1].cell_type = '.'
                self.grid[magnet_neg_x][y+2].cell_type = temp
                self.grid[magnet_neg_x][y+1].cell_type = self.grid[magnet_neg_x][y].cell_type
                self.grid[magnet_neg_x][y].cell_type = '.'
                break
            
    def check_white(self): 
         for row in range(self.rows):
            for col in range(self.cols):
              if self.grid[row][col].headwhite == True:
               self.white_space_counter = self.white_space_counter + 1
               if self.grid[row][col].cell_type in ['G','P','R']: 
                  self.grid[row][col].whiteFilled = True
                  self.white_filled_counter = self.white_filled_counter + 1
              else:
                  self.grid[row][col].whiteFilled = False
                 
            else:
              pass
         self.check_won(self.white_space_counter,self.white_filled_counter)

    def check_won(self,white_space_counter,white_filled_counter):
          if white_space_counter == white_filled_counter:
            print("You Won")
            from main import main
            main()
            return 
          else:
             print(f"white cells = {white_space_counter}")
             print(f"white filled = {white_filled_counter}")
             self.white_space_counter = 0
             self.white_filled_counter = 0
        
       
        


    def print_board(self):
        for row in self.grid:
           
              print('   '.join([ 
                 (Back.WHITE + cell.cell_type + Back.RESET) if cell.headwhite 
            else str(cell)  for cell in row ]))
      