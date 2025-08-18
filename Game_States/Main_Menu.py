import pygame as pg
from data_.VARIABLES import FPS
from icecream import ic
from data_.Enums import st

# TODO make it work


class Main_Menu:
    def __init__(self, game_surface, screen, clock, screenWidth, screenHeight):
        self.game_surface = game_surface
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.screen = screen
        self.clock = clock

        # LOAD data_
        self.default_bg = pg.image.load("data_/Bgs/resolution_test_2.png").convert_alpha()


    def main(self):
        while 1:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    ic("return")
                    return st.EXIT

            self.game_surface.fill((0, 255, 0))
            self.game_surface.blit(self.default_bg, (0, 0))


            # scale game surface → fullscreen, but keep it pixelated
            scaled_surface = pg.transform.scale(self.game_surface, (self.screenWidth, self.screenHeight))
            self.screen.blit(scaled_surface, (0, 0))

            # update
            pg.display.flip()
            self.clock.tick(FPS)

