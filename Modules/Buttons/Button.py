import logging as lg

class Button:
    def __init__(self, name: str, x_min, x_max, y_min, y_max) -> None:
        self.name = name
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

        lg.info(f"Button: {self.name} created")

        self.hover: bool = False

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
        lg.info(f"Button: {self.name} pressed")