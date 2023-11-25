from consts import *
from THEboard import BOARD
from matrix import *
class Piece:
    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color
        self.x = 0
        self.y = 0
        
        if column != 0 and column != COLS-1 and row != 0 and row != ROWS-1:
            self.calc_pos()
        else:
            print("invalid position")


    def calc_pos(self):
                self.y = SQUARE_SIZE * self.row  
                self.x = SQUARE_SIZE * self.column 

    def draw(self, board, WINDOW):
        radius = SQUARE_SIZE//2 - 8
        if(self.color==BLACK) and board.value(self.row, self.column) != 5:
            if(board.value(self.row,self.column) == 1 or board.place_piece( self.row, self.column, self.color) ):
                pygame.draw.circle(WINDOW, self.color, (self.x, self.y), radius)
                return True
            else:
                return False
        elif(self.color==WHITE) and board.value(self.row, self.column) != 6:
            if(board.value(self.row,self.column) == 2 or board.place_piece( self.row, self.column, self.color) ):
                pygame.draw.circle(WINDOW, self.color, (self.x, self.y), radius)
                return True
            else:
                return False

