import pygame
from consts import *
from THEboard import BOARD
from piece import Piece

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Go ban')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    column = x // SQUARE_SIZE
    return row, column


def main():
    run = True
    board = BOARD()
    pieces = []
    current_player = WHITE
    
    while run:
        board.draw_squares(WINDOW)
        board.printMatrix()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                r, c = get_row_col_from_mouse(pos)
                if board.value(r, c) == 1 or board.value(r, c) == 2:
                    continue
                if c != 0 and c != COLS - 1 and r != 0 and r != ROWS - 1:
                    # white player
                    if current_player == WHITE:
                        move = board.play()
                        new_white_piece = Piece(move[0], move[1], WHITE)
                        pieces.append(new_white_piece)
                        current_player = BLACK

                    # black plays
                    elif current_player == BLACK:
                        new_black_piece = Piece(r,c, BLACK)
                        pieces.append(new_black_piece)
                        current_player = WHITE
                        
                for row in range(ROWS):
                    captured = []
                    for col in range(COLS):
                        if col > 0 and col < COLS-2 and row > 0 and row < ROWS-2:
                            captured = board.capture_stones(col,row)      

        for piece in pieces:
            piece.draw(board, WINDOW)
        pygame.display.update()

    pygame.quit()

main()
