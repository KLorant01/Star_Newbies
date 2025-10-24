from Modules.Text.Bitmap import fonts
import logging as lg


class DialogManager:
    def __init__(self, text: list[str] = "", dialog_name: str = "None", font: str = "font_regular"):
        self.text: list[str] = text
        self.dialogName: str = dialog_name
        self.fontName = font
        self.dialogProgressCounter: int = 0

        for ft in fonts:
            if ft.fontName == self.fontName:
                self.font = ft
                break
        else:
            raise Exception("Searched font not found")

        # noinspection PyUnreachableCode
        lg.debug(f"New dialog {self.dialogName} is created")


    def draw_dialog(self, surface, pos: tuple[int, int], window: tuple[int, int]=(320,180)):

        if self.dialogProgressCounter < len(self.text):
            act_text = self.text[self.dialogProgressCounter]
            lg.debug(f"{self.dialogProgressCounter}\t{act_text}")
            self.font.render(surface, act_text, pos, window)
        else:
            return


    def trow_dialog(self, game_progress: list):
        ...
