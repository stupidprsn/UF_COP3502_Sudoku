from Scenes.scene import Scene
import pygame
from textmanager import TextManager
import config
from button import Button


class ResultScene(Scene):
    def __init__(self, screen: pygame.Surface, win: bool) -> None:
        self._screen: pygame.Surface = screen
        self._background: pygame.Surface = pygame.image.load(config.BACKGROUND_IMAGE)
        self._doRestart: bool = False
        self._backgroundRect: pygame.Rect = self._background.get_rect(
            topleft=(0, 0)
        )
        self._nextScene: Scene = None
        self._textManger: TextManager = TextManager.getInstance()
        self._doExit: bool = False
        if win:
            self._text: tuple[pygame.Surface, pygame.Rect] = self._textManger.getText("Game Won!", config.TITLE_SIZE,
                                                                                      config.WELCOME_POS[0],
                                                                                      config.WELCOME_POS[1])
            self._button: Button = Button(screen, "EXIT", (config.WINDOW_WIDTH // 2), config.HOME_BUTTON_Y,
                                          self.exitButton)
        else:
            self._text: tuple[pygame.Surface, pygame.Rect] = self._textManger.getText("Game Over :(", config.TITLE_SIZE,
                                                                                      config.WELCOME_POS[0],
                                                                                      config.WELCOME_POS[1])
            self._button: Button = Button(screen, "RESTART", (config.WINDOW_WIDTH // 2), config.HOME_BUTTON_Y,
                                          self.restartButton)

    def update(self, events: list[pygame.event.Event]) -> None:
        self._screen.blit(self._background, self._backgroundRect)
        self._screen.blit(self._text[0], self._text[1])
        self._button.update(events, pygame.mouse.get_pos())

    def exitButton(self) -> None:
        self._doExit = True

    def restartButton(self) -> None:
        self._doRestart = True

    @property
    def doExit(self) -> bool:
        return self._doExit

    @property
    def nextScene(self) -> Scene:
        return None

    @property
    def doRestart(self) -> bool:
        return self._doRestart
