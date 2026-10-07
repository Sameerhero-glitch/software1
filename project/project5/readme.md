# Treasure_Hunt

## Game Idea

Treasure Hunt is a simple text-based adventure game written in Python. The player explores different locations, collects items, and tries to complete the game by finding useful objects.

The game uses an object-oriented structure with separate classes for the player, rooms, and items. The program also uses text files for the game introduction and instructions and a save file so that the player can continue the game later.

## Objective

The objective of the game is to explore the available rooms and collect items. The player can move between the Forest, Castle, and Cave and collect the items found in these locations.

The player can check their inventory to see which items they have collected and can save their progress so that they can continue the game later.

## How the Game Works

When the game starts, the introduction and instructions are read from separate text files:

* 'intro.txt' contains the introduction to the game.
* 'instructions.txt' contains instructions for the player.

The player is then asked for their name and age. After this, the player can choose whether to continue a previously saved game or start a new game.

The main game menu provides the following commands:

* **move** – allows the player to move to another room.
* **collect** – collects an item from the current room.
* **inventory** – displays the items currently carried by the player.
* **save** – saves the current game state.
* **lopeta** – exits the game.

The game continues until the player chooses to exit.

## Game Structure

The project is divided into separate Python modules:

```text
project5/
│
├── treasure_hunt_final.py
├── player.py
├── room.py
├── item.py
├── intro.txt
├── instructions.txt
└── savegame.txt
```

### player.py

Contains the 'Player' class. A player has:

* a name
* an inventory containing collected items
* a current location

The 'Player' class also contains methods for moving and collecting items.

### room.py

Contains the 'Room' class. A room has:

* a name
* an item that can be collected

### item.py

Contains the 'Item' class. An item has:

* a name
* a weight

### treasure_hunt_final.py

This is the main program. It creates the player, rooms, and items, displays the game menu, and controls the game loop. It also handles reading text files and saving/loading the game.

## Saving and Loading

The game state is saved in 'savegame.txt'.

When the player chooses 'save', the program saves:

* the player's name
* the player's current location
* the items in the player's inventory

When the game starts again, the player can choose to continue a saved game. The program reads 'savegame.txt' and restores the saved information.

The current implementation uses one save file, so only one saved game can be stored at a time.

## Object-Oriented Programming

The game uses object-oriented programming to organize the different parts of the game.

The main classes are:

```text
Player
Room
Item
```

Objects are created from these classes. For example, the game creates different 'Item' objects for the sword, key, and potion, and different 'Room' objects for the Forest, Castle, and Cave.

This structure makes the program easier to organize and allows the different parts of the game to interact with each other.

## Sustainable Development

Sustainable development has been considered mainly through the design and implementation of the game.

The game is a text-based Python program, so it does not require large amounts of graphical resources, video, or other resource-intensive content. The game also uses simple text files for its introduction, instructions, and saved game data instead of requiring unnecessary external resources.

The game encourages exploration and problem-solving rather than requiring physical materials. This supports a more environmentally friendly digital learning experience.

The project also supports sustainable software development by separating the program into modules and classes. This makes the code easier to maintain, reuse, and improve instead of creating one large program that would be more difficult to modify.

