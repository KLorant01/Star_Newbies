import pygame as pg
from icecream import ic


fontData = [
        "Resources/Sprites/Objects/Text/Text_1/Aseprite_mini_fontmap.png",
        "ABCDEFGHKPRSTXYZabcdeghknopqrsuxyz023456789+/#= '\nMWmv\nNOQUV4?\nJLFjt1-\nIil.,!\r",
        "46532",    # Width
        "0",        # gap
        "6",        # Height
        "2",        # gap
    ]


class BitmapFont:
    fontCounter: int = 0
    def __init__(self, font_data: list):
        self.raw_image = pg.image.load(font_data[0]).convert_alpha()
        self.charMap = font_data[1]

        self.char_width_px = font_data[2]
        self.char_width_gap_px = font_data[3]
        self.char_height_px = font_data[4]
        self.char_height_gap_px = font_data[5]

        self.glyphs = {}

        fonCounter += 1


        # slice the sheet into glyphs
        sheet_width_px = self.raw_image.get_width() // (int(self.char_width_px[0]) + int(self.char_width_gap_px[0]))
        sheet_height_px = self.raw_image.get_height() // (int(self.char_height_px[0]) + int(self.char_height_gap_px[0]))


        ch_counter: int = 0
        for i in range(sheet_height_px):
            y = i * (int(self.char_height_gap_px) + int(self.char_height_px))

            ch_p: int = 0
            max_len: int = self.count_character_sep_to_sep(self.charMap, i)
            act_char_width_px = int(self.char_width_px[i])
            while ch_p < max_len-1:
                x = ch_p * (act_char_width_px + int(self.char_width_gap_px))

                # get the section
                ic(x)
                ic(y)
                ic(act_char_width_px)
                ic(self.char_height_px)

                rect = (x, y, act_char_width_px, int(self.char_height_px))
                ic(rect)
                self.glyphs.update({self.charMap[ch_counter] : self.raw_image.subsurface(rect)})

                ch_p += 1
                ch_counter += 1

            ch_counter += 1

#        i = 0
#        for y in range(sheet_height):
#            for x in range(sheet_width):
#                if i >= len(self.chars):
#                    break
#                rect = pg.Rect(x * char_width, y * char_height, char_width, char_height)
#                self.glyphs[chars[i]] = self.raw_image.subsurface(rect)
#                i += 1


# TODO add tördelés !!!
    def render(self, surface, text, pos):
        x, y = pos
        for char in text:
            if char in self.glyphs:
                surface.blit(self.glyphs[char], (x, y))
            x += self.char_width

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



# font_reg = BitmapFont()
