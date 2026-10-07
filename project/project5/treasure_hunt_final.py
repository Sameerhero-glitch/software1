from player import Player
from room import Room
from item import Item
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_FILE = os.path.join(BASE_DIR, "savegame.txt")


def read_file(filename):
    with open(filename, "r") as file:
        return file.read()


def save_game(player):
    with open(SAVE_FILE, "w") as file:
        file.write(player.name + "\n")
        file.write(player.location.name + "\n")

        for item in player.items:
            file.write(item.name + "\n")

    print("Game saved.")


def load_game(player, rooms, items):
    try:
        with open(SAVE_FILE, "r") as file:
            lines = file.read().splitlines()

        player.name = lines[0]

        location_name = lines[1]

        for room in rooms:
            if room.name == location_name:
                player.location = room
                break

        player.items = []

        for item_name in lines[2:]:
            for item in items:
                if item.name == item_name:
                    player.items.append(item)
                    break

        print("Saved game loaded.")
        return True

    except FileNotFoundError:
        return False


print(read_file(os.path.join(BASE_DIR, "intro.txt")))
print()
print(read_file(os.path.join(BASE_DIR, "instructions.txt")))
print()


name = input("What is your name? ")
age = int(input("How old are you? "))

if age < 12:
    print("You are a minor.")
    exit()

print(f"Welcome {name}!!")


# Create items
sword = Item("Sword", 2)
key = Item("Key", 1)
potion = Item("Potion", 1)

items = [sword, key, potion]


# Create rooms
forest = Room("Forest", sword)
castle = Room("Castle", key)
cave = Room("Cave", potion)

rooms = [forest, castle, cave]


# Create player
player = Player(name)
player.move(forest)


# Ask whether the player wants to continue a saved game
continue_game = input("Do you want to continue a saved game? (yes/no): ")

if continue_game == "yes":
    if not load_game(player, rooms, items):
        print("No saved game was found.")
        player.name = name
        player.move(forest)
else:
    print("Starting a new game.")


while True:
    print()
    print("You are in:", player.location.name)

    print("Main menu:")
    print("move")
    print("collect")
    print("inventory")
    print("save")
    print("lopeta")

    command = input("Choose a command: ")

    if command == "move":
        print("Available rooms:")
        print("forest")
        print("castle")
        print("cave")

        destination = input("Where do you want to go? ")

        if destination == "forest":
            player.move(forest)
            print("You moved to the forest.")

        elif destination == "castle":
            player.move(castle)
            print("You moved to the castle.")

        elif destination == "cave":
            player.move(cave)
            print("You moved to the cave.")

        else:
            print("Unknown room.")

    elif command == "collect":
        player.collect_item()

    elif command == "inventory":
        print("Your inventory:")

        if len(player.items) == 0:
            print("Your inventory is empty.")
        else:
            for item in player.items:
                print(item.name, "-", item.weight, "kg")

    elif command == "save":
        save_game(player)

    elif command == "lopeta":
        print("Goodbye!")
        break

    else:
        print("Unknown command.")