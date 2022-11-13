from Rooms import stoneHallway

class ExplorationPhase():
    def __init__(self, Explorer):
        self.Explorer = Explorer
        self.Room = stoneHallway()


    def examainItem(self):
        None

    def run(self):
        #This is where I will create my combat loop for 
        # encounters based on the list of attackers and defenders
        explorer = self.Explorer
        room = self.Room

        doneExploring = False
        while(not doneExploring):
            print("--------------------")
            room.printDescription()
            room.printElementalEffects()
            room.printFixedItemsInRoom()
            # newRoom = stoneHallway()
            # newRoom.getName
            # print(newRoom.baseDescription)
            # print(newRoom.elementalDescription)
            # print(newRoom.fixedItemDescription)

            doneExploring = True
        