import pygame as pg
import logging as lg
from icecream import ic


# TODO FIX THIS FUCKING SHIT


fonts: list = []

fontRegData: dict = {
        "filePath" :        "Resources/Sprites/Objects/Text/Text_1/Aseprite_mini_fontmap.png",
        "charMap" :         "ABCDEFGHKPRSTXYZabcdeghknopqrsuxyz023456789+/#= '\nMWmv\nNOQUV4?\nJLFjt1-\nIil.,!\r",
        "widthNumbers" :    "46532",    # Width
        "withGaps" :        "0",        # gap
        "heightNumbers" :   "6",        # Height
        "heightGaps" :      "2",        # gap
    }


def create_fonts():
    global fonts
    fonts.append(BitmapFont(fontRegData, "font_regular"))
    ic(fonts)



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

        # slice the sheet into glyphs
#        sheet_width_px = self.raw_image.get_width() // (int(self.char_width_px[0]) + int(self.char_width_gap_px[0]))
        sheet_height_px = self.raw_image.get_height() // (int(self.char_height_px[0]) + int(self.char_height_gap_px[0]))


        ch_counter: int = 0
        for i in range(sheet_height_px):
            y = i * (int(self.char_height_gap_px) + int(self.char_height_px))

            ch_p: int = 0
            max_len: int = self.count_character_sep_to_sep(self.charMap, i)
            act_char_width_px = int(self.char_width_px[i])
            while ch_p < max_len-2:
                x = ch_p * (act_char_width_px + int(self.char_width_gap_px))

                # get the section
                rect = (x, y, act_char_width_px, int(self.char_height_px))
                self.glyphs.update({self.charMap[ch_counter] : [self.raw_image.subsurface(rect), act_char_width_px]})

                ch_p += 1
                ch_counter += 1

            ch_counter += 1
            lg.info(f"New font {self.fontName} is created.")


# TODO add tördelés !!!
    def render(self, surface, text, pos: tuple):
        x, y = pos
        for char in text:
            if char in self.glyphs:
                act_glyphs = self.glyphs[char]
                surface.blit(act_glyphs[0], (x, y))
            x += act_glyphs[1]


    @staticmethod
    def count_character_sep_to_sep(string: str, st: int):
        st = st
        sub_str: str = ""
        i, counter = 0, 0

        while 1:
            if string[i] == "\n" or string[i] == "\r":
                st -= 1
                if st < 0:
                    break
            elif st == 0:
                sub_str += string[i]
                counter += 1

            i += 1

        return counter
