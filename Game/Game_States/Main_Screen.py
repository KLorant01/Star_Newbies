import pygame as pg
from Resources.Data.VARIABLES import FPS, VELOCITYS
from Resources.Data.Enums import MainSt, GameSt
from Modules.Buttons.Button import Button
import logging as lg
from icecream import ic

from Modules.Text.Bitmap import BitmapFont



class MainScreen:
    def __init__(self, game_surface, screen, clock, screenwidth, screenheight):
        lg.info("init")
        self.game_surface = game_surface
        self.screenWidth = screenwidth
        self.screenHeight = screenheight
        self.screen = screen
        self.clock = clock

        self.game_state = GameSt.MAIN_SCREEN

        # MOVING BACKGROUND
        self.bgPositions: list[float] = [0,0,0,0,0,0]

        self.buttons = [
            Button("Star_System", 7, 622, 5, 64),
            Button("Time", 7, 263, 78, 135),
            Button("Mission_State", 7, 950, 150, 253),

            Button("Character_1", 7, 130, 282, 402),
            Button("Character_2", 7, 130, 412, 536),
            Button("Character_3", 7, 130, 546, 666),
            Button("Character_4", 7, 130, 676, 801),

            Button("Cargo", 280, 830, 0, 1022),
            Button("Database", 7, 275, 0, 930),
            Button("Settings", 1850, 1910, 11, 72),

            Button("Ship in the Middle", 865, 1440, 105, 930),
        ]

        # LOAD Resources
        root: str = "Resources/Sprites/Bgs/Space_bg/"
        self.Csillagok_1 = pg.image.load(f"{root}Csillagok_1.png").convert_alpha()
        self.Csillagok_2 = pg.image.load(f"{root}Csillagok_2.png").convert_alpha()
        self.Bolygok_1 = pg.image.load(f"{root}Bolygók_1.png").convert_alpha()
        self.Kodok = pg.image.load(f"{root}Ködök.png").convert_alpha()
        self.Csillagok_3 = pg.image.load(f"{root}Csillagok_3.png").convert_alpha()
        self.Bolygok_2 = pg.image.load(f"{root}Bolygók_2.png").convert_alpha()
        self.Background = pg.image.load(f"{root}Background.png").convert_alpha()


        # TODO change
        self.default_bg = pg.image.load("Resources/Sprites/Game/Test/Game_layout_test.png").convert_alpha()

    def main(self):
        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return MainSt.MAIN_MENU

                elif event.type == pg.KEYDOWN:
                    command = self.key_handler(event)
                    if not command is None:
                        return command


                elif event.type == pg.MOUSEMOTION:
                    self.maus_handler(event)

                elif event.type == pg.MOUSEBUTTONDOWN:
                    self.maus_handler(event, event.button)


            self.darw_bg()
            self.game_surface.blit(self.default_bg, (0, 0))

            self.update_screen()


    def maus_handler(self, event, push: int = 0):
        pos = event.pos
        cursorPosX, cursorPosY = pos[0], pos[1]
        for button in self.buttons:
            if button.action(cursorPosX, cursorPosY, push):
                break

    @staticmethod
    def key_handler(event: pg.event) -> GameSt | None:
        ic()
         # noinspection PyUnreachableCode
        match event.key:
            case pg.K_q | pg.K_ESCAPE:
                ic()
                return GameSt.SETTINGS
            case pg.K_c | pg.K_i:
                return GameSt.INVENTORY
            case pg.K_1 | pg.K_2 | pg.K_3 | pg.K_4:
                return GameSt.CHARACTERS
            case pg.K_m:
                return GameSt.MAP
            case pg.K_s:
                return GameSt.SHIP
            case _ :
                return None


    def darw_bg(self):
        MAX_DIFF: int = 1080

        self.game_surface.blit(self.Background,     (0, 0))
        self.game_surface.blit(self.Bolygok_2,      (0, self.bgPositions[5]))
        self.game_surface.blit(self.Bolygok_2,      (0, self.bgPositions[5] + MAX_DIFF))
        self.game_surface.blit(self.Csillagok_3,    (0, self.bgPositions[4]))
        self.game_surface.blit(self.Csillagok_3,    (0, self.bgPositions[4] + MAX_DIFF))
        self.game_surface.blit(self.Kodok,          (0, self.bgPositions[3]))
        self.game_surface.blit(self.Kodok,          (0, self.bgPositions[3] + MAX_DIFF))
        self.game_surface.blit(self.Bolygok_1,      (0, self.bgPositions[2]))
        self.game_surface.blit(self.Bolygok_1,      (0, self.bgPositions[2] + MAX_DIFF))
        self.game_surface.blit(self.Csillagok_2,    (0, self.bgPositions[1]))
        self.game_surface.blit(self.Csillagok_2,    (0, self.bgPositions[1] + MAX_DIFF))
        self.game_surface.blit(self.Csillagok_1,    (0, self.bgPositions[0]))
        self.game_surface.blit(self.Csillagok_1,    (0, self.bgPositions[0] + MAX_DIFF))

        # Adjust positions
        for i in range(len(self.bgPositions)):
            self.bgPositions[i] -= VELOCITYS[i]
            if self.bgPositions[i] < -MAX_DIFF:
                self.bgPositions[i] = 0


    def update_screen(self):
        scaled_surface = pg.transform.scale(self.game_surface, (self.screenWidth, self.screenHeight))
        self.screen.blit(scaled_surface, (0, 0))
        pg.display.flip()
        self.clock.tick(FPS)
