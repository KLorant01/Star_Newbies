from Resources.Data.VARIABLES import SCREEN_RES
from Game.Main_Menu import MainMenu, MainSettings
from Game.Game_Loop import GameLoop
from Resources.Data.Enums import MainSt
import pygame as pg
import logging as lg


class Main:
    def __init__(self):
        pg.init()

        lg.info("pygame init")

        videoInfo = pg.display.Info()
        self.screenWidth, self.screenHeight = videoInfo.current_w, videoInfo.current_h
        self.screen = pg.display.set_mode((self.screenWidth, self.screenHeight), pg.FULLSCREEN)
#        self.screen = pg.display.set_mode((self.screenWidth, self.screenHeight))

        self.game_surface = pg.Surface(SCREEN_RES)      # < this is the "game surface" where everything is rendered pixel-perfect
        self.clock = pg.time.Clock()                    # < Init system clock


    def main(self):
        running: bool = True
        state: MainSt = MainSt.MAIN_MENU

        while running:
            match state:
                case MainSt.MAIN_MENU:
                    lg.info("MAIN_MENU")
                    state = MainMenu(self.game_surface, self.screen, self.clock, self.screenWidth,
                                     self.screenHeight).main()

                case MainSt.MENU_SETTINGS:
                    lg.info("MENU_SETTINGS")
                    state = MainSettings(self.game_surface, self.screen, self.clock, self.screenWidth,
                                         self.screenHeight).main()

                case MainSt.GAME_LOOP:
                    lg.info("GAME_LOOP")
                    state = GameLoop(self.game_surface, self.screen, self.clock, self.screenWidth,
                                     self.screenHeight).loop()

                case MainSt.EXIT:
                    lg.info("EXIT")
                    running = False
                    pg.display.quit()
                    pg.quit()


if __name__ == '__main__':
    lg.basicConfig(level=lg.DEBUG, filename="log.log", filemode="w",
                        format="%(asctime)s\t%(levelname)s\t%(filename)s\t%(funcName)s\t%(lineno)d\t%(message)s", )

    game = Main()
    game.main()
