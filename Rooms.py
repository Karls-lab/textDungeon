# Each room has a center, a forward, a right, a left, the origin
# What does each face have?: A description, items to pick up, and interactions to take
# Make a linear path with stone rooms
# Each has basic descriptons of what's inside the room and what is in the center of the room, and maybe
# basic items inside the room

import random

class Room():
    def __init__(self):
        self.name = "name of room"
        self.items = []
    
    def getName(self):
        return self.name



class stoneHallway(Room):
    def __init__(self):
        self.baseDescription = random.choice(stoneRoomFacesDescriptions)
        self.elemental = random.choice(elemental)
        self.elementalDescription = random.choice(elementalDescription[self.elemental])
        self.fixedItem = random.choice(fixedRoomItems)
        self.fixedItemDescription = random.choice(fixedRoomItemsDescriptions[self.fixedItem])

    def printDescription(self):
        print(self.baseDescription)

    def printElementalEffects(self):
        print(self.elementalDescription)

    def printFixedItemsInRoom(self):
        print(self.fixedItemDescription)




stoneRoomFacesDescriptions = ["The stone wall is smooth to the touch",
    "A spider web is caught within your fingers",
    "The hard, stone wall is cold to the touch",
    "The wall of stone bricks lay bare",
    "There's a wall of crudely chisled stone bricks",
    ]

elemental = ["Water", "Torch", "Wind"]
elementalDescription = {
    "Water": ["Water drips from the celing", "You hear the rush of water somewhere beyond this room",
             "The room is damp"],
    "Torch": ["flickering of light", "illuminated by "],
    "Wind": ["A cool, damp breeze rustles your cloths", "You feel a cool stale breeze"]
    }

fixedRoomItems = ["Bookcase", "Alter", "Shrine"]
fixedRoomItemsDescriptions = {
    "Bookcase": ["A broken bookcase sags in the corner", "A moldy bookcase houses several slimy books",
            "An old, dusty bookcase sits upright"],
    "Alter": ["A blood stained alter", "An alter incribed with mysterious runes"],
    "Shrine": ["A shrine dedicated to an unknown God", "A broken shrine is decorated with burning incense"]
}


# newRoom = stoneHallway()
# newRoom.getName
# print(newRoom.baseDescription)
# print(newRoom.elementalDescription)
# print(newRoom.fixedItemDescription)
