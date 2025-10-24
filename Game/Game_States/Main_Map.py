from random import choice


LEVEL_JUMP_PROBABILITY: list[int] = [-1, 0, 0, 0, +1, +1, +1, +1]
MAX_LEVEL: int = 3



class Map:
    def __init__(self):
        self.past_positions: list[str] = []
        self.act_level = 1
        self.act_position: str = "Earth"
        self.act_position: str = self.chose_place_by_level(1)


    def move(self):
        self.past_positions.append(self.act_position)
        self.change_level()
        self.act_position: str = "Eart"
        self.act_position = self.chose_place_by_level(self.act_level)


    def __str__(self):
        ret_str: str = f"Act position: {self.act_position} \n\n"
        for past_pos in self.past_positions:
            ret_str += f" - {past_pos}\n"
        ret_str += f"\n\n"
        return ret_str


    def change_level(self):
        self.act_level += choice(LEVEL_JUMP_PROBABILITY)
        if self.act_level < 1: self.act_level = 1
        elif self.act_level > MAX_LEVEL: self.act_level = MAX_LEVEL


    def chose_place_by_level(self, level) -> str:
        chosen = self.act_position
        chose_list: list = [map_name for map_name in MAP if MAP[map_name]["level"] == level]
        while chosen == self.act_position:
            chosen = choice(chose_list)
        return chosen



MAP = {
    "Nebula System": {
        "level": 1,
        "size": 20,
        "distance_ly": 3,
        "bgs": [],
        "bg_speed": []
    },

    "The Great Fog": {
        "level": 1,
        "size": 50,
        "distance_ly": 8,
        "bgs": [],
        "bg_speed": []
    },

    "Lil Dwarf System": {
        "level": 2,
        "size": 15,
        "distance_ly": 7,
        "bgs": [],
        "bg_speed": []
    },

    "Big Dwarf System": {
        "level": 3,
        "size": 15,
        "distance_ly": 14,
        "bgs": [],
        "bg_speed": []
    },

}

if __name__ == '__main__':
    alma = Map()
    print(alma)
    for _ in range(5):
        alma.move()
        print(alma)
