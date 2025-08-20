import pygame as pg
from Data.VARIABLES import FPS, VELOCITYS, SCREEN_RES
from icecream import ic
from Data.Enums import st


class Main_Menu:
    def __init__(self, game_surface, screen, clock, screenWidth, screenHeight):
        self.game_surface = game_surface
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.screen = screen
        self.clock = clock

        self.cursor: int = 0
        self.CURSOR_MAX: int = 2    # New Game, Settings, Credits, EXIT
        
        # LOAD Data
        root: str = "Data/Bgs/Main_Menu_bgs/"
        self.Csillagok_1 =      pg.image.load(f"{root}Csillagok_1.png").convert_alpha()
        self.Csillagok_2 =      pg.image.load(f"{root}Csillagok_2.png").convert_alpha()
        self.Bolygók_1 =        pg.image.load(f"{root}Bolygók_1.png").convert_alpha()
        self.Ködök =            pg.image.load(f"{root}Ködök.png").convert_alpha()
        self.Csillagok_3 =      pg.image.load(f"{root}Csillagok_3.png").convert_alpha()
        self.Bolygók_2 =        pg.image.load(f"{root}Bolygók_2.png").convert_alpha()
        self.Background =       pg.image.load(f"{root}Background.png").convert_alpha()

        root = "Data/Objects/Main_Menu_texts/"
        self.CursorPic =        pg.image.load(f"{root}Cursor.png").convert_alpha()
        self.CreditsPic =       pg.image.load(f"{root}CREDITS.png").convert_alpha()
        self.NewGamePic =       pg.image.load(f"{root}NEW_GAME.png").convert_alpha()
        self.SettingsPic =      pg.image.load(f"{root}SETTINGS.png").convert_alpha()


    def main(self):

        bgPositions: list[float] = [0,0,0,0,0,0]
        cursorPos_y: list[int] = [0,26,52]
        MAX_DIFF: int = 1080

        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                     return st.EXIT
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_w:
                        self.cursor_up()
                    elif event.key == pg.K_s:
                        self.cursor_down()
                    elif event.key == pg.K_d:
                        ret = self.cursor_execute()
                        return ret


            # MOVING BACKGROUND
            self.game_surface.blit(self.Background,     (0, 0))
            self.game_surface.blit(self.Bolygók_2,      (0, bgPositions[5]))
            self.game_surface.blit(self.Bolygók_2,      (0, bgPositions[5] + MAX_DIFF))
            self.game_surface.blit(self.Csillagok_3,    (0, bgPositions[4]))
            self.game_surface.blit(self.Csillagok_3,    (0, bgPositions[4] + MAX_DIFF))
            self.game_surface.blit(self.Ködök,          (0, bgPositions[3]))
            self.game_surface.blit(self.Ködök,          (0, bgPositions[3] + MAX_DIFF))
            self.game_surface.blit(self.Bolygók_1,      (0, bgPositions[2]))
            self.game_surface.blit(self.Bolygók_1,      (0, bgPositions[2] + MAX_DIFF))
            self.game_surface.blit(self.Csillagok_2,    (0, bgPositions[1]))
            self.game_surface.blit(self.Csillagok_2,    (0, bgPositions[1] + MAX_DIFF))
            self.game_surface.blit(self.Csillagok_1,    (0, bgPositions[0]))
            self.game_surface.blit(self.Csillagok_1,    (0, bgPositions[0] + MAX_DIFF))

            # Adjust positions
            for i in range(len(bgPositions)):
                bgPositions[i] -= VELOCITYS[i]
                if bgPositions[i] < -MAX_DIFF:
                    bgPositions[i] = 0

            # TEXTS and CURSOR
            self.game_surface.blit(self.CursorPic, (0, cursorPos_y[self.cursor]))
            self.game_surface.blit(self.CreditsPic, (0,0))
            self.game_surface.blit(self.NewGamePic, (0,0))
            self.game_surface.blit(self.SettingsPic, (0,0))





            # Screen work
            scaled_surface = pg.transform.scale(self.game_surface, (self.screenWidth, self.screenHeight))
            self.screen.blit(scaled_surface, (0, 0))
            pg.display.flip()
            self.clock.tick(FPS)


    def cursor_up(self) -> None:
        if self.cursor > 0:
            self.cursor -= 1
        ic(self.cursor)


    def cursor_down(self) -> None:
        if self.cursor < self.CURSOR_MAX:
            self.cursor += 1
        ic(self.cursor)


    def cursor_execute(self):
        ic()
        match self.cursor:
            case 0:
                return st.GAME_LOOP
            case 1:
                return st.MENU_SETTINGS
            case 2:
                # TODO make a credits sceen
                return st.MAIN_MENU
            case 3:
                return st.EXIT
            case _:
                raise Exception


class Main_Settings:
    def __init__(self, game_surface, screen, clock, screenWidth, screenHeight):
        self.game_surface = game_surface
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.screen = screen
        self.clock = clock

        # LOAD Data
        self.default_bg = pg.image.load("Data/Bgs/resolution_test_2.png").convert_alpha()


    def main(self):
        while 1:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return st.EXIT
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        ic("Q is pressed")
                        return st.MAIN_MENU

            self.game_surface.fill((255, 0, 0))
            self.game_surface.blit(self.default_bg, (0, 0))

            scaled_surface = pg.transform.scale(self.game_surface, (self.screenWidth, self.screenHeight))
            self.screen.blit(scaled_surface, (0, 0))
            pg.display.flip()
            self.clock.tick(FPS)
