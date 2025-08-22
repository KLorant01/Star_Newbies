from enum import Enum


# MAIN STATE ENUM
class main_st(Enum):
    MAIN_MENU = 1
    MENU_SETTINGS = 12
    GAME_LOOP = 2
    EXIT = 66


class game_st(Enum):
    MAIN_SCREEN = 0     # DEFAULT
    SHIP = 1            # SHADE TOWARDS
    INVENTORY = 2       # SHADE LEFT
    CHARACTERS = 3      # SHADE RIGHT
    MAP = 4             # SHADE INWARDS
    SETTINGS = 5        # SHADE INWARDS
    WIKIPEDIA = 6       # SHADE DOWN
    PROCESSES = 7       # SHADE UP

    FIGHT = 444         # SHADE TOWARDS

