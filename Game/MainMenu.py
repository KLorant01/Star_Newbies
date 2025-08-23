import pygame as pg
from Resources.Data.VARIABLES import FPS, VELOCITYS
from icecream import ic
from Resources.Data.Enums import MainSt


class MainMenu:
    def __init__(self, game_surface, screen, clock, screenwidth, screenheight):
        self.game_surface = game_surface
        self.screenWidth = screenwidth
        self.screenHeight = screenheight
        self.screen = screen
        self.clock = clock

        self.cursor: int = 0
        self.CURSOR_MAX: int = 2    # New Game, Settings, Credits, EXIT
        
        # LOAD Resources
        root: str = "Resources/Sprites/Bgs/Main_Menu_bgs/"
        self.Csillagok_1 =      pg.image.load(f"{root}Csillagok_1.png").convert_alpha()
        self.Csillagok_2 =      pg.image.load(f"{root}Csillagok_2.png").convert_alpha()
        self.Bolygok_1 =        pg.image.load(f"{root}Bolygók_1.png").convert_alpha()
        self.Kodok =            pg.image.load(f"{root}Ködök.png").convert_alpha()
        self.Csillagok_3 =      pg.image.load(f"{root}Csillagok_3.png").convert_alpha()
        self.Bolygok_2 =        pg.image.load(f"{root}Bolygók_2.png").convert_alpha()
        self.Background =       pg.image.load(f"{root}Background.png").convert_alpha()

        root = "Resources/Sprites/Objects/Main_Menu_texts/"
        self.CursorPic =        pg.image.load(f"{root}Cursor.png").convert_alpha()
        self.CreditsPic =       pg.image.load(f"{root}CREDITS.png").convert_alpha()
        self.NewGamePic =       pg.image.load(f"{root}NEW_GAME.png").convert_alpha()
        self.SettingsPic =      pg.image.load(f"{root}SETTINGS.png").convert_alpha()


    def main(self):

        bgPositions: list[float] = [0,0,0,0,0,0]
        cursorPos_y: list[int] = [0,26,52]
        MAX_DIFF: int = 1080
        clearScreen: bool = False

        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                     return MainSt.EXIT
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_w or event.key == pg.K_UP:
                        self.cursor_up()
                    elif event.key == pg.K_s or event.key == pg.K_DOWN:
                        self.cursor_down()
                    elif event.key == pg.K_d or event.key == pg.K_RETURN or event.key == pg.K_RIGHT:
                        return self.cursor_execute
                    elif event.key == pg.K_h:
                        clearScreen = not clearScreen


            # MOVING BACKGROUND
            self.game_surface.blit(self.Background,     (0, 0))
            self.game_surface.blit(self.Bolygok_2, (0, bgPositions[5]))
            self.game_surface.blit(self.Bolygok_2, (0, bgPositions[5] + MAX_DIFF))
            self.game_surface.blit(self.Csillagok_3,    (0, bgPositions[4]))
            self.game_surface.blit(self.Csillagok_3,    (0, bgPositions[4] + MAX_DIFF))
            self.game_surface.blit(self.Kodok, (0, bgPositions[3]))
            self.game_surface.blit(self.Kodok, (0, bgPositions[3] + MAX_DIFF))
            self.game_surface.blit(self.Bolygok_1, (0, bgPositions[2]))
            self.game_surface.blit(self.Bolygok_1, (0, bgPositions[2] + MAX_DIFF))
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
            if not clearScreen:
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


    # noinspection PyUnreachableCode
    def cursor_execute(self):
        match self.cursor:
            case 0:
                return MainSt.GAME_LOOP
            case 1:
                return MainSt.MENU_SETTINGS
            case 2:
                # TODO make a credits screen
                return MainSt.MAIN_MENU
            case 3:
                return MainSt.EXIT
            case _:
                raise Exception


class MainSettings:
    def __init__(self, game_surface, screen, clock, screenwidth, screenheight):
        self.game_surface = game_surface
        self.screenWidth = screenwidth
        self.screenHeight = screenheight
        self.screen = screen
        self.clock = clock

        # LOAD Resources
        self.default_bg = pg.image.load("Resources/Sprites/Bgs/resolution_test_2.png").convert_alpha()

        # LOAD Resources
        root: str = "Resources/Sprites/Bgs/Main_Menu_bgs/"
        self.Csillagok_1 =      pg.image.load(f"{root}Csillagok_1.png").convert_alpha()
        self.Csillagok_2 =      pg.image.load(f"{root}Csillagok_2.png").convert_alpha()
        self.Bolygok_1 =        pg.image.load(f"{root}Bolygók_1.png").convert_alpha()
        self.Kodok =            pg.image.load(f"{root}Ködök.png").convert_alpha()
        self.Csillagok_3 =      pg.image.load(f"{root}Csillagok_3.png").convert_alpha()
        self.Bolygok_2 =        pg.image.load(f"{root}Bolygók_2.png").convert_alpha()
        self.Background =       pg.image.load(f"{root}Background.png").convert_alpha()

        root = "Resources/Sprites/Objects/MainSettings/"
        self.placeholder =      pg.image.load(f"{root}Menu_Settings_Placeholder.png").convert_alpha()



    def main(self):
        bgPositions: list[float] = [0,0,0,0,0,0]
        MAX_DIFF: int = 1080

        while 1:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return MainSt.EXIT
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_q or event.key == pg.K_ESCAPE:
                        ic("Q is pressed")
                        return MainSt.MAIN_MENU


            # MOVING BACKGROUND
            self.game_surface.blit(self.Background,     (0, 0))
            self.game_surface.blit(self.Bolygok_2, (0, bgPositions[5]))
            self.game_surface.blit(self.Bolygok_2, (0, bgPositions[5] + MAX_DIFF))
            self.game_surface.blit(self.Csillagok_3,    (0, bgPositions[4]))
            self.game_surface.blit(self.Csillagok_3,    (0, bgPositions[4] + MAX_DIFF))
            self.game_surface.blit(self.Kodok, (0, bgPositions[3]))
            self.game_surface.blit(self.Kodok, (0, bgPositions[3] + MAX_DIFF))
            self.game_surface.blit(self.Bolygok_1, (0, bgPositions[2]))
            self.game_surface.blit(self.Bolygok_1, (0, bgPositions[2] + MAX_DIFF))
            self.game_surface.blit(self.Csillagok_2,    (0, bgPositions[1]))
            self.game_surface.blit(self.Csillagok_2,    (0, bgPositions[1] + MAX_DIFF))
            self.game_surface.blit(self.Csillagok_1,    (0, bgPositions[0]))
            self.game_surface.blit(self.Csillagok_1,    (0, bgPositions[0] + MAX_DIFF))

            # Adjust positions
            for i in range(len(bgPositions)):
                bgPositions[i] -= VELOCITYS[i]
                if bgPositions[i] < -MAX_DIFF:
                    bgPositions[i] = 0

            # PLACEHOLDER
            self.game_surface.blit(self.placeholder,    (0, 0))


            scaled_surface = pg.transform.scale(self.game_surface, (self.screenWidth, self.screenHeight))
            self.screen.blit(scaled_surface, (0, 0))
            pg.display.flip()
            self.clock.tick(FPS)
