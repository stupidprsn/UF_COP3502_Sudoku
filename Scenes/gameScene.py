import pygame
import config
from board import Board
from difficulty import Difficulty
from typing import Self
from Scenes.scene import Scene
from textmanager import TextManager
from Scenes.resultScene import ResultScene
from button import Button


class GameScene(Scene):
    # self._row and self._col are initialized to a value of -1 to show that they have not been selected yet.
    def __init__(self, screen: pygame.Surface, difficulty: Difficulty) -> None:
        self._nextScene: Scene = None
        self._doExit: bool = False
        self._doRestart: bool = False
        self._screen: pygame.Surface = screen
        self._textManager: TextManager = TextManager.getInstance()
        self._board: Board = Board(config.WINDOW_WIDTH, config.WINDOW_WIDTH, screen, difficulty)
        self._row: int = -1
        self._col: int = -1
        self._background: pygame.Surface = pygame.image.load(config.BACKGROUND_IMAGE)
        self._backgroundRect: pygame.Rect = self._background.get_rect(
            topleft=(0, 0)
        )
        self._buttons: list[Button] = [
            Button(screen, "RESET", (config.WINDOW_WIDTH // 2) - config.HOME_BUTTON_OFFSET,
                   config.HOME_BUTTON_Y, self.resetButton),
            Button(screen, "RESTART", (config.WINDOW_WIDTH // 2), config.HOME_BUTTON_Y,
                   self.restartButton),
            Button(screen, "EXIT", (config.WINDOW_WIDTH // 2) + config.HOME_BUTTON_OFFSET,
                   config.HOME_BUTTON_Y, self.exitButton)
        ]

    def update(self, events: list[pygame.event.Event]) -> None:
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                pos: tuple[int, int] = self._board.click(event.pos[0], event.pos[1])
                if pos is not None:
                    self._col, self._row = pos
                    self._board.select(self._row, self._col)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                    self._board.clear()
                elif event.key == pygame.K_RETURN:
                    self._board.place_number()
                    if self._board.is_full():
                        if self._board.check_board():
                            self._nextScene = ResultScene(self._screen, True)
                        else:
                            self._nextScene = ResultScene(self._screen, False)
                elif (event.key == pygame.K_w or event.key == pygame.K_UP) and self._row != -1 and self._col != -1:
                    self._row -= 1
                    if self._row < 0:
                        self._row = 8
                    self._board.select(self._row, self._col)
                elif (event.key == pygame.K_s or event.key == pygame.K_DOWN) and self._row != -1 and self._col != -1:
                    self._row += 1
                    if self._row > 8:
                        self._row = 0
                    self._board.select(self._row, self._col)
                elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and self._col != -1 and self._col != -1:
                    self._col -= 1
                    if self._col < 0:
                        self._col = 8
                    self._board.select(self._row, self._col)
                elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and self._row != -1 and self._col != -1:
                    self._col += 1
                    if self._col > 8:
                        self._col = 0
                    self._board.select(self._row, self._col)
                else:
                    num: int = event.key - ord('0')
                    if 1 <= num <= 9:
                        self._board.sketch(num)

        self._screen.blit(self._background, self._backgroundRect)
        self._board.draw()
        mouse: tuple[int, int] = pygame.mouse.get_pos()
        for button in self._buttons:
            button.update(events, mouse)

    def restartButton(self) -> None:
        self._doRestart = True

    def resetButton(self) -> None:
        self._board.reset_to_original()

    @property
    def doRestart(self) -> bool:
        return self._doRestart

    def exitButton(self) -> None:
        self._doExit = True

    @property
    def nextScene(self) -> Self:
        return self._nextScene

    @property
    def doExit(self) -> bool:
        return self._doExit
