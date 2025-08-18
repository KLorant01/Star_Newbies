

class Character:
    def __init__(self):
        self.name: str = ""
        self.level: int = 0

        self.baseStats: dict = {
            "STR": 7,
            "DEX": 7,
            "CON": 7,
            "INT": 7,
            "OBS": 7,
            "CHA": 7,

            "HP": 20,
            "Armore": 10
            "Morale": 50
        }

        self.baseCharacteristics = {
            "arms": 0,
            "legs": 0,
            "eyes": 0,

            "gender": None,
            "race": None,
            "humanoid": False,
        }

        self.baseAttributes: list = [

        ]

# MODIFIED STATS ######################################
        self.Stats: dict = {
            "STR": 7,
            "DEX": 7,
            "CON": 7,
            "INT": 7,
            "OBS": 7,
            "CHA": 7,

            "HP": 20,
            "Armore": 10
            "Morale": 50
        }

        self.Characteristics = {
            "arms": 0,
            "legs": 0,
            "eyes": 0,

            "gender": None,
            "race": None,
            "humanoid": False,
        }

        self.Attributes: list = []
        self.Effects: list = []


    def generate(self):
        ...






