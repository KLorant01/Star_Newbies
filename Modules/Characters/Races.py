from Modules.Characters.Crew import Character, get_name, get_gender






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

RACES: dict = {
    100: Human,
#    30 : Racoon,
#    10 : Obin,
#    10 : Wogon,
}
