import pygame as pg
from Resources.Data.VARIABLES import FPS, VELOCITYS
from Resources.Data.Enums import MainSt
# import logging as lg


class MainSettings:
    def __init__(self, game_surface, screen, clock, screenwidth, screenheight):
        self.game_surface = game_surface
        self.screenWidth = screenwidth
        self.screenHeight = screenheight
        self.screen = screen
        self.clock = clock

        self.bgPositions: list[float] = [0,0,0,0,0,0]               # MOVING BACKGROUND

        # LOAD Resources
        root: str = "Resources/Sprites/Bgs/Space_bg/"
        self.Csillagok_1 =      pg.image.load(f"{root}Csillagok_1.png").convert_alpha()
        self.Csillagok_2 =      pg.image.load(f"{root}Csillagok_2.png").convert_alpha()
        self.Bolygok_1 =        pg.image.load(f"{root}Bolygók_1.png").convert_alpha()
        self.Kodok =            pg.image.load(f"{root}Ködök.png").convert_alpha()
        self.Csillagok_3 =      pg.image.load(f"{root}Csillagok_3.png").convert_alpha()
        self.Bolygok_2 =        pg.image.load(f"{root}Bolygók_2.png").convert_alpha()
        self.Background =       pg.image.load(f"{root}Background.png").convert_alpha()

        root = "/home/lorant/PycharmProjects/Star_Newbies/Resources/Sprites/Objects/Text/Text_1/"
        self.placeholder = pg.image.load(f"{root}Aseprite_mini_fontmap.png").convert_alpha()

#        root = "Resources/Sprites/Objects/Main_Settings/"
#        self.placeholder =      pg.image.load(f"{root}Menu_Settings_Placeholder.png").convert_alpha()


    def main(self):
        while 1:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return MainSt.EXIT

                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_q or event.key == pg.K_ESCAPE:
                        return MainSt.MAIN_MENU

            self.draw_bg()
            self.game_surface.blit(self.placeholder,    (0, 0))

            self.update_screen()


    def draw_bg(self):
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
