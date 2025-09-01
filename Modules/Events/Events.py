import logging as lg
import random


# TODO test this out

class Event:
    global_events: list[str] = []
    global_id: int = 0

    def __init__(self, name: str, probability: float, dialog: list, criteria_settings: dict[str : bool], **kwargs):
        self.id_: int = Event.global_id
        Event.global_id += 1

        self.name: str = name
        self.probability: float = probability
        self.dialog: list = dialog

        if "repeatable" in criteria_settings:
            self.repeatable: bool = criteria_settings["repeatable"]

        self.criterias: list = []
        self.kwargs: dict = kwargs

        criteria_options: dict = {
            "criteria_event_happened" :                 self.criteria_event_happened,
            "criteria_event_not_happened" :             self.criteria_event_not_happened,
            "crew_contains_race" :                      self.crew_contains_race,
            "crew_contains_race_opposite_gender" :      self.crew_contains_race_opposite_gender,
        }

        for key in criteria_options:
           if key in criteria_settings:
               if criteria_settings[key]:
                    self.criterias.append(criteria_options[key])


    def criteria_handler(self, act_game_data: dict) -> bool:
        global events

        for criteria in self.criterias:
            if not criteria(act_game_data):
                return False

        if not self.repeatable:
            self.probability = 0

        return True


    def criteria_event_happened(self, act_game_data) -> bool:
        for event in act_game_data["events"]:
            if not event in self.kwargs["mustHaveEvents"]:
                return False
        return True


    def criteria_event_not_happened(self, act_game_data) -> bool:
        for event in act_game_data["events"]:
            if event in self.kwargs["blockingEvents"]:
                return False
        return True


    def crew_contains_race(self, act_game_data) -> bool:
        if "mustHaveRaceCount" in self.kwargs:  raceDeCounter: int = self.kwargs["mustHaveRaceCount"]
        else:                                   raceDeCounter: int = 1

        for member in act_game_data["crew"]:
            if member.race == self.kwargs["mustHaveRace"]:
                raceDeCounter -= 1
                if raceDeCounter == 0:
                    return True

        return False

    def crew_contains_race_opposite_gender(self, act_game_data) -> bool:
        requirementNumber: int = 0
        for member in act_game_data["crew"]:
            if member.race == self.kwargs["mustHaveRace"]:
                match member.sex:
                    case "male":            requirementNumber += 1
                    case "female":          requirementNumber += 100
                    case "Hermaphrodite":   pass

        if requirementNumber > 100 and requirementNumber % 100 != 0:    return True
        return False



# EVENT CHOOSER
def new_event(act_game_data: dict) -> Event:
    OVERFLOW: int = 100
    global events

    past_events = events.copy()
    probability_sum: float = 0
    for event in past_events:
        if event.probability == 0:
            events.remove(event)
        else:
            probability_sum += event.probability

    for _ in range(OVERFLOW):
        chosen = random.random() * probability_sum
        chosen_sum: float = 0
        for event in events:
            chosen_sum += event.probability
            if chosen_sum >= chosen and event.criteria_handler(act_game_data):
                return event

    lg.info("No event is compatible")
    raise Exception("No event is compatible")



events = [
    Event(
        name= "A Good Start",
        probability= 1000000.0,
        dialog= [
            "Hey Capitan, how are you doing? Your crew is really excited about the mission.",
            "Yes, we are!",
            "People, don't be superficial! There is a long road ahead of us. We need to be sure that everything works fine.",
            "Who's gana check the crucial systems?",
        ],
        criteria_settings= {
            "repeatable":                           False,
            "criteria_event_happened" :             False,
            "criteria_event_not_happened" :         False,
            "crew_contains_race" :                  False,
            "crew_contains_race_opposite_gender" :  False,
        },
    ),

    Event(
        name= "The Beautiful Love",
        probability= 20,
        dialog= [
            "Oh Capitan! I feel something strange lately around {name}. I have no idea what should I doo with this feeling."
        ],
        criteria_settings= {
            "crew_contains_race_opposite_gender":   True,
        },
        mustHaveGender= "Human"
    ),
]


print(events)

