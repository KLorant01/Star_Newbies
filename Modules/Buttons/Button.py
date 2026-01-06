import logging as lg
import pygame as pg
from Modules.Text.Bitmap import BitmapFont, fonts
from Resources.Data.VARIABLES import SCREEN_RES

#TODO make the screen fit!!!
#TODO Fix this shit


class Button:
    def __init__(self, name: str, x_min, x_max, y_min, y_max, text: str = "", border_thickness: int = 0, color: str = "red", font: str = "font_regular") -> None:
        self.name: str = name
        self.text: str = text
        # Kihagyhatóak...
        self.border_thickness: int = border_thickness
        self.color: str = color
        self.fontName = font

        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

        for ft in fonts:
            if ft.fontName == self.fontName:
                self.font = ft
                break
        else:
            raise Exception("Searched font not found")

        lg.debug(f"Button: {self.name} created")

        self.hover: bool = False


    def draw(self):
        videoInfo = pg.display.Info()
        screenWidth,screenHeight = videoInfo.current_w, videoInfo.current_h

        size =  ((SCREEN_RES[0]/screenWidth)*(self.x_max-self.x_min), (SCREEN_RES[0]/screenWidth)*(self.y_max-self.y_min))

        button_look = pg.Surface(size, pg.SRCALPHA)
        if self.border_thickness > 0:
            pg.draw.rect(button_look, self.color, button_look.get_rect(), self.border_thickness)
        else:
            pg.draw.rect(button_look, self.color, button_look.get_rect())

        if self.text != "":
            self.font.render(button_look, self.text, (0,0), (self.x_max-self.x_min, self.y_max-self.y_min))

        return button_look


    def action(self, cursor_x, cursor_y, pressed: int) -> bool:
        self.hover = False
        if not (self.x_min < cursor_x < self.x_max):
            return False
        if not (self.y_min < cursor_y < self.y_max):
            return False

        if pressed == 1:
            self.hover = False
            self.action_on_push()
        else:
            self.hover = True
            self.action_on_hover()
        return True


    def action_on_hover(self):
        lg.debug(f"Button: {self.name} hover")


    def action_on_push(self):
        lg.debug(f"Button: {self.name} pressed")