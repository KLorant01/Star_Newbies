import pygame as pg
from Resources.Data.VARIABLES import FPS, VELOCITYS, shared_bgPositions
from Resources.Data.Enums import MainSt
import logging as lg


class MainMenu:
    def __init__(self, game_surface, screen, clock, screenwidth, screenheight):
        self.game_surface = game_surface
        self.screenWidth = screenwidth
        self.screenHeight = screenheight
        self.screen = screen
        self.clock = clock

        self.cursor: int = 0
        self.CURSOR_MAX: int = 3    # New Game, Settings, Credits, EXIT

        # MOVING BACKGROUND
        self.bgPositions: list[float] = shared_bgPositions

        # LOAD Resources
        root: str = "Resources/Sprites/Bgs/Space_bg/"
        self.Csillagok_1 =      pg.image.load(f"{root}Csillagok_1.png").convert_alpha()
        self.Csillagok_2 =      pg.image.load(f"{root}Csillagok_2.png").convert_alpha()
        self.Bolygok_1 =        pg.image.load(f"{root}Bolygók_1.png").convert_alpha()
        self.Kodok =            pg.image.load(f"{root}Ködök.png").convert_alpha()
        self.Csillagok_3 =      pg.image.load(f"{root}Csillagok_3.png").convert_alpha()
        self.Bolygok_2 =        pg.image.load(f"{root}Bolygók_2.png").convert_alpha()
        self.Background =       pg.image.load(f"{root}Background.png").convert()

        root = "Resources/Sprites/Objects/Main_Menu_texts/"
        self.CursorPic =        pg.image.load(f"{root}Cursor.png").convert_alpha()
        self.CreditsPic =       pg.image.load(f"{root}CREDITS.png").convert_alpha()
        self.NewGamePic =       pg.image.load(f"{root}NEW_GAME.png").convert_alpha()
        self.SettingsPic =      pg.image.load(f"{root}SETTINGS.png").convert_alpha()
        self.ExitPic =          pg.image.load(f"{root}EXIT.png").convert_alpha()


    def main(self):
        cursorPos_y: list[int] = [0, 26, 52, 78]      # TODO make it work
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
                        lg.debug("option selected")
                        return self.cursor_execute()
                    elif event.key == pg.K_h and (event.mod & pg.KMOD_CTRL):        # < Bitmask magic
                        clearScreen = not clearScreen

            self.draw_bg()
            if not clearScreen:     # TEXTS and CURSOR
                self.game_surface.blit(self.CursorPic,      (0, cursorPos_y[self.cursor]))
                self.game_surface.blit(self.CreditsPic,     (0,0))
                self.game_surface.blit(self.NewGamePic,     (0,0))
                self.game_surface.blit(self.SettingsPic,    (0,0))
                self.game_surface.blit(self.ExitPic,        (0,0))

            self.update_screen()


    def cursor_up(self) -> None:
        if self.cursor > 0:
            self.cursor -= 1
        lg.debug(f"cursor position: {self.cursor}")


    def cursor_down(self) -> None:
        if self.cursor < self.CURSOR_MAX:
            self.cursor += 1
        lg.debug(f"cursor position: {self.cursor}")


    # noinspection PyUnreachableCode
    def cursor_execute(self):
        match self.cursor:
            case 0:
                lg.debug("go to MainSt.GAME_LOOP")
                return MainSt.GAME_LOOP
            case 1:
                lg.debug("go to MainSt.MENU_SETTINGS")
                return MainSt.MENU_SETTINGS
            case 2:
                lg.debug("go to MainSt.CREDITS")
                # TODO make a credits screen
                return MainSt.CREDITS
            case 3:
                lg.debug("go to MainSt.EXIT")
                return MainSt.EXIT
            case _:
                lg.critical("Cursor invalid value?")
                raise Exception


    def draw_bg(self):
        MAX_DIFF: int = 1080

        self.game_surface.blit(self.Background, (0, 0))
        self.game_surface.blit(self.Bolygok_2, (0, self.bgPositions[5]))
        self.game_surface.blit(self.Bolygok_2, (0, self.bgPositions[5] + MAX_DIFF))
        self.game_surface.blit(self.Csillagok_3, (0, self.bgPositions[4]))
        self.game_surface.blit(self.Csillagok_3, (0, self.bgPositions[4] + MAX_DIFF))
        self.game_surface.blit(self.Kodok, (0, self.bgPositions[3]))
        self.game_surface.blit(self.Kodok, (0, self.bgPositions[3] + MAX_DIFF))
        self.game_surface.blit(self.Bolygok_1, (0, self.bgPositions[2]))
        self.game_surface.blit(self.Bolygok_1, (0, self.bgPositions[2] + MAX_DIFF))
        self.game_surface.blit(self.Csillagok_2, (0, self.bgPositions[1]))
        self.game_surface.blit(self.Csillagok_2, (0, self.bgPositions[1] + MAX_DIFF))
        self.game_surface.blit(self.Csillagok_1, (0, self.bgPositions[0]))
        self.game_surface.blit(self.Csillagok_1, (0, self.bgPositions[0] + MAX_DIFF))

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