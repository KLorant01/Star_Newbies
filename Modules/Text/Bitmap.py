import pygame as pg


fontChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,!?-+/*= "

class BitmapFont:
    def __init__(self, filename, char_width, char_height, chars):
        self.image = pg.image.load(filename).convert_alpha()
        self.char_width = char_width
        self.char_height = char_height
        self.chars = chars
        self.glyphs = {}

        # slice the sheet into glyphs
        sheet_width = self.image.get_width() // char_width
        sheet_height = self.image.get_height() // char_height

        i = 0
        for y in range(sheet_height):
            for x in range(sheet_width):
                if i >= len(chars):
                    break
                rect = pg.Rect(x * char_width, y * char_height, char_width, char_height)
                self.glyphs[chars[i]] = self.image.subsurface(rect)
                i += 1



    def render(self, surface, text, pos):
        x, y = pos
        for char in text:
            if char in self.glyphs:
                surface.blit(self.glyphs[char], (x, y))
            x += self.char_width


# font_reg = BitmapFont()
