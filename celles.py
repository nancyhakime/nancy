from colorama import Back, Fore, init

init(autoreset=True)

class Cell:
    def __init__(self, cell_type, headwhite=False,whiteFilled=False):
        self.cell_type = cell_type
        self.headwhite = headwhite
        self.whiteFilled = whiteFilled

    def __str__(self):
        return self.cell_type if self.cell_type != '.' else '.'


class GreyIron(Cell):
    def __init__(self, headwhite = False):
        super().__init__(cell_type='G', headwhite=headwhite)

    def __str__(self):
        return Fore.BLACK + self.cell_type + Fore.RESET

class PurpleMagnet(Cell):
    def __init__(self, headwhite = False):
        super().__init__(cell_type='P', headwhite=headwhite)

    def __str__(self):
        return Fore.MAGENTA + self.cell_type + Fore.RESET

class RedMagnet(Cell):
    def __init__(self, headwhite = False):
        super().__init__(cell_type='R', headwhite=headwhite)

    def __str__(self):
        return Fore.RED + self.cell_type + Fore.RESET

class EmptyCell(Cell):
    def __init__(self):
        super().__init__(' ')

class WhitePiece(Cell):
    def __init__(self,headwhite = True,whiteFilled = False):
         super().__init__(cell_type='.', headwhite=headwhite,whiteFilled=whiteFilled)
      
       

    def __str__(self):
        return Back.WHITE + self.cell_type + Back.RESET
