class ExplorationPhase():
    def __init__(self, Explorer, Room):
        self.Explorer = Explorer
        self.Room = Room


    def examainItem(self):
        None

    def run(self):
        #This is where I will create my combat loop for 
        # encounters based on the list of attackers and defenders
        Explorer = self.Explorer
        Room = self.Room

        hasCombatEnded = False
        while(not hasCombatEnded):
            print("--------------------")
            print("available targets: ")
            for i in range(len(self.defenders)):
                defender = self.defenders[i]
                print(f'[{i}] {defender.name} HP: {defender.stats["HP"]}')
            targetId = int(input("Which one do you attack?: "))
            target = self.defenders[targetId]
            print(target)
            self.meleeAttack(attacker, target)
        