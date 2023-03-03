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


# Total of 7 stone rooms, when the 7 rooms are done, print something
# Remove a room description everytime it fires. 
class stoneHallway(Room):
    # for dictionaries, choose a random key, and then a random item in that key's list
    def __init__(self):
        self.baseDescription = random.choice(stoneRoomFacesDescriptions)
        self.elementalName = random.choice(list(elementalDescription.keys()))
        self.elementalDescription = random.choice(elementalDescription[self.elementalName])
        self.fixedItemName = random.choice(list(fixedRoomItems.keys()))
        self.fixedItemDescription = random.choice(fixedRoomItems[self.fixedItemName])
        self.fate = "Nothing"

    def getDescription(self):
        stoneRoomFacesDescriptions.remove(self.baseDescription)
        return self.baseDescription

    def describeElementalEffects(self):
        elementalDescription.get(self.elementalName).remove(self.elementalDescription)
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
newRoom = stoneHallway()

print(newRoom.baseDescription)
print(newRoom.elementalDescription)
print(newRoom.fixedItemDescription)
