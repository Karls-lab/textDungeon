class CombatPhase():
    def __init__(self, player, monsters: list):
        self.player = player
        self.monsters = monsters


    def meleeAttack(self, attacker, defender):
        print("--------------------")
        print(attacker.name + " attacked " + defender.name)
        attackModifer = attacker.stats["STR"]
        attackRoll = attacker.attackRoll() + attackModifer
        print(attacker.name + "'s  attack roll was: " + str(attackRoll))
        if(defender.compareAC(attackRoll)):
            print(attacker.name + " Hits!")
            dmg = attacker.attackDamage()
            defender.takeDamage(dmg)
            print(str(defender.name) + " took " + str(dmg) + " Damage! Their health is now: " + str(defender.getHealth()))
        else:
            print(str(attacker.name) + " misses!")


    def run(self):
        #This is where I will create my combat loop for 
        # encounters based on the list of attackers and defenders
        
        if len(self.monsters) == 0:
            return None

        hasCombatEnded = False
        while(not hasCombatEnded):
            print("--------------------") # Player selects monster/s to attack
            print("available targets: ")
            for count, monster in enumerate(self.monsters):
                print(f'{monster.name}[{count}] HP: {monster.stats["HP"]}')

            # Player Attacks Monsters
            targetId = int(input("Which one do you attack?: "))
            target = self.monsters[targetId]
            self.meleeAttack(self.player, target)

            # Check if player killed any monsters
            for monster in self.monsters:
                if monster.isDead():
                    print(f'You killed the {monster.name}')
                    self.monsters.remove(monster)

            # If there are no more monsters, exit the loop
            if len(self.monsters) <= 0:
                hasCombatEnded = True

            # Monsters attack player
            print("--------------------") 
            for monster in self.monsters:
                print(self.monsters)
                self.meleeAttack(monster, self.player)
