
"""
Add effects to characters comming soon.

"""


class effect:
    def __init__(self, name: str, desc: str, duration_round: int):
        self.name: str = name
        self.description: str = desc
        self.duration: int = duration_round

    def __sub__(self, amount: int):
        self.duration -= amount
