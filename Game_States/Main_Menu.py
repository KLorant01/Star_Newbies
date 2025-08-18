import pygame as pg
from Data.VARIABLES import FPS
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
        self.CURSOR_MAX: int = 3    # New Game, Settings, Credits, EXIT
        
        # LOAD Data
        self.default_bg = pg.image.load("Data/Bgs/resolution_test_2.png").convert_alpha()
        # TODO feliratok és kurzor


    def main(self):
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
                        return self.cursor_execute()


            # TODO kurzor mozgatása


            self.game_surface.fill((0, 255, 0))
            self.game_surface.blit(self.default_bg, (0, 0))

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


    def cursor_execute(self) -> st:
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
