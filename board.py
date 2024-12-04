import pygame
import cell
import math
import sudoku_generator
import difficulty as diff
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cell_board = []
        if difficulty == diff.Difficulty.easy:
            self.filled_values = sudoku_generator.generate_sudoku(9, 30)
        elif difficulty == diff.Difficulty.medium:
            self.filled_values = sudoku_generator.generate_sudoku(9, 40)
        else:
            self.filled_values = sudoku_generator.generate_sudoku(9, 50)

        for i in range(9):
            appending_cell_row = []
            for j in range(9):
                appending_cell_row.append(cell.Cell(i, j, self.screen, self.filled_values[i][j]))
                appending_cell_row[j].draw()
                self.cell_board.append(appending_cell_row)

    def draw(self):
        for i in range(3):
            pygame.draw.line(self.screen, "black", (i * 192, 0), (i * 192, 576), 5)
            pygame.draw.line(self.screen, "black", (0, i * 192), (576, i * 192), 5)
    def select(self, row, col):
        pass
    def click(self, x, y):
        if 1152 >= (x + y) >= 0:
            return math.floor(x / 64), math.floor(y / 64)
    def clear(self):
        pass
    def sketch(self, value):
        pass
    def place_number(self, value):
        pass
    def reset_to_original(self):
        pass
    def is_full(self):
        for rows in self.cell_board:
            for cells in rows:
                if cells.value == 0:
                    return False
        return True
    def update_board(self):
        pass
    def find_empty(self):
        pass
    def check_board(self):
        pass

