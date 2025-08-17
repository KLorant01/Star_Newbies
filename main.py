from enum import Enum
from icecream import ic
import pygame as pg

SCREEN_RES = (320, 180)  # "internal resolution"
FPS = 60


class st(Enum):
    MAIN_MENU = 1
    MENU_SETTINGS = 12
    GAME_LOOP = 2
    GAME_SETTINGS = 22
    EXIT = 66


class Main:
    def __init__(self):
        self.state = st.MAIN_MENU
        pg.init()

        videoInfo = pg.display.Info()
        self.screenWidth, self.screenHeight = videoInfo.current_w, videoInfo.current_h
        self.screen = pg.display.set_mode((self.screenWidth, self.screenHeight), pg.FULLSCREEN)

        self.game_surface = pg.Surface(SCREEN_RES)      # < this is the "game surface" where everything is rendered pixel-perfect
        self.clock = pg.time.Clock()                    # < Init system clock

        # LOAD RESOURCES
        self.default_bg = pg.image.load("resources/Bgs/resolution_test_2.png").convert_alpha()
        self.test_object = pg.image.load("resources/Modells/Box_modell_1.png").convert()
        self.test_object_2 = pg.image.load("resources/Modells/Box_modell_1.png").convert()


    def main(self):
        running = True
        while running:

            self.game_surface.fill((0, 0, 0))
            self.game_surface.blit(self.default_bg, (0, 0))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.state = st.EXIT

            match self.state:
                case st.MAIN_MENU:
                    ic("MAIN_MENU")
                    self.game_surface.blit(self.test_object, (5,5))

                case st.MENU_SETTINGS:
                    ic("MENU_SETTINGS")

                case st.GAME_LOOP:
                    ic("GAME_LOOP")

                case st.GAME_SETTINGS:
                    ic("GAME_SETTINGS")

                case st.EXIT:
                    ic("EXIT")
                    running = False

            # scale game surface → fullscreen, but keep it pixelated
            scaled_surface = pg.transform.scale(self.game_surface, (self.screenWidth, self.screenHeight))
            self.screen.blit(scaled_surface, (0, 0))

            # update
            pg.display.flip()
            self.clock.tick(FPS)

        pg.quit()

if __name__ == '__main__':
    game = Main()
    game.main()
