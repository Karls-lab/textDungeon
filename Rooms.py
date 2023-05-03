# Each room has a center, a forward, a right, a left, the origin
# What does each face have?: A description, items to pick up, and interactions to take
# Make a linear path with stone rooms
# Each has basic descriptons of what's inside the room and what is in the center of the room, and maybe
# basic items inside the room

import random
import json

class Room():
    def __init__(self):
        self.name = "name of room"
        self.items = []
        self.position = None
        self.visited = False
        self.north = None
        self.south = None
        self.east = None
        self.west = None
    
    def getName(self):
        return self.name
    
    def get_position(self):
        return self.position
    
    def go_north(self):
        return self.north

    def go_south(self):
        return self.south
    
    def go_east(self):
        return self.east
    
    def go_west(self):
        return self.west
    
    def get_possible_movement(self):
        possible_moves = []
        if self.north != None:
            possible_moves.append("North")
        if self.south != None:
            possible_moves.append("South")
        if self.east != None:
            possible_moves.append("East")
        if self.west != None:
            possible_moves.append("West")
        return possible_moves


# Total of 7 stone rooms, when the 7 rooms are done, print something
# Remove a room description everytime it fires. 
class stoneHallway(Room):
    def __init__(self):
        super().__init__()
        # for dictionaries, choose a random key, and then a random item in that key's list
        self.baseDescription = None
        self.elementalName = None
        self.elementalDescription = None
        self.fixedItemName = None
        self.fixedItemDescription = None
        self.fate = None
        self.generate()
        
    def generate(self):
        with open("./rooms/stoneRoom/description.json", "r") as f:
            data = json.load(f)
            random_selection = str(random.randint(0, len(data["stoneRoomFacesDescriptions"]) - 1))
            self.baseDescription = data["stoneRoomFacesDescriptions"][random_selection]

        #self.baseDescription = random.choice(stoneRoomFacesDescriptions)
        self.elementalName = random.choice(list(elementalDescription.keys()))
        self.elementalDescription = random.choice(elementalDescription[self.elementalName])
        self.fixedItemName = random.choice(list(fixedRoomItems.keys()))
        self.fixedItemDescription = random.choice(fixedRoomItems[self.fixedItemName])
        self.fate = "Nothing"

    def getDescription(self):
        return self.baseDescription

    def describeElementalEffects(self):
        return self.elementalDescription

    def descriptionOfFixedItems(self):
        return self.fixedItemDescription

    def searchFixedItem(self):  # will roll luck
        self.rollLuck()
        d = fixedRoomItemInteraction[self.fixedItemName]
        foundThing = random.choice(d[self.fate])
        return foundThing

    def rollLuck(self):
        options = ["Good", "Bad", "Nothing"]
        newFate = random.choice(options)
        self.fate = newFate


# DESCRIPTIONS OF ROOM AND THEIR PROPERTIES AND ITEMS
stoneRoomFacesDescriptions = [
    "The stone walls are smooth to the touch",
    "A spider web is caught within your fingers",
    "The hard, stone walls is cold to the touch",
    "The walls are lined with black drapes",
    "The room is built and lined with crudely constructed bricks",
    "Moss and lichen cling to the now slimy walls"
    ]

# A list of potential elemental effects, and their random choice descriptions.
elementalDescription = {
    "Water": [
        "Water drips from the celing",
        "You hear the rush of water somewhere beyond this room",
        "The room is damp"
        ],
    "Torch": [
        "flickering of light",
        "illuminated by "
        ],
    "Wind": [
        "A cool, damp breeze rustles your cloths",
        "You feel a cool, stale breeze"
        ]
    }

fixedRoomItems = {
    "Bookcase":[
        "A broken bookcase sags in the corner",
        "A moldy bookcase sits on the wall that houses several slimy books",
        "An old, dusty bookcase sits upright to your left"
        ],
    "Alter": [
        "A blood stained alter is in the center of the room",
        "An alter incribed with mysterious runes is in the center of the room"
        "You hear faint wispers as you look at the mysterious Hex diagrams on the floor"
        ],
    "Shrine": [
        "A shrine dedicated to an unknown God",
        "A broken shrine is decorated with burning incense"
        ],
    "Chest": [
        "A sturdy oak chest is sitting next to the wall",
        "A stone sarcophagus inscribed with ancient runes flanks left side of the room",
        "You see a dilapidated wooden chest with no lock"
    ]
}

fixedRoomItemInteraction = {
    "Bookcase":{
        "Good": ["Magic Scroll"],
        "Nothing": ["Dusty Books"],
        "Bad": ["Spiders"]
    },
    "Alter":{
        "Good": ["You feel warmth surround you"],
        "Nothing": ["You don't feel anything"],
        "Bad": ["You are cursed"]
    },
    "Shrine":{
        "Good": ["You feel blessed"],
        "Nothing": ["Nothing happens"],
        "Bad": ["One of the Gods does not think kindly of you"]
    },
    "Chest":{
        "Good": ["Sword", "Gold", "Amulet"],
        "Nothing": ["Cobwebs", "Maggots", "Mice"],
        "Bad": ["Mimic", "Arrow Trap"]
    }
}

# d = fixedRoomItemInteraction["Bookcase"]
# r = random.choice(list(d.keys()))
# print(r)
# print(d["Bad"])
# newRoom = stoneHallway()

# print(newRoom.baseDescription)
# print(newRoom.elementalDescription)
# print(newRoom.fixedItemDescription)
