def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = [f"Hello, my name is {name}." for name in names]
    return badges

def assign_rooms(names):
    rooms = range(1, len(names) +1)
    messages = [f"Hello, {name}! You'll be assigned to room {room}!" for name, room in zip(names, rooms)]
    return messages

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)

    for badge, room_assignment in zip(badges, room_assignments):
        print(f"Hello, my name is {badge}.")
        print(f"Hello, {badge}! You'll be assigned to {room_assignment}.")
