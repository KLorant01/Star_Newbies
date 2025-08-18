from icecream import ic
import pygame as pg
from data_.VARIABLES import SCREEN_RES
from Game_States.Main_Menu import Main_Menu, Main_Settings
from data_.Enums import st


class Main:
    def __init__(self):
        pg.init()

        videoInfo = pg.display.Info()
        self.screenWidth, self.screenHeight = videoInfo.current_w, videoInfo.current_h
#        self.screen = pg.display.set_mode((self.screenWidth, self.screenHeight), pg.FULLSCREEN)
        self.screen = pg.display.set_mode((self.screenWidth, self.screenHeight))

        self.game_surface = pg.Surface(SCREEN_RES)      # < this is the "game surface" where everything is rendered pixel-perfect
        self.clock = pg.time.Clock()                    # < Init system clock


    def main(self):
        running: bool = True
        state: st = st.MENU_SETTINGS

        while running:
            match state:
                case st.MAIN_MENU:
                    ic("MAIN_MENU")
                    state = Main_Menu(self.game_surface, self.screen, self.clock, self.screenWidth, self.screenHeight).main()

                case st.MENU_SETTINGS:
                    ic("MENU_SETTINGS")
                    state = Main_Settings(self.game_surface, self.screen, self.clock, self.screenWidth, self.screenHeight).main()

                case st.GAME_LOOP:
                    ic("GAME_LOOP")

                case st.GAME_SETTINGS:
                    ic("GAME_SETTINGS")

                case st.EXIT:
                    ic("EXIT")
                    running = False
                    pg.display.quit()
                    pg.quit()


if __name__ == '__main__':
    game = Main()
    game.main()
