from Modules.Characters.Character import Character, get_name, get_gender


class Human(Character):
    def __init__(self):
        super().__init__()
        self.race_description = "Basic Human"        # TODO make

        gender: str = get_gender()
        self.name = get_name("Human", gender)
        self._baseCharacteristics["gender"] = gender
        self._baseCharacteristics["race"] = "Human"
        self._baseCharacteristics["humanoid"] = True

        self._modifiers: dict = {
            "STR": -1,
            "CON": -2,
            "CHA": +1,
            "DEX": +1,
            "INT": +1
        }


class Racoon(Character):
    def __init__(self):
        super().__init__()
        self.race_description = "Basic Racoon"        # TODO make

        gender: str = get_gender()
        self.name = get_name("Racoon", gender)
        self._baseCharacteristics["gender"] = gender
        self._baseCharacteristics["race"] = "Racoon"
        self._baseCharacteristics["humanoid"] = False

        self._modifiers: dict = {
            "STR": -2,
            "CON": -2,
            "DEX": +3,
            "INT": +1
        }


RACES_probs: list = [
    50,
    50,
#    10,
#    10,
]

RACES: list = [
    Human,
    Racoon,
    #    10 : Obin,
    #    10 : Wogon,
]
