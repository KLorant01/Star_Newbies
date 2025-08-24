import pygame as pg
from Resources.Data.VARIABLES import FPS, VELOCITYS
from Resources.Data.Enums import MainSt, GameSt
from Game.Game_States.Main_Screen import MainScreen
import logging as lg
from icecream import ic


class GameLoop:
    def __init__(self, game_surface, screen, clock, screenwidth, screenheight):
        lg.info("init")

        self.game_surface = game_surface
        self.screenWidth = screenwidth
        self.screenHeight = screenheight
        self.screen = screen
        self.clock = clock


    def loop(self):
        game_state = GameSt.MAIN_SCREEN

        while 1:
            match game_state:
                case GameSt.MAIN_SCREEN:
                    lg.info("Go to GameSt.MAIN_SCREEN")
                    game_state = MainScreen(self.game_surface, self.screen, self.clock, self.screenWidth, self.screenHeight).main()

                case GameSt.SHIP:
                   lg.info("Go to GameSt.SHIP")
                   raise NotImplementedError("Feature GameSt.SHIP not implemented yet")

                case GameSt.INVENTORY:
                   lg.info("Go to GameSt.INVENTORY")
                   raise NotImplementedError("Feature GameSt.INVE not implemented yet")

                case GameSt.CHARACTERS:
                   lg.info("Go to GameSt.CHARACTERS")
                   raise NotImplementedError("Feature GameSt.CHAR not implemented yet")

                case GameSt.MAP:
                   lg.info("Go to GameSt.MAP")
                   raise NotImplementedError("Feature GameSt.MAP not implemented yet")

                case GameSt.SETTINGS:
                   lg.info("Go to GameSt.SETTINGS")
                   raise NotImplementedError("Feature GameSt.SETT not implemented yet")

                case GameSt.PROCESSES:
                   lg.info("Go to GameSt.PROCESSES")
                   raise NotImplementedError("Feature GameSt.PROC not implemented yet")

                case GameSt.FIGHT:
                   lg.info("Go to GameSt.FIGHT")
                   raise NotImplementedError("Feature GameSt.FIGH not implemented yet")

                case MainSt.MAIN_MENU:
                    return MainSt.MAIN_MENU

