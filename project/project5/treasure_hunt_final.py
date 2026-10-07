from player import Player
from room import Room
from item import Item
import os


# Get the directory where this Python file is located.
# This makes it possible to find the text and save files reliably.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create the path for the game's save file.
SAVE_FILE = os.path.join(BASE_DIR, "savegame.txt")


# Read and return the contents of a text file.
def read_file(filename):
    with open(filename, "r") as file:
        return file.read()


# Save the player's current game state to savegame.txt.
# The player's name, location and inventory are stored.
def save_game(player):
    with open(SAVE_FILE, "w") as file:
        file.write(player.name + "\n")
        file.write(player.location.name + "\n")


        # Save every item currently in the player's inventory.
        for item in player.items:
            file.write(item.name + "\n")

    print("Game saved.")


# Load the previously saved game from savegame.txt.
def load_game(player, rooms, items):
    try:
        with open(SAVE_FILE, "r") as file:
            # Read the save file and separate it into individual lines.
            lines = file.read().splitlines()

        # Restore the player's name.
        player.name = lines[0]

        # Restore the player's location.
        location_name = lines[1]

        # Find the room that matches the saved location.
        for room in rooms:
            if room.name == location_name:
                player.location = room
                break

        # Clear the current inventory before restoring the saved items.
        player.items = []

        # Restore the items saved in the player's inventory.
        for item_name in lines[2:]:
            for item in items:
                if item.name == item_name:
                    player.items.append(item)
                    break

        print("Saved game loaded.")
        return True

    # If there is no save file, the game starts as a new game.
    except FileNotFoundError:
        return False


# Display the game introduction and instructions from text files.
print(read_file(os.path.join(BASE_DIR, "intro.txt")))
print()
print(read_file(os.path.join(BASE_DIR, "instructions.txt")))
print()


# Ask the player for their basic information.
name = input("What is your name? ")
age = int(input("How old are you? "))


# Prevent players under 12 from continuing.
if age < 12:
    print("You are a minor.")
    exit()

print(f"Welcome {name}!!")


# Create the items used in the game.
sword = Item("Sword", 2)
key = Item("Key", 1)
potion = Item("Potion", 1)

# Store all items in a list so they can be used when loading a saved game.
items = [sword, key, potion]


# Create the rooms and place an item in each room.
forest = Room("Forest", sword)
castle = Room("Castle", key)
cave = Room("Cave", potion)

# Store all rooms in a list for the save/load system.
rooms = [forest, castle, cave]


# Create the player and start them in the Forest.
player = Player(name)
player.move(forest)

# Ask whether the player wants to continue a previously saved game.
continue_game = input("Do you want to continue a saved game? (yes/no): ")

if continue_game == "yes":
    # Try to restore the player's previous game state.
    if not load_game(player, rooms, items):
        print("No saved game was found.")
        player.name = name
        player.move(forest)
else:
    print("Starting a new game.")


# Main game loop. The menu continues until the player chooses to quit.
while True:
    print()
    print("You are in:", player.location.name)

    # Display the available player actions.
    print("Main menu:")
    print("move")
    print("collect")
    print("inventory")
    print("save")
    print("lopeta")

    command = input("Choose a command: ")

    # Move the player to another room.
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


    # Collect an item from the current room.
    elif command == "collect":
        player.collect_item()

    # Display the items currently carried by the player.
    elif command == "inventory":
        print("Your inventory:")

        if len(player.items) == 0:
            print("Your inventory is empty.")
        else:
            for item in player.items:
                print(item.name, "-", item.weight, "kg")

    # Save the current game state.
    elif command == "save":
        save_game(player)

    # Exit the game.
    elif command == "lopeta":
        print("Goodbye!")
        break

    # Handle commands that are not recognized.
    else:
        print("Unknown command.")