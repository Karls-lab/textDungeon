from Rooms import stoneHallway

class ExplorationPhase():
    def __init__(self, Explorer, tile):
        self.Explorer = Explorer
        self.Room = tile
        self.next_room = None


    def examainItem(self):
        None

    def get_next_tile(self):
        return self.next_room

    def run(self):
        #This is where I will create my combat loop for 
        # encounters based on the list of attackers and defenders

        doneExploring = False
        while(not doneExploring):
            print("--------------------")
            print(f"You enter the Room {self.Room.get_position()}")
            print(f'{self.Room.getDescription()}')
            print(f'{self.Room.describeElementalEffects()}')
            print(f'{self.Room.descriptionOfFixedItems()} [{0}]')


            next_room = input(f"Do you want to go? {self.Room.get_possible_movement()}").upper()
            if next_room == "N":
                self.next_room = self.Room.go_north()
            if next_room == "S":
                self.next_room = self.Room.go_south()
            if next_room == "E":
                self.next_room = self.Room.go_east()
            if next_room == "W":
                self.next_room = self.Room.go_west()
            


            # targetId = 1
            # while(targetId != 0):
            #     targetId = int(input("What do you want to investigate? (Select a number) "))
            #     print(targetId)
            # print(f'you are investigating feature: {targetId}')
            # searchedItem = self.Room.searchFixedItem()
            # print(f'You found: {searchedItem}')
            

            doneExploring = True
        