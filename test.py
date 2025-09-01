from Modules.Events.Events import Event, new_event


game_data: dict = {
    "events" : [],
    "crew" : [],
}


event = new_event(game_data)
game_data["events"].append(event.name)

print(game_data)

event = new_event(game_data)
game_data["events"].append(event.name)


print(game_data)
