import pygame
import config
from Scenes.scene import Scene
from textmanager import TextManager
from Scenes.menuScene import MenuScene


def main() -> None:
    pygame.init()
    pygame.display.set_caption(config.TITLE)
    pygame.display.set_icon(pygame.image.load(config.ICON))
    screen: pygame.Surface = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))

    clock: pygame.time.Clock = pygame.time.Clock()
    run: bool = True

    textManager: TextManager = TextManager(screen)
    scene: Scene = MenuScene(screen)

    events: list[pygame.event.Event] = []

    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                run = False

        scene.update(events)
        if scene.nextScene is not None:
            scene = scene.nextScene
        if scene.doExit:
            run = False
        if scene.doRestart:
            scene = MenuScene(screen)

        pygame.display.flip()
        clock.tick(config.FPS_CAP)


if __name__ == '__main__':
    main()
