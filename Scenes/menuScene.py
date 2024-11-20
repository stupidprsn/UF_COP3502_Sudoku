import config
import pygame
from typing import Optional
from Scenes.gameScene import GameScene
from button import Button
from textmanager import TextManager
from Scenes.scene import Scene
from difficulty import Difficulty

class MenuScene(Scene):
    def __init__(self, screen: pygame.Surface, textManager: TextManager) -> None:
        self._nextScene: Optional[Scene] = None
        self._screen: pygame.Surface = screen
        self._background: pygame.Surface = pygame.image.load(config.BACKGROUND_IMAGE)
        self._backgroundRect: pygame.Rect = self._background.get_rect(
            topleft=(0,0)
        )
        self._textManager: TextManager = textManager
        self._texts: list[tuple[pygame.Surface, pygame.Rect]] = [
            textManager.getText(config.WELCOME_MSG, config.TITLE_SIZE, config.WELCOME_POS[0], config.WELCOME_POS[1]),
            textManager.getText(config.SELECT_GAME_MSG, config.SUBTITLE_SIZE, config.SELECT_GAME_POS[0],
                                config.SELECT_GAME_POS[1])
        ]
        self._buttons: list[Button] = [
            Button(textManager, screen, "EASY", (config.WINDOW_WIDTH // 2) - config.HOME_BUTTON_OFFSET,
                   config.HOME_BUTTON_Y, self.easyButton),
            Button(textManager, screen, "MEDIUM", (config.WINDOW_WIDTH // 2), config.HOME_BUTTON_Y, self.mediumButton),
            Button(textManager, screen, "HARD", (config.WINDOW_WIDTH // 2) + config.HOME_BUTTON_OFFSET,
                   config.HOME_BUTTON_Y, self.hardButton)
        ]

    def update(self, events: list[pygame.event.Event]) -> None:
        self._screen.blit(self._background, self._background.get_rect(
            topleft=(0, 0)
        ))
        for text in self._texts:
            self._screen.blit(text[0], text[1])
        mouse: tuple[int, int] = pygame.mouse.get_pos()
        for button in self._buttons:
            button.update(events, mouse)

    @property
    def nextScene(self) -> Scene:
        return self._nextScene

    @property
    def doRestart(self) -> bool:
        return False

    @property
    def doExit(self) -> bool:
        return False

    def easyButton(self) -> None:
        self._nextScene = GameScene(self._screen, self._textManager, Difficulty.easy)

    def mediumButton(self) -> None:
        self._nextScene = GameScene(self._screen, self._textManager, Difficulty.medium)

    def hardButton(self) -> None:
        self._nextScene = GameScene(self._screen, self._textManager, Difficulty.hard)
