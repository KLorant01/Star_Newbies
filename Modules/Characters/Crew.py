from random import randint
from Modules.Characters.Races import RACES, RACES_probs


def get_race():
    sum_prob = 0
    chosen_prob = randint(0, 99)

    for i in range(len(RACES_probs)):
        act_prob = RACES_probs[i]
        sum_prob += act_prob

        if sum_prob > chosen_prob:
            return RACES[i]
    return None


class Crew:
    def __init__(self, crew_size):
        self.characters: list = []

        for _ in range(crew_size):
            act_member = get_race()
            act_member().generate()
            self.characters.append(act_member)


if __name__ == '__main__':
    crew = Crew(4)
    print(crew.characters)



