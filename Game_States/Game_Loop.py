import pygame as pg
from Data.VARIABLES import FPS
from icecream import ic
from Data.Enums import main_st, game_st

class Button:
    def __init__(self, name: str, x_min, x_max, y_min, y_max):
        self.name = name
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
1
        self.hower: bool = False

    def action(self, cursorPosX, cursorPosY, pressed: int) -> bool:
        self.hower = False
        if not (self.x_min < cursorPosX < self.x_max):
            return False
        if not (self.y_min < cursorPosY< self.y_max):
            return False

        if pressed == 1:
            self.hower = False
            self.actionOnPush()
        else:
            self.hower = True
            self.actionOnHover()
        return True


    def actionOnHover(self):
        ic(f"Button: {self.name} howerd")


    def actionOnPush(self):
        ic(f"Button: {self.name} pushed")



class Game_Loop:
    def __init__(self, game_surface, screen, clock, screenWidth, screenHeight):
        self.game_surface = game_surface
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.screen = screen
        self.clock = clock

        self.game_state = game_st.MAIN_SCREEN


        # TODO: finomhangold
        self.buttons = [
            Button("Left Upper Corner", 0, 90, 0, 90),
            Button("Left Bottom Corner", 0, 90, 1022, 960),
            Button("Right Upper Corner", 860, 950, 0, 90),
            Button("Right Bottom Corner", 860, 950, 1022, 960),
            Button("Ship in the Middle", 280, 830, 0, 1022),

        ]

        # LOAD Data
        # TODO change
        self.default_bg = pg.image.load("Data/Bgs/resolution_test_2.png").convert_alpha()


    def loop(self):
        while 1:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return main_st.MAIN_MENU
                elif event.type == pg.KEYDOWN:
                   ...
                elif event.type == pg.MOUSEMOTION:
                    self.MousHandler(event)

                elif event.type == pg.MOUSEBUTTONDOWN:
                    self.MousHandler(event, event.button)




            self.game_surface.fill((0, 0, 255))
            self.game_surface.blit(self.default_bg, (0, 0))

            # Screen work
            scaled_surface = pg.transform.scale(self.game_surface, (self.screenWidth, self.screenHeight))
            self.screen.blit(scaled_surface, (0, 0))
            pg.display.flip()
            self.clock.tick(FPS)

    def MousHandler(self, event, push: int = 0):
        pos = event.pos
        cursorPosX, cursorPosY = pos[0], pos[1]
        print(cursorPosX)
        print(cursorPosY)
        print(push)

        for button in self.buttons:
            if button.action(cursorPosX, cursorPosY, push):
                break

