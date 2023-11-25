from consts import *
import copy

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [
            [7, 7, 7, 7, 7, 7, 7, 7],
            [7, 0, 0, 0, 0, 0, 0, 7],
            [7, 0, 0, 0, 0, 0, 0, 7],
            [7, 0, 0, 0, 0, 0, 0, 7],
            [7, 0, 0, 0, 0, 0, 0, 7],
            [7, 0, 0, 0, 0, 0, 0, 7],
            [7, 0, 0, 0, 0, 0, 0, 7],
            [7, 7, 7, 7, 7, 7, 7, 7]
        ]

    def set_value(self, row, col, value):
        if self.matrix[row][col] == 0 and self.legal_move(row, col, value) == True:
            if value == BLACK:
                self.matrix[row][col] = 1
            else:
                self.matrix[row][col] = 2
            return True
        else:
            return False

    def get_value(self, row, col):
        return self.matrix[row][col]

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def get_matrix(self):
        return self.matrix
    
    def capture_stones(self, r, c):
        count = 0
        color = self.matrix[r][c]
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if self.matrix[nr][nc] == color or self.matrix[nr][nc] == 0 :
                return
            else:
                count=count+1
        
        if self.matrix[r][c] == 1 and count==4:
            self.matrix[r][c] = 3
        elif(count==4):
            self.matrix[r][c] = 4

    def make_move(self, move, player):
        new_board = copy.deepcopy(self.matrix)
        new_board[move[0]][move[1]] = player
        return new_board

    def get_valid_moves(self):
        valid_moves = []
        for i in range(1, self.rows-1):
            for j in range(1, self.cols-1):
                if self.matrix[i][j] == 0:
                    valid_moves.append((i, j))
        return valid_moves

    def evaluate(self):
        black_score = 0
        white_score = 0
        for row in self.matrix:
            for stone in row:
                if stone == 1 or stone == 3:
                    black_score += 1
                elif stone == 2 or stone == 4:
                    white_score += 1
        return white_score - black_score
    
    def minimax(self, new_board, depth, maximizing_player):
        if depth == 0:
            return self.evaluate()

        valid_moves = self.get_valid_moves()

        if maximizing_player:
            max_eval = float('-inf')
            for move in valid_moves:
                new_board = self.make_move(move, 2)
                eval = self.minimax(new_board, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in valid_moves:
                new_board = self.make_move(move, 1)
                eval = self.minimax(new_board, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval

    def get_best_move(self):
        valid_moves = self.get_valid_moves()
        best_score = float('-inf')
        best_move = None
        print(best_move)

        for move in valid_moves:
            new_board = self.make_move(move, 2)
            score = self.minimax(new_board, 3, False)
            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def check(self, row, col, color):
        place = self.matrix[row][col]
        if place == 0: 
            return True
        elif place == 7:
            return False
        if color == BLACK and place != 1:
            return False
        elif color == WHITE and place != 2:
            return False

        return True

    def mark(self, row, col, color):
        if color == BLACK:
            self.matrix[row][col] = 5
        elif color == WHITE:
            self.matrix[row][col] = 6

    def legal_move(self, row, col, color):
        pos = self.matrix[row][col]

        if pos == 7:
            return False

        if pos == 0:
            # Checking the east, west, north, and south positions
            if (
                self.check(row + 1, col, color)
                or self.check(row - 1, col, color)
                or self.check(row, col + 1, color)
                or self.check(row, col - 1, color)
            ):
                return True
            else:
                self.mark(row, col, color)
                return False
        return False

