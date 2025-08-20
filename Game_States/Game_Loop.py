import pygame as pg
from Data.VARIABLES import FPS
from icecream import ic
from Data.Enums import st



class Game_Loop:
    def __init__(self, game_surface, screen, clock, screenWidth, screenHeight):
        self.game_surface = game_surface
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.screen = screen
        self.clock = clock

        # LOAD Data
        # TODO change
        self.default_bg = pg.image.load("Data/Bgs/resolution_test_2.png").convert_alpha()


    def loop(self):
        while 1:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return st.MAIN_MENU
                elif event.type == pg.KEYDOWN:
                   ...


            self.game_surface.fill((0, 0, 255))
            self.game_surface.blit(self.default_bg, (0, 0))

            # Screen work
            scaled_surface = pg.transform.scale(self.game_surface, (self.screenWidth, self.screenHeight))
            self.screen.blit(scaled_surface, (0, 0))
            pg.display.flip()
            self.clock.tick(FPS)