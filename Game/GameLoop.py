import pygame as pg
from Resources.Data.VARIABLES import FPS
from icecream import ic
from Resources.Data.Enums import MainSt, GameSt

class Button:
    def __init__(self, name: str, x_min, x_max, y_min, y_max):
        self.name = name
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

        self.hower: bool = False

    def action(self, cursorposx, cursorposy, pressed: int) -> bool:
        self.hower = False
        if not (self.x_min < cursorposx < self.x_max):
            return False
        if not (self.y_min < cursorposy < self.y_max):
            return False

        if pressed == 1:
            self.hower = False
            self.action_on_push()
        else:
            self.hower = True
            self.action_on_hover()
        return True


    def action_on_hover(self):
        ic(f"Button: {self.name} howerd")


    def action_on_push(self):
        ic(f"Button: {self.name} pushed")



class GameLoop:
    def __init__(self, game_surface, screen, clock, screenwidth, screenweight):
        self.game_surface = game_surface
        self.screenWidth = screenwidth
        self.screenHeight = screenweight
        self.screen = screen
        self.clock = clock

        self.game_state = GameSt.MAIN_SCREEN


        # TODO: finomhangold
        self.buttons = [
            Button("Left Upper Corner", 0, 90, 0, 90),
            Button("Left Bottom Corner", 0, 90, 1022, 960),
            Button("Right Upper Corner", 860, 950, 0, 90),
            Button("Right Bottom Corner", 860, 950, 1022, 960),
            Button("Ship in the Middle", 280, 830, 0, 1022),
        ]

        # LOAD Resources
        # TODO change
        self.default_bg = pg.image.load("Resources/Sprites/Bgs/resolution_test_2.png").convert_alpha()


    def loop(self):
        while 1:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return MainSt.MAIN_MENU
                elif event.type == pg.KEYDOWN:
                   ...
                elif event.type == pg.MOUSEMOTION:
                    self.maus_handler(event)

                elif event.type == pg.MOUSEBUTTONDOWN:
                    self.maus_handler(event, event.button)




            self.game_surface.fill((0, 0, 255))
            self.game_surface.blit(self.default_bg, (0, 0))

            # Screen work
            scaled_surface = pg.transform.scale(self.game_surface, (self.screenWidth, self.screenHeight))
            self.screen.blit(scaled_surface, (0, 0))
            pg.display.flip()
            self.clock.tick(FPS)

    def maus_handler(self, event, push: int = 0):
        pos = event.pos
        cursorPosX, cursorPosY = pos[0], pos[1]
        print(cursorPosX)
        print(cursorPosY)
        print(push)

        for button in self.buttons:
            if button.action(cursorPosX, cursorPosY, push):
                break

