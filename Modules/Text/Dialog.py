from Modules.Text.Bitmap import fonts
from icecream import ic
import logging as lg

class DialogWindow:
    def __init__(self, text: list[str], dialog_name: str = "None", font: str = "font_regular"):
        self.text: list[str] = text
        self.dialogName: str = dialog_name
        self.fontName = font
        self.dialogProgressCounter: int = 0

        ic(fonts)
        for ft in fonts:
            ic(ft.fontName)
            ic(self.fontName)
            ic(ft.fontName == self.fontName)
            if ft.fontName == self.fontName:
                self.font = ft
                break
        else:
            raise Exception("Searched font not found")

        # noinspection PyUnreachableCode
        lg.info(f"New dialog {self.dialogName} is created")

    def draw_dialog(self, surface, pos: tuple[int,int]):
        if self.dialogProgressCounter < len(self.text):
            act_text = self.text[self.dialogProgressCounter]
            self.font.render(surface, act_text, pos)
        else:
            return