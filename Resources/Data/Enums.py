from enum import Enum


# MAIN STATE ENUM
class MainSt(Enum):
    MAIN_MENU = 1
    MENU_SETTINGS = 12
    GAME_LOOP = 2
    CREDITS = 3
    EXIT = 666


# noinspection SpellCheckingInspection
class GameSt(Enum):
    MAIN_SCREEN = 0     # DEFAULT
    SHIP = 1            # SHADE TOWARDS
    INVENTORY = 2       # SHADE LEFT
    CHARACTERS = 3      # SHADE RIGHT
    SETTINGS = 5        # SHADE INWARDS
    DATABASE = 6       # SHADE DOWN
    MISSIONS = 7       # SHADE UP       <<< lehet character menüpont alá kéne tenni

    FIGHT = 444         # SHADE TOWARDS

class Values(Enum):
    ITEM = 0
    WEAPON = 1
    ARMOR = 2
    GADGET = 3
    FOOD = 4
    TRINKET = 5
    PART = 6
