import pygame as pg
from Resources.Data.Fonts import *
import logging as lg


fonts: list = []


def create_fonts():
    global fonts
    a = BitmapFont(fontRegData, "font_regular")
    fonts.append(a)
    lg.info(f"Fonts: {fonts}")


class BitmapFont:
    def __init__(self, font_data: dict, name:str = ""):
        self.fontName: str = name
        self.raw_image = pg.image.load(font_data["filePath"]).convert_alpha()
        self.charMap = font_data["charMap"]

        self.char_width_px = font_data["widthNumbers"]
        self.char_width_gap_px = int(font_data["withGaps"])
        self.char_height_px = font_data["heightNumbers"]
        self.char_height_gap_px = int(font_data["heightGaps"])

        self.glyphs = {}


        for i in range(len(self.charMap)):
            y = i * (self.char_height_gap_px + int(self.char_height_px))

            ch_p: int = 0
            act_char_width_px: int = int(self.char_width_px[i])
            act_line: str = self.charMap[i]
            max_len = len(act_line)

            while ch_p < max_len:
                x = ch_p * (act_char_width_px + self.char_width_gap_px)
                rect = (x, y, act_char_width_px, int(self.char_height_px))
                self.glyphs.update({act_line[ch_p] : [self.raw_image.subsurface(rect), act_char_width_px]})

                ch_p += 1

        lg.info(f"New font [{self.fontName}] is created.")


    def render(self, surface, text: str, pos: tuple[int, int], window: tuple[int, int]):
        """
        :param surface: There will be the text
        :param text: Don't be stupid
        :param pos: the upper LEFT corner of the text
        :param window: the lower RIGHT corner of the text
        :return: Nothing. It just works LoL
        """

        x, y = pos
        window_x, window_y = window
        words: list[str] = []
        word: str = ""

        for ch in text:     # Parce the text to words
            word += ch
            if ch == " ":
                words.append(word)
                word = ""
        words.append(word)

        for word in words:
            wordLenght: int = 0
            for ch in word:
                if ch in self.glyphs:
                    act_glyphs = self.glyphs[ch]
                else: raise SyntaxError(f"Unknown character detected in {text}")
                wordLenght += act_glyphs[1]

            # IF WORD BIG, MAKE IT NEW LINE UGA BUGA!
            if wordLenght > window_x:
                raise Exception("WTF IS THIS MONSTROSITY OF A WORD BRO?!")
            elif x + wordLenght > window_x:
                y += self.char_height_gap_px + int(self.char_height_px)
                x = pos[0]
            if y > window_y:
                raise Exception("Text to BIG! \n DOES NOT FIT IN THE FUCK'IN WINDOW!!!")

            for ch in word:     # < draw the word into it's place
                if ch in self.glyphs:
                    act_glyphs = self.glyphs[ch]
                    surface.blit(act_glyphs[0], (x, y))
                else: raise SyntaxError(f"Unknown character detected in {text}")
                x += act_glyphs[1]

