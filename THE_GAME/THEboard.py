import pygame
from consts import *
from matrix import *

class BOARD:

    board = Matrix(ROWS, COLS)

    def __init__(self):
        pass
    def printMatrix(self):
         self.board.print_matrix()

    def getMatrix(self):
        return self.board
    
    def draw_squares(self, WINDOW):
        WINDOW.fill(BEIGE)

        for row in range(ROWS):
            for col in range(COLS):
                if col > 0 and col < COLS-2 and row > 0 and row < ROWS-2:
                    if col in range(row % 2, ROWS, 2):
                        pygame.draw.rect(WINDOW, GRAY, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)) 
                else:
                    pygame.draw.rect(WINDOW, BLUE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)) 
                self.board.capture_stones(row,col)

    def place_piece(self, row, col,color):
        if self.board.set_value(row, col,color) == 0 and self.board.legal_move(row, col, color):
            return False
        else:
            return True
        
    def value(self,row,col):
        return self.board.get_value( row, col)
    
    def capture_stones(self,row,col):
        return self.board.capture_stones(row,col)
    
    def play(self):
        best_move = self.board.get_best_move()
        return best_move
        


    
