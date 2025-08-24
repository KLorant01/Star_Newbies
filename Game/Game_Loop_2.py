import pygame as pg
from Resources.Data.VARIABLES import FPS, VELOCITYS
from Resources.Data.Enums import MainSt, GameSt
from Modules.Buttons.Button import Button
import logging as lg


class GameLoop:
    def __init__(self, game_surface, screen, clock, screenwidth, screenheight):
        lg.info("init")

        self.game_surface = game_surface
        self.screenWidth = screenwidth
        self.screenHeight = screenheight
        self.screen = screen
        self.clock = clock


        # LOAD Resources
        root: str = "Resources/Sprites/Bgs/Space_bg/"
        self.Csillagok_1 =      pg.image.load(f"{root}Csillagok_1.png").convert_alpha()
        self.Csillagok_2 =      pg.image.load(f"{root}Csillagok_2.png").convert_alpha()
        self.Bolygok_1 =        pg.image.load(f"{root}Bolygók_1.png").convert_alpha()
        self.Kodok =            pg.image.load(f"{root}Ködök.png").convert_alpha()
        self.Csillagok_3 =      pg.image.load(f"{root}Csillagok_3.png").convert_alpha()
        self.Bolygok_2 =        pg.image.load(f"{root}Bolygók_2.png").convert_alpha()
        self.Background =       pg.image.load(f"{root}Background.png").convert_alpha()


    def loop(self):

        bgPositions: list[float] = [0,0,0,0,0,0]
        MAX_DIFF: int = 1080
        game_state = GameSt.MAIN_SCREEN

        while 1:
            match game_state:
                case GameSt.MAIN_SCREEN:
                    game_state =


            # MOVING BACKGROUND
            self.game_surface.blit(self.Background,     (0, 0))
            self.game_surface.blit(self.Bolygok_2,      (0, bgPositions[5]))
            self.game_surface.blit(self.Bolygok_2,      (0, bgPositions[5] + MAX_DIFF))
            self.game_surface.blit(self.Csillagok_3,    (0, bgPositions[4]))
            self.game_surface.blit(self.Csillagok_3,    (0, bgPositions[4] + MAX_DIFF))
            self.game_surface.blit(self.Kodok,          (0, bgPositions[3]))
            self.game_surface.blit(self.Kodok,          (0, bgPositions[3] + MAX_DIFF))
            self.game_surface.blit(self.Bolygok_1,      (0, bgPositions[2]))
            self.game_surface.blit(self.Bolygok_1,      (0, bgPositions[2] + MAX_DIFF))
            self.game_surface.blit(self.Csillagok_2,    (0, bgPositions[1]))
            self.game_surface.blit(self.Csillagok_2,    (0, bgPositions[1] + MAX_DIFF))
            self.game_surface.blit(self.Csillagok_1,    (0, bgPositions[0]))
            self.game_surface.blit(self.Csillagok_1,    (0, bgPositions[0] + MAX_DIFF))

            # Adjust positions
            for i in range(len(bgPositions)):
                bgPositions[i] -= VELOCITYS[i]
                if bgPositions[i] < -MAX_DIFF:
                    bgPositions[i] = 0

            self.game_surface.blit(self.default_bg, (0, 0))

            # Screen work
            scaled_surface = pg.transform.scale(self.game_surface, (self.screenWidth, self.screenHeight))
            self.screen.blit(scaled_surface, (0, 0))
            pg.display.flip()
            self.clock.tick(FPS)

