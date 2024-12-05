import pygame
from typing import Callable
import config
from textmanager import TextManager

'''
Creates a button
**Call update method every frame**
'''
class Button:
    def __init__(self,
                 screen: pygame.Surface, text: pygame.Surface, x: int, y: int,
                 callback: Callable[[], None]) -> None:
        self._screen: pygame.Surface = screen
        self._text: tuple[pygame.Surface, pygame.Rect] = TextManager.getInstance().getText(text, config.BUTTON_TEXT, x, y)
        self._rect: pygame.Rect = pygame.Rect(0, 0, config.BUTTON_WIDTH, config.BUTTON_HEIGHT)
        self._rect.center = (x, y)
        self._callback = callback

    def update(self, events: list[pygame.event.Event], mouse: tuple[int, int]) -> None:
        # Hover effect!
        if not self._rect.collidepoint(mouse[0], mouse[1]):
            pygame.draw.rect(self._screen, config.BUTTON_COLOR, self._rect)
        else:
            pygame.draw.rect(self._screen, config.BUTTON_HOVER_COLOR, self._rect)
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
                    self._callback()
        self._screen.blit(self._text[0], self._text[1])
