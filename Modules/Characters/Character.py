from Resources.Data.NAMES import NAMES
from random import choice, randint



class Character:
    global_ID: int = 0

    def __init__(self):
        self.ID: int = Character.global_ID
        Character.global_ID += 1
        self.name: str = ""
        self.race_description = ""
        self.level: int = 0

        self._baseStats: dict = {
            "STR": 7,
            "DEX": 7,
            "CON": 7,
            "INT": 7,
            "OBS": 7,
            "CHA": 7,
        }

        self._baseStats_2: dict = {
            "HP": 20,
            "Armore": 10,
            "Morale": 50,
        }

        self._baseCharacteristics = {
            "arms": 2,
            "legs": 2,
            "eyes": 2,

            "gender": None,
            "race": None,
            "humanoid": False,
        }

        self._modifiers: dict = {}

        self._baseAttributes: list = []
        self._baseEffects: list = []

        # MODIFIED STATS ######################################
        self.Stats: dict = {
            "STR": 7,
            "DEX": 7,
            "CON": 7,
            "INT": 7,
            "OBS": 7,
            "CHA": 7,
        }

        self.Stats_2: dict = {
            "HP": 20,
            "Armore": 10,
            "Morale": 50,
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
        for stat in self._baseStats:
            self._baseStats[stat] += stat_modify()
            if stat in self._modifiers:
                self._baseStats[stat] += self._modifiers[stat]

    def __str__(self):
        print(f"{self.name} ----------------------------")
        print(f"ID: {self.ID}\t Level: {self.level}\t Race: {self._baseStats["race"]}")
        print(f"{self._baseCharacteristics}")
        print(f"Base stats: {self._baseStats}\t{self._baseStats_2}\n")
        print(f"{self.Characteristics}")
        print(f"Base stats: {self.Stats}\t{self.Stats_2}\n")



def get_name(race, gender) -> str | None:
    probs: dict = NAMES[race][gender]
    sum_prob = 0
    chosen_prob = randint(0, 100)

    for act_prob in probs:
        sum_prob += act_prob
        if sum_prob > chosen_prob:
            return probs[act_prob]
    return None


def get_gender():
    return choice(["male", "female"])


def stat_modify(modif_range=None) -> int:
    if modif_range is None:
        modif_range = [-2, -1, 0, 1, 2]
    return choice(modif_range)


if __name__ == '__main__':
    print("Wrong file Bro...")

