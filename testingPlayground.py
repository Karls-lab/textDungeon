import json
import random

with open("./rooms/stoneRoom/description.json", "r") as f:
    data = json.load(f)
    random_selection = str(random.randint(0, len(data["stoneRoomFacesDescriptions"]) - 1))
    print(data["stoneRoomFacesDescriptions"][random_selection])