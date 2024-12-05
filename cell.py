import pygame

import config
from textmanager import TextManager


class Cell:
    def __init__(self, row: int, col: int, screen: pygame.Surface, value: int = 0) -> None:
        self.row: int = row
        self.col: int = col
        self.screen: pygame.Surface = screen
        self.value: int = value

        self._textManager: TextManager = TextManager.getInstance()
        self._text: tuple[pygame.Surface, pygame.Rect] = None

        self.sketched_value: int = 0
        self.canEdit: bool = True if value == 0 else False
        self.selected: bool = False
        self.rect: pygame.Rect = pygame.Rect(col * 64, row * 64, 64, 64)

        if value != 0:
            self._text = self._textManager.getText(
                str(self.value), config.SUBTITLE_SIZE, self.col * 64 + 64 / 2, self.row * 64 + 64 / 2
            )


    def set_cell_value(self) -> None:
        if self.canEdit:
            self.value = self.sketched_value
            self._text = self._textManager.getText(
                str(self.value), config.SUBTITLE_SIZE, self.col * 64 + 64 / 2, self.row * 64 + 64 / 2
            )

    def set_sketched_value(self, value: int) -> None:
        if self.canEdit:
            self.sketched_value = value
            self._text = self._textManager.getText(
                str(value), config.SKETCH_SIZE, self.col * 64 + 64 / 2, self.row * 64 + 64 / 2
            )

    def draw(self) -> None:
        pygame.draw.line(self.screen, "black", (self.col * 64, self.row * 64), ((self.col + 1) * 64, self.row * 64))
        pygame.draw.line(self.screen, "black", (self.col * 64, self.row * 64), (self.col * 64, (self.row + 1) * 64))
        pygame.draw.line(self.screen, "black", (self.col * 64, (self.row + 1) * 64), ((self.col + 1) * 64, (self.row + 1) * 64))
        pygame.draw.line(self.screen, "black", ((self.col + 1) * 64, self.row * 64), ((self.col + 1) * 64, (self.row + 1) * 64))

        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 2)

        if self._text is not None:
            self.screen.blit(self._text[0], self._text[1])
