from typing import Final
from typing import Optional
from os import path

# Window Settings
TITLE: Final[str] = "Sudoku"
ICON: Final[str] = path.join("Resources", "sudoku.png")
WINDOW_WIDTH: Final[int] = 800
WINDOW_HEIGHT: Final[int] = 600
BACKGROUND_IMAGE: Final[str] = path.join("Resources", "background.jpg")
FPS_CAP: Final[int] = 60

# Text Settings
# Set FONT to None for default
FONT: Final[Optional[str]] = path.join("Resources", "SourGummy.ttf")
TITLE_SIZE: Final[int] = 60
SUBTITLE_SIZE: Final[int] = 40
TEXT_COLOR: Final[tuple[int, int, int]] = (60, 55, 68)

# Button Settings
BUTTON_WIDTH: Final[int] = 160
BUTTON_HEIGHT: Final[int] = 70
BUTTON_TEXT: Final[int] = SUBTITLE_SIZE
BUTTON_COLOR: Final[tuple[int, int, int]] = (121, 132, 120)
BUTTON_HOVER_COLOR: Final[tuple[int, int, int]] = (73, 79, 72)

# Main Menu
WELCOME_MSG: Final[str] = "Welcome to Sudoku!"
WELCOME_FONT_SIZE: Final[int] = TITLE_SIZE
WELCOME_POS: Final[tuple[int, int]] = (WINDOW_WIDTH // 2, 250)

SELECT_GAME_MSG: Final[str] = "Select Game Mode:"
SELECT_GAME_FONT_SIZE: Final[int] = SUBTITLE_SIZE
SELECT_GAME_POS: Final[tuple[int, int]] = (WINDOW_WIDTH // 2, 550)

HOME_BUTTON_Y: Final[int] = 650
HOME_BUTTON_OFFSET: Final[int] = 220

