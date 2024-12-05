import pygame
import config
import sudoku_generator

from cell import Cell
from difficulty import Difficulty
from copy import deepcopy


class Board:
    def __init__(self, width: int, height: int, screen: pygame.Surface, difficulty: Difficulty) -> None:
        self.width: int = width
        self.height: int = height
        self.screen: pygame.Surface = screen

        self.cell_board: list[list[Cell]] = []
        self.filled_values: list[list[int]] = sudoku_generator.generate_sudoku(9, difficulty.value)
        self.userValues: list[list[int]] = deepcopy(self.filled_values)
        self.reset_to_original()

        self.selectedCell: Cell = None

    def draw(self) -> None:
        for i in range(3):
            pygame.draw.line(self.screen, config.TEXT_COLOR, (i * 192, 0), (i * 192, 576), 5)
            pygame.draw.line(self.screen, config.TEXT_COLOR, (0, i * 192), (576, i * 192), 5)

        for row in self.cell_board:
            for cell in row:
                cell.draw()

    def select(self, row: int, col: int) -> None:
        if self.selectedCell is not None:
            self.selectedCell.selected = False

        self.selectedCell = self.cell_board[row][col]
        self.selectedCell.selected = True

    @staticmethod
    def click(x: int, y: int) -> tuple[int, int]:
        if x < config.WINDOW_WIDTH and y < config.WINDOW_WIDTH:
            return x // 64, y // 64
        return None

    def clear(self) -> None:
        self.selectedCell.sketched_value = 0
        self.selectedCell.value = 0
        self.selectedCell._text = None

    def sketch(self, value: int) -> None:
        self.selectedCell.set_sketched_value(value)

    def place_number(self) -> None:
        self.selectedCell.set_cell_value()

    def reset_to_original(self) -> None:
        self.cell_board = []
        for i in range(9):
            appending_cell_row: list[Cell] = []
            for j in range(9):
                appending_cell_row.append(Cell(i, j, self.screen, self.filled_values[i][j]))
            self.cell_board.append(appending_cell_row)

    def is_full(self) -> bool:
        return True if self.find_empty() == (-1, -1) else False

    def update_board(self) -> None:
        for i in range(9):
            for j in range(9):
                self.userValues[i][j] = self.cell_board[i][j].value

    def find_empty(self) -> tuple[int, int]:
        for i in range(9):
            for j in range(9):
                if self.cell_board[i][j].value == 0:
                    return i, j

        return -1, -1

    def check_board(self) -> bool:
        self.update_board()
        checker: sudoku_generator.SudokuGenerator = sudoku_generator.SudokuGenerator(9, 9)
        checker.board = self.userValues
        for i in range(9):
            for j in range(9):
                if not checker.is_valid(i, j, self.userValues[i][j]):
                    return False

        return True