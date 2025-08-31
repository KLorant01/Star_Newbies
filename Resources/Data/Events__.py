import random

# TODO test this out

class Event:
    global_events: list[str] = []

    def __init__(self, id_: int, name: str, probability: float, dialog: list, criteria_settings: list[bool], **kwargs):
        self.id_: int = id_
        self.name: str = name
        self.probability: float = probability
        self.dialog: list = dialog
        self.criterias: list = []
        self.kwargs: dict = kwargs

        criteria_options = [
            self.criteria_event_happened,
            self.criteria_event_not_happened,
        ]

        for i in range(len(criteria_options)):
           if criteria_settings[i]:
               self.criterias.append(criteria_options[i])


    def criteria_handler(self, act_game_data: dict) -> bool:
        for criteria in self.criterias:
            if not criteria(act_game_data):
                return False
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


    def crew_member(self) -> bool:
        ...


def new_event(act_game_data: dict) -> Event:
    OVERFLOW: int = 100

    probability_sum: float = 0
    for event in events:
        probability_sum += event.probability

    for _ in range(OVERFLOW):
        chosen = random.random() * probability_sum
        chosen_sum: float = 0
        for event in events:
            chosen_sum += event.probability
            if chosen_sum >= chosen and event.criteria_handler(act_game_data):
                return event

    raise Exception("No event is compatible")


events = [
    Event( id_= 0,
          name= "A Good Start",
          probability= 1000000.0,
          dialog= [
              "Hey Capitan, how are you doing? Your crew is really excited about the mission."
              "Yes, we are!"
              "People, don't be superficial! There is a long road ahead of us. We need to be sure that everything works fine."
              "Who's gana check the crucial systems?"
          ],
           criteria_settings= [
               False,
               True
           ],
           blockingEvents=["A Good Start"]
          )

]

