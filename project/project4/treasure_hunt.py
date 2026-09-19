from player import Player
from room import Room
from item import Item


name = input("What is your name? ")
age = int(input("How old are you? "))

if age < 12:
    print("You are a minor.")
    exit()

print("Welcome", name + "!")


# Create items
sword = Item("Sword", 2)
key = Item("Key", 1)
potion = Item("Potion", 1)


# Create rooms
forest = Room("Forest", sword)
castle = Room("Castle", key)
cave = Room("Cave", potion)


# Create player
player = Player(name)
player.move(forest)


while True:
    print()
    print("You are in:", player.location.name)
    print("Main menu:")
    print("move")
    print("collect")
    print("inventory")
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

    elif command == "lopeta":
        print("Goodbye!")
        break

    else:
        print("Unknown command.")