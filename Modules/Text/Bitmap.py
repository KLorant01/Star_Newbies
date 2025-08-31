import pygame as pg
from Modules.Text.Fonts import *
import logging as lg


fonts: list = []


def create_fonts():
    global fonts
    fonts.append(BitmapFont(fontRegData, "font_regular"))
    lg.info(f"Fonts: {fonts}")


class BitmapFont:
    def __init__(self, font_data: dict, name:str = ""):
        self.fontName: str = name
        self.raw_image = pg.image.load(font_data["filePath"]).convert_alpha()
        self.charMap = font_data["charMap"]

        self.char_width_px = font_data["widthNumbers"]
        self.char_width_gap_px = font_data["withGaps"]
        self.char_height_px = font_data["heightNumbers"]
        self.char_height_gap_px = font_data["heightGaps"]

        self.glyphs = {}


        for i in range(len(self.charMap)):
            y = i * (int(self.char_height_gap_px) + int(self.char_height_px))

            ch_p: int = 0
            act_char_width_px: int = int(self.char_width_px[i])
            act_line: str = self.charMap[i]
            max_len = len(act_line)

            while ch_p < max_len:
                x = ch_p * (act_char_width_px + int(self.char_width_gap_px))
                rect = (x, y, act_char_width_px, int(self.char_height_px))
                self.glyphs.update({act_line[ch_p] : [self.raw_image.subsurface(rect), act_char_width_px]})

                ch_p += 1

            lg.info(f"New font {self.fontName} is created.")


# TODO add tördelés !!!
    def render(self, surface, text: str, pos: tuple):
        x, y = pos
        for char in text:
            if char in self.glyphs:
                act_glyphs = self.glyphs[char]
                surface.blit(act_glyphs[0], (x, y))
            else:
                raise SyntaxError(f"Unknown character detected in {text}")

            x += act_glyphs[1]
