import config
import pygame
from typing import Optional
from typing import Self

'''
Manages building text
Implements singleton pattern
'''


class TextManager:

    _instance: Optional[Self] = None

    @staticmethod
    def getInstance() -> Self:
        if TextManager._instance is None:
            raise Exception("Text manager has not been initialized")
        return TextManager._instance

    def __init__(self, screen: pygame.Surface) -> None:
        self._screen: pygame.Surface = screen
        self._titleFont: pygame.font.Font = pygame.font.Font(config.FONT, config.TITLE_SIZE)
        self._subTitleFont: pygame.font.Font = pygame.font.Font(config.FONT, config.SUBTITLE_SIZE)
        self._sketchFont: pygame.font.Font = pygame.font.Font(config.FONT, config.SKETCH_SIZE)

        TextManager._instance = self

    # x, y coords are for center
    # Size should use values from config.py
    def getText(self, text: str, size: int, x: int, y: int) -> tuple[pygame.Surface, pygame.Rect]:
        surface: pygame.Surface = None
        match size:
            case config.TITLE_SIZE:
                surface: pygame.surface = self._titleFont.render(text, True, config.TEXT_COLOR)
            case config.SUBTITLE_SIZE:
                surface: pygame.surface = self._subTitleFont.render(text, True, config.TEXT_COLOR)
            case config.SKETCH_SIZE:
                surface: pygame.surface = self._sketchFont.render(text, True, config.BUTTON_COLOR)
        pos: pygame.Rect = surface.get_rect()
        pos.center = (x, y)
        return surface, pos
