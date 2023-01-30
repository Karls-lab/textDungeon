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
            print("You enter the Room")
            print(f'{room.getDescription()}')
            print(f'{room.describeElementalEffects()}')
            print(f'{room.descriptionOfFixedItems()} [{0}]')
            targetId = 1
            while(targetId != 0):
                targetId = int(input("What do you want to investigate? (Select a number) "))
                print(targetId)
            print(f'you are investigating feature: {targetId}')
            searchedItem = room.searchFixedItem()
            print(f'You found: {searchedItem}')
            

            doneExploring = True
        