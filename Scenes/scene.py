from abc import ABC, abstractmethod
import pygame
from typing import Optional
from typing import Self

class Scene(ABC):
    # Returns Scene
    @classmethod
    @abstractmethod
    def update(self, events: list[pygame.event.Event]) -> None:
        pass

    # Need to change scene?
    @property
    @abstractmethod
    def nextScene(self) -> Optional[Self]:
        pass

    # Need to exit?
    @property
    @abstractmethod
    def doExit(self) -> bool:
        pass

    # Restart
    @property
    @abstractmethod
    def doRestart(self) -> bool:
        pass